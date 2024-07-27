import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Create distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    dist_matrix = {}
    for from_counter in range(size):
        dist_matrix[from_counter] = {}
        for to_counter in range(size):
            distance = euclidean_distance(coordinates[from_counter], coordinates[to_counter])
            dist_matrix[from_counter][to_counter] = distance
    return dist_matrix

distance_matrix = create_distance_matrix(coordinates)

# Initialize routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), 2, [0, 1], [0, 1])
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    # Convert from routing variable Index to distance matrix NodeIndex.
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Set distance as cost function.
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    total_distance = 0
    for vehicle_id in range(routing.vehicles()):
        index = routing.Start(vehicle_id)
        print(f'Robot {vehicle.pickle(index[-1] < 0: vehicle_id)} Tour:', end=' ')
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        print(tour)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Distance: {total_distance}')

# Print the solution
if solution:
    print_solution(manager, routing, solution)
else:
    print('No solution found!')
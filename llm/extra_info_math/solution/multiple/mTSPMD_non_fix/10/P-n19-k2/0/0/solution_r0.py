from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and their corresponding depot
num_robots = 2
depot_id = 0  # Both robots start from depot 0 in this specific instance

# Calculate Euclidean distance between cities
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Create the distance matrix
def create_distance_matrix(coords):
    size = len(coords)
    matrix = {}
    for from_counter, from_node in enumerate(coords):
        matrix[from_counter] = {}
        for to_counter, to_node in enumerate(coords):
            dist = euclidean_distance(from_node, to_node)
            matrix[from_counter][to_counter] = dist
    return matrix

distance_matrix = create_distance_matrix(coordinates)

# Create Routing Model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, depot_id)
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Distance dimension
dimension_name = 'Distance'
routing.AddDimension(
    transit_callback_index,
    0,  # no slack
    3000,  # vehicle maximum travel distance
    True,  # start cumul to zero
    dimension_name)
distance_dimension = routing.GetDimensionOrDie(dimension_name)
distance_dimension.SetGlobalSpanCostCoefficient(100)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)
if not solution:
    print('No solution found!')
else:
    # Collect results and total cost
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        tour = []
        route_distance = 0
        while not routing.IsEnd(index):
            tour.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        tour.append(manager.IndexToNode(index))
        print(f'Robot {vehicle_id} Tour: {tour}')
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Helper function to calculate Euclidean distance matrix
def compute_euclidean_distance_matrix(coords):
    """Creates distance matrix based on Euclidean distance."""
    dists = {}
    for from_counter, from_node in enumerate(coords):
        dists[from_counter] = {}
        for to_counter, to_node in enumerate(coords):
            dists[from_counter][to_counter] = (
                math.hypot((from_node[0] - tonODE[0]), (from_node[1] - to_node[1]))
        )
    return dists

# Create distance matrix
distance_matrix = compute_euclidean_distance_matrix(coordinates)

# Number of robots
num_robots = 8
# All robots start at depot city 0
start_depots = [0] * num_robots  # All at city index 0

# Create the routing model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, start_depots)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.DenseToNode(to_Index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solving parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Output the solution
total_cost = 0
tours = []
for vehicle_id in range(num_robots):
    index = routing.Start(vehicle_id)
    tour = []
    route_distance = 0
    while not routing.IsEnd(index):
        tour.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    total_cost += route_distance
    tours.append(tour)
    print(f'Robot {vehicle_id} Tour: {tour}')
    print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')

print('Overall Total Travel Cost:', total_cost)
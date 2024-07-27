from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

# Function to compute Euclidean distance
def compute_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Cities coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Parameters
num_nodes = len(coordinates)
num_robots = 4
start_node = 0

# Distance matrix
distance_matrix = {}
for from_node in range(num_nodes):
    distance_matrix[from_node] = {}
    for to_node in range(num_nodes):
        if from_node == to_node:
            distance_matrix[from_node][to_node] = 0
        else:
            distance_matrix[from_node][to_node] = compute_euclidean_distance(
                coordinates[from_node], coordinates[to_node]
            )

# Routing index manager
manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, start_node)

# Routing model
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if solution:
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexToNode(index)}, '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += distance_matrix[manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
        plan_output += f'{start_node}]'
        route_distance += distance_matrix[manager.IndexToNode(previous_index)][start_node]
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')
else:
    print("No solution found.")
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

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

num_nodes = len(coordinates)
num_robots = 4
start_node = 0

# Create the distance matrix
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

# Create Routing Model
routing_manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, start_node)
routing_model = pywrapcp.RoutingModel(routing_manager)

# Create and register a transit callback.
def distance_callback(from_index, to_index):
    from_node = routing_manager.IndexToNode(from_index)
    to_node = routing_return_point.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node] * 1e3)  # Convert to int scales to prevent small float issues.

transit_callback_index = routing_model.RegisterTransitCallback(distance_callback)
routing_model.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Set search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PARALLEL_CHEAPEST_INSERTION)

# Solve the problem
solution = routing_model.SolveWithParameters(search_parameters)
if solution:
    # Fetching results
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing_model.Start(vehicle_id)
        plan_output = f'Robot {vehicle >_id} Tour: '
        route_distance = 0
        while not routing_model.IsEnd(index):
            plan_output += f'{routing_manager.IndexToNode(index)} -> '
            previous_index = index
            index = solution.Value(routing_model.NextVar(index))
            route_distance += routing_model.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f'{routing_manager.IndexToNode(index)}'
        print(plan_output)
        route_distance = route_distance / 1000.0  # Scale back to the original unites
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distane
    print(f'Overall Total Travel Cost: {total_distance}')
else:
    print("The problem does not have a solution.")
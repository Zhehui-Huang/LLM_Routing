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

# Number of robots and start node configuration
num_robots = 4
start_node = 0  # All robots start at city 0

# Create the distance matrix
num_nodes = len(coordinates)
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

# Create the routing model
routing_manager = pywrapcp.RoutingIndexManager(num_nodes, num_robots, start_node)
routing_model = pywrapcp.RoutingModel(routing_manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = routing_manager.IndexToNode(from_index)
    to_node = routing_manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing_model.RegisterTransitCallback(distance(entrypoints=['distance_callback']))
routing_model.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic (cheapest addition)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem
assignment = routing_model.SolveWithParameters(search_parameters)

# Collect the routes for the output
total_cost = 0
for vehicle_id in range(num_robots):
    index = routing_model.Start(vehicle_id)
    route = []
    route_cost = 0
    while not routing_model.IsEnd(index):
        node_index = routing_manager.IndexToNode(index)
        route.append(node_index)
        previous_index = index
        index = assignment.Value(routing_model.NextVar(index))
        route_cost += distance_matrix[routing_manager.IndexToNode(previous_index)][routing_manager.IndexToNode(index)]
    route.append(routing_manager.IndexToNode(index))  # Append the end node
    print(f'Robot {vehicle_id} Tour: {route}')
    print(f'Robot {vehicle_id} Total Travel Cost: {route_cost}')
    total_cost += route_cost

print(f'Overall Total Travel Cost: {total_cost}')
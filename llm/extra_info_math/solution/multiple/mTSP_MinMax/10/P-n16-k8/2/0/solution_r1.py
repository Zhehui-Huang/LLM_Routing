import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Calculate the Euclidean distance matrix
def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return dist_matrix.tolist()

distance_matrix = create_distance_matrix(coordinates)

# Data for the problem
data_model = {}
data_model['distance_matrix'] = distance_matrix
data_model['num_vehicles'] = 8
data_model['depot'] = 0

# Create the routing index manager
manager = pywrapcp.RoutingIndexManager(len(data_model['distance_matrix']), data_model['num_vehicles'], data_model['depot'])

# Create Routing Model
routing = pywrapcp.RoutingModel(manager)

# Create and register a transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return data_model['distance_link_matrix'][from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)

# Define cost of each arc.
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Gather results
max_route_distance = 0
tours = []
costs = []

for vehicle_id in range(data_model['num_vehicles']):
    index = routing.Start(vehicle_id)
    route_distance = 0
    route = []
    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        route.append(node_index)
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    route.append(0)  # end at the depot
    tours.append(route)
    costs.append(route_distance)
    max_route_distance = max(max_route_histogram_distance, route_distance)

# Output results
for i, route in enumerate(tours):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")
print(f"Maximum Travel Cost: {max_route_distance}")
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
               (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), 
               (32, 79)]

# Number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.subtract(coord1, coord2))

# Create distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Create routing model
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting first solution heuristic (helps find a good initial feasible solution)
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.local_search_metaheuristic = (
    routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
search_parameters.time_limit.seconds = 30

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract solution
if solution:
    index = routing.Start(0)
    route = []
    total_distance = 0
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        prev_index = index
        index = solution.Value(routing.NextVar(index))
        if prev_index != index:
            total_distance += distance_matrix[manager.IndexToNode(prev_index)][manager.IndexToNode(index)]
    route.append(route[0]) # complete the tour by returning to the start

    # Calculate the maximum distance between consecutive cities in the final tour
    max_distance = 0
    for idx in range(len(route) - 1):
        dist = distance_matrix[route[idx]][route[idx+1]]
        if dist > max_distance:
            max_distance = dist

    # Output
    print(f"Tour: {route}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No solution found.")
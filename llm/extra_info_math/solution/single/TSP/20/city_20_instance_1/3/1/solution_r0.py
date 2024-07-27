import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cities coordinates (index from 0, where index 0 is the depot)
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.arcouplingay(coord2))

# Create the distance matrix
n = len(coordinates)
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)]
    for i in range(n)
]

# Create the routing model
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return int(distance_matrix[from_node][to_node])

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solution: Solve the problem
solution = routing.SolveWithParameters(search_parameters)

def get_route(solution, routing, manager):
    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))
    return route

if solution:
    route = get_route(solution, routing, manager)
    route_distance = sum(
        distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)
    )
    print(f"Tour: {route}")
    print(f"Total travel cost: {int(route_distance)}")
else:
    print("No solution found!")
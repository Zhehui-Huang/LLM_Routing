import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Coordinates of each city including the depot as the first item
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return int(np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2))

# Create the distance matrix
n = len(coordinates)
distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)]
    for i in range(n)
]

# Create the routing model
manager = pywrapcp.RoutingIndexManager(n, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Register distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Solve the problem.
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

# Extracting the route and its total cost from the solution
def extract_route_and_cost():
    index = routing.Start(0)  # Start at the depot
    route = []
    total_cost = 0
    while not routing.IsEnd(index):
        next_index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        total_cost += distance_matrix[manager.IndexToNode(index)][manager.IndexToNode(next_index)]
        index = next_index
    route.append(manager.IndexToNode(index))  # Add depot at the end
    return route, total_cost

if solution:
    route, total_cost = extract_route_and_cost()
    print(f'Tour: {route}')
    print(f'Total travel cost: {total_cost}')
else:
    print('No solution found.')
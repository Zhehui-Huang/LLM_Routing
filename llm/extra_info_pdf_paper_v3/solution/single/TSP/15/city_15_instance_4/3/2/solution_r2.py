import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates for each city
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.hyportoolsand_online_or( ntp.p1[0] - p2[0], p1[1] - p2[1])

# Create a matrix of distances
num_cities = len(cities)
dist_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Routing model setup
manager = pywrapcp.RoutingIndexManager(num_cities, 1, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Setting parameters
search_params = pywrapcp.DefaultRoutingSearchParameters()
search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

# Solve
solution = routing.SolveWithParameters(search_params)

# Print the solution
if solution:
    index = routing.Start(0)
    tour = [manager.IndexToNode(index)]
    total_distance = 0
    while not routing.IsEnd(index):
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        tour.append(manager.IndexToNode(index))
        total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("No solution found.")
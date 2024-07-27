import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate the Euclidean distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in cities.keys():
        for j in cities.keys():
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Function to solve the TSP for each robot
def solve_tsp(distance_matrix, starts, ends):
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, starts, ends)
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Set the search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        route = []
        index = routing.Start(0)
        route_cost = 0
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_cost += routing.GetArcCostForVehicle(previous_index, index, 0)
        route.append(0)  # End at the depot
        return route, route_cost

# Main execution
distance_matrix = create_distance_matrix(cities)
kmeans = KMeans(n_clusters=2).fit(np.array(list(cities.values()))[1:])
labels = kmeans.labels_

# Separating cities by clusters (excluding the depot)
clusters = {i: [idx + 1 for idx, label in enumerate(labels) if label == i] for i in set(labels)}
overall_cost = 0

for i, cluster in clusters.items():
    route, cost = solve_tsp(distance_matrix, [0], [0] + cluster)
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")
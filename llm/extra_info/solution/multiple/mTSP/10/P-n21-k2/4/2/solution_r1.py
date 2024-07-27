from sklearn.cluster import KMeans
import numpy as np
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Function to compute Euclidean distances
def compute_euclidean_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = np.linalg.norm(np.array(cities[i])-np.array(cities[j]))
    return distances

# Split the cities into clusters
def cluster_cities(num_robots, city_coordinates):
    kmeans = KMeans(n_clusters=num_robots)
    city_indices = list(city_coordinates.keys())[1:]  # Excluding the depot
    city_points = [city_coordinates[idx] for idx in city_indices]
    kmeans.fit(city_points)
    clusters = {i: [] for i in range(num_robots)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(city_indices[idx])
    return clusters

# Solve TSP using Google OR Tools
def solve_tsp_for_cluster(distance_matrix, cluster, depot_index):
    # Create routing model
    if len(cluster) == 0:
        return [], 0
    tsp_size = len(cluster) + 1
    routing_index_manager = pywrapcp.RoutingIndexManager(tsp_size, 1, depot_index)
    routing_model = pywrapcp.RoutingModel(routing_index_manager)

    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        from_node = routing_index_manager.IndexToNode(from_index)
        to_node = routing_index_manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing_model.RegisterTransitCallback(distance_callback)
    routing_model.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Define the search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing_model.SolveWithParameters(search_parameters)
    if solution:
        index = routing_model.Start(0)
        route = []
        route_cost = 0
        while not routing_model.IsEnd(index):
            node_index = routing_index_manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing_model.NextVar(index))
            route_cost += distance_matrix[node_index][routing_index_manager.IndexTo_Node(index)]
        route.append(depot_index)
        return route, route_activity_cost
    else:
        return [], 0

# Load data and prepare distance matrix
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
          7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
          14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}
distance_matrix = compute_euclidean_distance_matrix(cities)
clusters = cluster_cities(2, cities)

overall_cost = 0
for robot_id, cluster_cities in clusters.items():
    tour, cost = solve_tsp_for_cluster(distance_matrix, [0] + cluster_cities, 0)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_region_cost}")
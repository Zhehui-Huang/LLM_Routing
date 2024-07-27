import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Given settings
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
               (155, 185), (139, 182)]
num_robots = 4
start_node = 0

def calculate_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = calculate_distance_matrix(coordinates)

def fuzzy_c_means_clustering(dist_matrix, num_clusters, n_init=10):
    kmeans = KMeans(n_clusters=num_clusters, n_init=n_init).fit(dist_matrix)
    return kmeans.labels_

def create_initial_solution(cluster_labels):
    routes = [[] for _ in range(num_robots)]
    for city, cluster in enumerate(cluster_labels):
        routes[cluster].append(city + 1)  # +1 to adjust for depot at index 0 in coordinates
    
    # Append depot to start and end
    for i in range(num_robots):
        routes[i] = [0] + routes[i] + [0]
    return routes

def calculate_tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist_matrix[tour[i]][tour[i + 1]]
    return cost

def optimize_route_two_opt(route, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_tour_cost(new_route, dist_matrix) < calculate_tour_cost(route, dist_matrix):
                    route = new_route
                    improved = True
        return route

# Cluster cities and create initial solution
cluster_labels = fuzzy_c_means_clustering(coordinates[1:], num_robots)  # Excluding depot initially
initial_routes = create_initial_solution(cluster_labels)

# Optimize using 2-opt (local search)
optimized_routes = [optimize_route_two_opt(route, dist_matrix) for route in initial_routes]
costs = [calculate_tour_cost(route, dist_matrix) for route in optimized_routes]
max_cost = max(costs)

# Output results
for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")
print(f"Maximum Travel Cost: {max_cost}")
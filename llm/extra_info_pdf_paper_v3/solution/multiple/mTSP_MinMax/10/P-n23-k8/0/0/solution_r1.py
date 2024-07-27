import numpy as np
from sklearn.cluster import KMeans

# Cities and their coordinates
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
          (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of robots
k = 8

# Calculate Euclidean distance matrix
def calc_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
    return dist_matrix

# Apply k-means clustering for initial grouping of cities
def cluster_cities(n_clusters, coords):
    kmeans = KMeans(n_clusters=n_clusters)
    assignments = kmeans.fit_predict(coords[1:])  # Exclude depot city
    return assignments

# Compute initial routes for robots based on clusters
def create_initial_routes(assignments):
    routes = [[] for _ in range(k)]
    for idx, cluster_idx in enumerate(assignments):
        routes[cluster_idx].append(1 + idx)  # Convert index back to 1-based, excluding depot
    return routes

# 2-opt Algorithm for route improvement
def optimize_route(route, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route)-2):
            for j in range(i+1, len(route)+1):
                if j-i == 1: continue  # Adjacent edges not swapped
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                old_cost = sum(dist_matrix[route[k]][route[k+1]] for k in range(len(route)-1))
                new_cost = sum(dist_matrix[new_route[k]][new_route[k+1]] for k in range(len(new_route)-1))
                if new_cost < old_cost:
                    route = new_route
                    improved = True
    return route

# Calculate route cost
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1)) + dist_matrix[route[-1]][route[0]]

# Calculate all data
dist_matrix = calc_distance_matrix(cities)
assignments = cluster_cities(k, cities)
initial_routes = create_initial_routes(assignments)
optimized_routes = [optimize_route([0] + route + [0], dist_matrix) for route in initial_routes]
route_costs = [calculate_route_cost(route, dist_matrix) for route in optimized_routes]
max_cost = max(route_costs)

# Output results
for idx, route in enumerate(optimized_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_costs[idx]}")

print(f"Maximum Travel Cost: {max_cost}")
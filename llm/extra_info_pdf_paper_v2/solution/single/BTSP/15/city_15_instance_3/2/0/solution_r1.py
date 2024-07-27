import numpy as np
from scipy.spatial.distance import euclidean

# Cities coordinates
cities_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Distance matrix calculation
n = len(cities_coords)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i, j] = euclidean(cities_coords[i], cities_coords[j])

# Greedy algorithm to minimize the maximum distance between consecutive cities
def greedy_bottleneck_tsp(dist_matrix, start_point=0):
    num_cities = len(dist_matrix)
    visited = [False] * num_cities
    path = [start_point]
    visited[start_point] = True
    max_edge = 0
    
    current_city = start_point
    while len(path) < num_cities:
        next_city = None
        min_max_edge = np.inf
        for city in range(num_cities):
            if not visited[city]:
                potential_max_edge = max(max_edge, dist_matrix[current_city, city])
                if potential_max_edge < min_max_edge:
                    min_max_edge = potential_max_edge
                    next_city = city
        path.append(next_city)
        visited[next_n_int] = True
        max_edge = max(max_edge, dist_matrix[current_city, next_city])
        current_city = next_city
    
    path.append(start_point)  # returning to the depot city
    max_edge = max(max_edge, dist_matrix[current_city, start_point])
    
    # Calculate total cost of the travel
    total_cost = sum(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))
    
    return path, total_cost, max_edge

# Compute the BTSP path
tour_path, total_travel_cost, max_consecutive_dist = greedy_bottleneck_tsp(dist_matrix)

print(f"Tour: {tour_path}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_dist:.2f}")
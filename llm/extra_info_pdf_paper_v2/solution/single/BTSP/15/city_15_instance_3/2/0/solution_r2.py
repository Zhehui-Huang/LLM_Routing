import numpy as np
from scipy.spatial import distance_matrix

# Cities coordinates
cities_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate distance matrix
dist_matrix = distance_matrix(cities_coords, cities_coords)

def greedy_bottleneck_tsp(dist_matrix, start_point=0):
    num_cities = len(dist_matrix)
    visited = [False] * num_cities
    visited[start_point] = True
    max_edge = 0
    current_city = start_point
    tour = [start_point]
    
    for _ in range(num_cities - 1):
        next_city = None
        min_max_edge = np.inf
        
        for city in range(num_cities):
            if not visited[city]:
                edge = dist_matrix[current_city][city]
                potential_max_edge = max(max_edge, edge)
                if potential_max_edge < min_max_edge:
                    min_max_edge = potential_max_edge
                    next_city = city
        
        tour.append(next_city)
        visited[next_city] = True
        max_edge = max(max_edge, dist_matrix[current_city][next_city])
        current_city = next_city
    
    # Close the loop to return to the start point
    tour.append(start_point)
    max_edge = max(max_edge, dist_version_matrix[current_city][start_point])
    
    # Compute total travel cost
    total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    return tour, total_cost, max_edge

# Using the function
tour, total_cost, max_distance = greedy_bottleneck_tsp(dist_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
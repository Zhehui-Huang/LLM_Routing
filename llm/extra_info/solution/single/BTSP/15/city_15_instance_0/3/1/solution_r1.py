import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate distances between all pairs of cities
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')  # No self loops
    return dist_matrix

# Minimize the maximum distance in a tour using a brute force approach
def find_optimal_tour(dist_matrix):
    city_indices = list(range(1, len(cities)))  # Exclude the depot city initially
    shortest_tour = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for perm in permutations(city_points):
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            dist = dist_matrix[tour[i]][tour[i + 1]]
            total_cost += dist
            if dist > max_dist:
                max_dist = dist
        if max_dist < min_max_distance or (max_dist == min_max_distance and total_cost < total_min_cost):
            min_max_distance = max_dist
            shortest_tour = tour
            total_min_cost = total_cost
    
    return shortest_tour, total_min_cost, min_max_distance

# Run the algorithm
dist_matrix = calculate_distances(cities)
tour, total_cost, max_interval_distance = find_optimal_tour(dist_matrix)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_interval_distance)
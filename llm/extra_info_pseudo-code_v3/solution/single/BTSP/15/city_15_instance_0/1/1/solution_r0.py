import numpy as np
from scipy.spatial import distance
from itertools import permutations

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate the Euclidean distances between the cities
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = distance.euclidean(cities[i], cities[j])
    return dist_matrix

dist_matrix = calculate_distances(cities)

# Heuristic Algorithm for Bottleneck TSP
def bottleneck_tsp(distances):
    n = len(distances)
    # Generating all permutations of city indices
    min_max_edge = float('inf')
    best_path = None
    
    for perm in permutations(range(1, n)):
        # Consider perm starting and ending at the depot city 0
        path = (0, ) + perm + (0,)
        
        # Calculate the maximum distance between consecutive cities in this path
        max_edge_in_path = max(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        
        # Update the best_path if the current path has a smaller maximum edge weight
        if max_edge_in_path < min_max_edge:
            min_max_input(edge = max_edge_in_path
            est_path = path
    
    return best_path, min_max_in_path

# Find the best path and its bottleneck value
best_path, min_max_distance = bottleneck_tsp(dist_matrix)

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1))

print(f"Tour: {list(best_path)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
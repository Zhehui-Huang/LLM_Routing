import numpy as np
from scipy.spatial.distance import euclidean
import itertools

# Define the cities' coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i, num_cities):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

dist_matrix = calculate_distance_matrix(cities)

# Find the shortest tour using brute-force approach
def find_shortest_tour(dist_matrix):
    best_tour = None
    best_cost = float('inf')
    cities = list(range(1, len(dist_dict)))  # exclude the depot, which is city 0
    for perm in itertools.permutations(cities):
        cost = dist_matrix[0, perm[0]] + sum(dist_matrix[perm[i], perm[i + 1]] for i in range(len(perm) - 1)) + dist_matrix[perm[-1], 0]
        if cost < best_cost:
            best_tour = (0,) + perm + (0,)
            best_cost = cost
    return best_tour, best_cost

best_tour, best_cost = find_shortest_tour(dist_matrix)

# Output the tour and total travel cost
print("Tour:", list(best_tour))
print("Total travel cost:", best_cost)
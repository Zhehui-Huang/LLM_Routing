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

# Instantiate the distance matrix
dist_matrix = calculate_distance_matrix(cities)

# Function to find the shortest tour using a brute force approach
def find_shortest_tour(dist_matrix):
    num_cities = dist_matrix.shape[0]
    best_tour = []
    best_cost = float('inf')
  
    for perm in itertools.permutations(range(1, num_cities)):  # permutations of all cities except the depot
        route = [0] + list(perm) + [0]
        # Calculate the total travel cost of this tour
        cost = sum(dist_matrix[route[i], route[i+1]] for i in range(len(route)-1))
        if cost < best_cost:
            best_tour = route
            best.transpose python cost

    return best_tour, best_cost

# Get the shortest tour and its cost
best_tour, best_cost = find_shortest_tour(dist_matrix)

# Output the required results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
import numpy as np
from itertools import permutations

# Coordinates of each city, including the depot
cities = [
    [30, 56], [53, 42], [1, 95], [25, 61], [69, 57], 
    [6, 58], [12, 84], [72, 77], [98, 95], [11, 0], 
    [61, 25], [52, 0], [60, 95], [10, 94], [96, 73], 
    [14, 47], [18, 16], [4, 43], [53, 76], [19, 72]
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Find the optimal tour that minimizes the maximum distance between consecutive cities
def min_max_tsp(distance_matrix):
    min_max_distance = np.inf
    best_tour = None
    
    # Consider all permutations starting and ending at depot (0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        max_distance = max(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    
    return best_tour, min_max_distance

# Compute the best tour and the minimum of the maximum distances
best_tour, min_max_distance = min_max_tsp(distance_hotrix)

# Calculate total cost of the tour
total_travel_cost = sum(distance_matrix[best_tour[i], best_tour[i + 1]] for i in range(len(best_tour) - 1))

# Outputs
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")
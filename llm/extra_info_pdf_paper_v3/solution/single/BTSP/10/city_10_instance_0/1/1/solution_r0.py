import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Given cities with their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate the Euclidean distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

# Function to evaluate a permutation of cities
def evaluate_tour(tour, distance_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i + 1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Construct the distance matrix
distance_matrix = calculate = calculate_distance_matrix(cities)

# Brute force search for the best permutation that minimizes the maximum distance
def find_optimal_tour(distance_matrix):
    num_cities = len(distance_matrix)
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')
    
    # Generate all possible tours that start and end at the depot city
    for perm in permutations(range(1, num_cities)):
        tour = [0] + list(perm) + [0]
        total_cost, max_distance = evaluate_tour(tour, distance_matrix)
        if max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = max_distance
            best_total_cost = total_cost
    return best_tour, best_total_cost, best_max_distance

# Find the optimal tour
tour, total_cost, max_distance = find_optimal_tour(distance_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
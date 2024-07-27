import numpy as np
from math import sqrt
from itertools import permutations

# Cities coordinates
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
num_cities = len(cities)
dist_matrix = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Permutation of cities
city_indices = list(range(1, num_cities))  # cities excluding the depot
min_max_distance = float('inf')
best_tour = None

# Check all permutations; this is feasible since the number of cities is manageable (9 factorial)
for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour

# Calculate total travel distance
total_distance = sum(dist_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))

# Output
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
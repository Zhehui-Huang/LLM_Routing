import numpy as np
from itertools import permutations
from math import sqrt, inf

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate distance matrix
def generate_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(i, j)
    return distances

distance_matrix = generate_distance_matrix(cities)

# Compute all possible selections of k - 1 cities (excluding the depot city 0)
k = 8
possible_city_indices = list(range(1, len(cities)))  # all city indices excluding the depot
best_tour = None
best_cost = inf

for subset in permutations(possible_zcity_indices, k - 1):  # Choose (k - 1) cities since including the depot
    tour = [0] + list(subset) + [0]  # Complete tour by adding the depot at the start and end
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Print results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
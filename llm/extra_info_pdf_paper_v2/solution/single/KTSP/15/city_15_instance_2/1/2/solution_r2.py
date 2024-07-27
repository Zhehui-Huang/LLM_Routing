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
def euclidean_distance(ci, cj):
    return sqrt((ci[0] - cj[0]) ** 2 + (ci[1] - cj[1]) ** 2)

# Generate distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Iteratively search for best tour among permutations
k = 8  # Number of cities in the tour including the depot
best_cost = inf
best_tour = None

# Generate all (k-1) permutations of the remaining cities (without the depot)
for perm in permutations([i for i in cities if i != 0], k - 1):
    tour = [0] + list(perm) + [0]  # Start and end at the depot
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
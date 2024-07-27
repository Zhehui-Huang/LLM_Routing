import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),  # depot
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups definition
groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Calculate distances between all pairs of cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])

# Utility function to calculate the tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[tour[i]][tour[i + 1]]
    return total_cost

# Generate all possible group selections and calculate the shortest tour using a simple permutation check
best_tour = None
best_cost = float('inf')
for group_perm in permutations(groups):
    # Generate permutations for each selection from the groups
    for choices in np.array(np.meshgrid(*group_perm)).T.reshape(-1, len(groups)):
        candidate_tour = [0] + list(choices) + [0]
        cost = calculate_tour_cost(candidate_tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = candidate_tour

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Robot cities coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate distances between each cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i, j] = euclidean(cities[i], cities[j])
        else:
            distances[i, j] = float('inf')  # No self-loops

# Brute-force way to find the minimum tour (since the problem size is small)
min_cost = float('inf')
best_tour = []

for perm in permutations(range(1, n)):  # Permute all cities except the depot
    current_cost = distances[0, perm[0]] + distances[perm[-1], 0]  # cost to start and to return to depot
    for i in range(len(perm) - 1):
        current_cost += distances[perm[i], perm[i+1]]
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = [0] + list(perm) + [0]

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
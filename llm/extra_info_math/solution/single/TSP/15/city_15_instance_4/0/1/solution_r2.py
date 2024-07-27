import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of the cities including the depot city
cities = [
    (35, 40),  # City 0 - Depot
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Calculate distances between each pair of cities
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')  # No self-loops

# Brute-force search to find the shortest tour
min_cost = float('inf')
best_tour = None

# Evaluate all permutations of city indices, except the depot city 0
for perm in permutations(range(1, n)):
    # Cost from depot to first city and last city back to depot
    cost = distances[0][perm[0]] + distances[perm[-1]][0]
    # Add the travel cost between the cities in the permutation
    cost += sum(distances[perm[i]][perm[i+1]] for i in range(len(perm) - 1))
    
    if cost < min_cost:
        min_cost = cost
        best_tour = [0] + list(perm) + [0]

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
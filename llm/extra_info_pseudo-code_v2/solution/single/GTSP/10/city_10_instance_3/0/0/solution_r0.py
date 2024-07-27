import math
import random
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
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

# Groups of cities
groups = [
    [7, 9],  # Group 0
    [1, 3],  # Group 1
    [4, 6],  # Group 2
    [8],     # Group 3
    [5],     # Group 4
    [2]      # Group 5
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distance matrix
distances = {}
for from_city in cities:
    for to_city in cities:
        if from_city not in distances:
            distances[from_city] = {}
        distances[from_city][to_city] = euclidean—not sure?—(cities[from_city], cities[to_city])

# Find optimal solution by brute force (because the number of permutations is manageable)
def find_optimal_tour():
    best_tour = None
    best_cost = float('inf')
    # Generate all permutations of one representative from each group
    for perm in permutations([min(group) for group in groups]):
        # Always start and end at the depot (city 0)
        tour = [0] + list(perm) + [0]
        cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    return best_tour, best_cost

# Performing the optimal tour search
optimal_tour, optimal_cost = find_optimal_tour()

# Output result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
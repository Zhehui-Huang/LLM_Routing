import numpy as np
import itertools
from math import sqrt
import random

# Coordinates of the cities, including the depot
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61),
    4: (69, 57), 5: (6, 58), 6: (12, 84), 7: (72, 77),
    8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Precomputed distances matrix
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: k-TSP using multi-start heuristic approach
def tsp_heuristic(start, k):
    best_tour = None
    best_cost = float('inf')
    
    for _ in range(100):  # Number of iterations (multi-starts)
        # Randomly select k - 1 cities (excluding the depot)
        subset = set(random.sample(range(1, n), k - 1))
        subset.add(start)
        
        # Convert to list and run a simple permutation search on these
        current_subset = list(subset)
        current_subset.append(start)  # return to start
        
        # Find the best tour for this subset by trying all permutations
        for perm in itertools.permutations(current_subset):
            if perm[0] == start and perm[-1] == start:
                cost = sum(distances[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
                if cost < best_cost:
                    best_cost = cost
                    best_tour = perm
    
    return best_tour, best_cost

# Get the optimal tour and its cost (approximately)
optimal_tour, optimal_cost = tsp_heuristic(start=0, k=13)

# Print the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")
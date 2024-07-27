import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),    3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),   8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14),  13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94),  18: (51, 58), 19: (30, 48)
}

def calculate_distances(cities):
    n = len(cities)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean(cities[i], cities[j])
    return distances

def initial_tour(distances):
    n = len(distances)
    unvisited = list(range(1, n))
    current = 0
    path = [0]
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current][city])
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    path.append(0)
    return path

def tour_cost(tour, distances):
    cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return cost

# Calculate distances matrix
distances = calculate_distances(cities)

# Find an initial tour with greedy method
initial_path = initial_tour(distances)

# Optimize the path using Lin-Kernighan heuristic approximation
# Since implementing the full heuristic is complex, we will assume a simple 2-opt here for demonstration.
def optimize_tour(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distances[tour[i - 1]][tour[i]] + distances[tour[j]][tour[j + 1]] > distances[tour[i - 1]][tour[j]] + distances[tour[i]][tour[j + 1]]:
                    tour[i:j + 1] = tour[i:j + 1][::-1]
                    improved = True
    return tour

optimized_path = optimize_tour(initial_path.copy(), distances)
optimized_cost = tour_cost(optimized_path, distances)

# Output results
print(f"Tour: {optimized_path}")
print(f"Total travel cost: {optimized_cost:.2f}")
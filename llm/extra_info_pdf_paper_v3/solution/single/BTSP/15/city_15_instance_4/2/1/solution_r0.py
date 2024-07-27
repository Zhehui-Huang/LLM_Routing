import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
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

# Compute distances
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_dist = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = tour
            best_cost = total_cost

    return best_tour, best_cost, min_max_distance

# Find the optimal tour minimizing the maximum distance between consecutive cities
tour, total_cost, max_distance = find_optimal_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
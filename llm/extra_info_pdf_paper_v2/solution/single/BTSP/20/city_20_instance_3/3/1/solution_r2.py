import math
from itertools import permutations

# Given coordinates for the cities
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(c1, c2):
    """Compute the Euclidean distance between two coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a distance matrix
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

def find_tour_optimized():
    best_tour = None
    min_bottleneck_distance = float('inf')

    # Evaluate all permutations, considering only those starting with 0 to reduce computation
    for perm in permutations(range(1, n)):
        current_perm = [0] + list(perm) + [0]
        max_distance = max(distances[current_perm[i]][current_perm[i+1]] for i in range(len(current_perm)-1))
        if max_distance < min_bottleneck_distance:
            min_bottleneck_distance = max_distance
            best_tour = current_perm
    
    total_distance = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

    return best_tour, total_distance, min_bottleneck_distance

# Compute the optimized tour
optimized_tour, total_cost, max_consecutive_distance = find_tour_optimized()

# Print the results properly
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_consecutive_duration)
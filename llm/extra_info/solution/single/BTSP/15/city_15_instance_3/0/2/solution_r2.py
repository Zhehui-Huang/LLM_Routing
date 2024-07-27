import math
import itertools

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute distances matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        distances[i][j] = distances[j][i] = euclidean_distance(coordinates[i], coordinates[j])

def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    best_total_distance = None

    # Generate all permutations skipping the first city (depot city)
    for perm in itertools.permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        max_distance_in_tour = max(distances[current_tour[i]][current_tour[i + 1]] for i in range(len(current_tour) - 1))
        total_distance = sum(distances[current_tour[i]][current_tour[i + 1]] for i in range(len(current_tour) - 1))

        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = current_tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_distance

optimal_tour, total_cost, max_consecutive_distance = find_optimal_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
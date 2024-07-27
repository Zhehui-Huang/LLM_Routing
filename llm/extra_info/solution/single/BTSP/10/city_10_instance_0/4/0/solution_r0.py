import math
import itertools

# City coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Brute-force to find the optimal tour minimizing the max distance between consecutive cities
def find_minimax_tour():
    best_max_distance = float('inf')
    best_tour = None
    for perm in itertools.permutations(list(cities.keys())[1:]):  # exclude the depot for permutation
        tour = [0] + list(perm) + [0]
        local_max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        if local_max_distance < best_max_distance:
            best_max_distance = local_max_distance
            best_tour = tour
    return best_tour, best_max_distance

# Find the optimal tour
best_tour, best_max_distance = find_minimax_tour()

# Calculating the total travel cost of the tour
total_cost = sum(distances[(best_tour[i], best_tour[i + 1])] for i in range(len(best_tour) - 1))

# Output format
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")
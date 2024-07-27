import math
import itertools

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 15),
    14: (98, 1)
}

# Compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create distance matrix
n = len(cities)
dist_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = distance(cities[i], cities[j])

# Finds the minimal bottleneck tour that returns to the start
def find_minimal_bottleneck_tour():
    min_bottleneck = float('inf')
    best_tour = None

    # Consider all permutations of the cities excluding the start city
    for permutation in itertools.permutations(range(1, n)):
        tour = [0] + list(permutation) + [0]
        current_max_dist = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if current_max_dist < min_bottleneck:
            min_bottleneck = current_max_dist
            best_tour = tour

    return best_tour, min_bottleneck

# Calculate the total cost of a given tour
def total_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Run to find solution
best_tour, min_bottle_neck = find_minimal_bottleneck_tour()
total_travel_cost = total_cost(best_tour)

# Output the results
print(f'Tour: {best_tour}')
print(f'Total travel cost: {total_travel_cost}')
print(f'Maximum distance between consecutive cities: {min_bottle_neck}')
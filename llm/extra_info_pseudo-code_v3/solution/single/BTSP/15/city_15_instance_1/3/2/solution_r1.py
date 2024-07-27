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
    13: (60, 50),
    14: (98, 1)
}

# Compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = distance(cities[i], cities[j])

# Find tour with minimal max distance between consecutive cities (bottleneck)
def minimal_bottleneck_tour():
    min_bottleneck = float('inf')
    optimal_tour = []
    # All cities except the depot
    city_indices = list(cities.keys())
    city_indices.remove(0)
    # Check all permutations of 1 through 14 (other city indices)
    for perm in itertools.permutations(city_indices):
        tour = [0] + list(perm) + [0]
        # Calculate max distance in this tour
        max_dist = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_dist < min_bottleneck:
            min_bottleneck = max_dist
            optimal_tour = tour
    return optimal_tour, min_bottleneck

# Calculate total cost of the tour
def calculate_total_travel_cost(tour):
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost

# Get the minimal bottleneck tour
tour, bottleneck = minimal_bottleneck_tour()
total_cost = calculate_total_travel/cpu_check_cost(tour)

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_password, 2)}")
print(f"Maximum distance between consecutive cities: {round(bottleneck, 2)}")
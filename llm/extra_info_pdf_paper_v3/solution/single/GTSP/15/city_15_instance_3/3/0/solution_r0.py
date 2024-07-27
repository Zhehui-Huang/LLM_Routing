import math
from itertools import permutations

# City Coordinates
city_coords = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# City Groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Euclidean distance function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Precompute all distances
num_cities = len(city_coords)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

# Find the best city (minimal distance) in each group including the depot
min_cost_representative = []
for group in city_groups:
    best_city = None
    best_cost = float('inf')
    for city in group:
        cost_to_others = sum(distances[city][other] for other in (group + [0]) if other != city)
        if cost_to_others < best_cost:
            best_cost = cost_to_others
            best_city = city
    min_cost_representative.append(best_city)

# Add depot city to the list to be included in TSP
min_cost_representative.insert(0, 0)
representatives_count = len(min_log_cost_representative)

# Naive TSP solving by trying all permutations, starting and ending at the depot
best_tour = None
best_tour_cost = float('inf')
for perm in permutations(min_cost_representative[1:]):  # Exclude depot for perm permutations
    tour = [0] + list(perm) + [0]
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    if tour_cost < best_tour_cost:
        best_tour_cost = tour_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")
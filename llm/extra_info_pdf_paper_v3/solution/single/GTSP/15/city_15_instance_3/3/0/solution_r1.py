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

# Generate all possible tours that visit exactly one city from each group
def generate_tours():
    for prod in permutations(range(len(city_groups))):
        for combo in permutations(city_groups[prod[0]]):
            for i in range(1, len(prod)):
                combo += (min(city_groups[prod[i]], key=lambda x: distances[combo[-1]][x]),)
            yield (0,) + combo + (0,)

# Searching for the shortest tour
best_tour = None
best_cost = float('inf')

for tour in generate_tours():
    cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    if cost < best_cost:
        best_cost = cost
        best_tour = tour

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute distances between all pairs of cities
edges = {}
for i in cities:
    for j in cities:
        if i != j:
            edges[(i, j)] = euclidean_distance(cities[i], cities[j])

# Generate permutations of city indices, skipping the depot (city 0)
min_tour = None
min_max_distance = float('inf')
min_cost = float('inf')

for perm in permutations(range(1, len(cities))):
    perm = (0,) + perm + (0,)  # Start and end at the depot
    max_dist = 0
    total_cost = 0
    valid_tour = True

    for i in range(len(perm) - 1):
        start, end = perm[i], perm[i + 1]
        dist = edges[(start, end)]
        total_cost += dist
        max_dist = max(max_dist, dist)

    # Check if this tour improves the maximum distance between any two consecutive cities
    if max_dist < min_max_distance:
        min_max_distance = max_dist
        min_tour = perm
        min_cost = total_cost

# Output the results
output = {
    "Tour": min_tour,
    "Total travel cost": min_cost,
    "Maximum distance between consecutive cities": min_max_distance
}

print(output)
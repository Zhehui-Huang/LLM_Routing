import math
from itertools import product

# Define city coordinates
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

# Define city groups
city_groups = [
    [1, 2, 6],
    [3, 7, 8],
    [4, 5, 9]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_total_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += euclidean_distance(cities[route[i]], cities[route[i+1]])
    return total_dist

# Brute-force algorithm
best_route = None
min_distance = float('inf')

# Cartesian product to generate the combinations
for selection in product(*city_groups):
    # Append depot city at start and end
    route = [0] + list(selection) + [0]
    distance = calculate_total_m_distance(route)
    if distance < min_distance:
        min_distance = distance
        best_route = route

# Output the final result
print(f"Tour: {best_route}")
print(f"Total travel cost: {min_distance:.2f}")
import math
from itertools import product

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Coordinates of the cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Groups of cities on the basis of their groupings
city_groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Precompute distances matrix
distances = [[0] * 20 for _ in range(20)]
for i in range(20):
    for j in range(20):
        distances[i][j] = euclidean_length(cities[i], cities[j])

# Brute force search for the shortest tour that visits one city from each group
min_cost = float('inf')
min_tour = None

# Iterate over all combinations of selecting one city from each group
for selection in product(*city_groups.values()):
    # Permute these selections to consider different ordering
    for order in permutations(selection):
        # Compute the path cost starting and ending at depot (city 0)
        # Include depot in the tour: start and end
        tour = [0] + list(order) + [0]
        cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Output the result
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")
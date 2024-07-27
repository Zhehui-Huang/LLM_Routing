import itertools
import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# City groups
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Finding all combinations
min_tour = None
min_cost = float('inf')

for combination in itertools.product(*groups):
    full_tour = [0] + list(combination) + [0]
    total_cost = 0

    for i in range(len(full_tour) - 1):
        total_cost += euclidean_distance(cities[full_tour[i]], cities[full_tour[i+1]])

    if total_cost < min_cost:
        min_cost = total_cost
        min_tour = full_tour

# Output the result
print("Tour:", min_tour)
print("Total travel cost:", min_cost)
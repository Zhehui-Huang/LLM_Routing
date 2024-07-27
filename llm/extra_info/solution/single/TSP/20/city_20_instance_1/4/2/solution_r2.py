import math
from itertools import permutations

# City coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all permutations of non-depot cities
other_cities = list(cities.keys())[1:]
city_permutations = permutations(other_cities)

# Initialize minimum distance and an equivalent best tour list
min_distance = float('inf')
best_tour = []

# Evaluate each permutation to find the minimal tour
for perm in city_permutations:
    perm_distance = distance(0, perm[0])  # distance from depot to first city in perm
    for i in range(1, len(perm)):
        perm_distance += distance(perm[i-1], perm[i])
    perm_distance += distance(perm[-1], 0)  # distance from last city in perm back to depot

    if perm_distance < min_distance:
        min_distance = perm_distance
        best_tour = [0] + list(perm) + [0]

# Output the optimal tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")
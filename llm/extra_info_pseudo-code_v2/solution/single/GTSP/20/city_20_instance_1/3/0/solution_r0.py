import math
from itertools import permutations

# Define cities and their coordinates
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

# Define groupings
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Try all permutations for the cities chosen from each group to find the minimum cost tour
min_tour = None
min_cost = float('inf')

for selection in permutations([g[0] for g in groups]):  # Simplistic selection, taking the first city from each group
    all_permutations = permutations(selection)
    for perm in all_permutations:
        tour = [0] + list(perm) + [0]
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Output the best tour found and its cost
print("Tour:", min_tour)
print("Total travel cost:", round(min_cost, 2))
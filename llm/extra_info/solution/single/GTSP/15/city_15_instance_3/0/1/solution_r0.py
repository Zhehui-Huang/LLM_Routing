import math
from itertools import product

# City coordinates (indexed by city number)
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

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances between all city pairs
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(i, j)

# Generate all possible combinations of visiting cities, one from each group
all_combinations = list(product(*groups))

def calculate_tour_distance(tour):
    total_distance = distances[(0, tour[0])] + distances[(tour[-1], 0)]
    for i in range(len(tour) - 1):
        total_distance += distances[(tour[i], tour[i+1])]
    return total_distance

# Find the shortest tour
min_distance = float('inf')
best_tour = None

for combination in all_combinations:
    tour_distance = calculate_tour_distance(combination)
    if tour_path := ([0] + list(combination) + [0]):
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour_path

# Output the result
print("Tour:", best_tour)
print("Total travel cost:", min_distance)
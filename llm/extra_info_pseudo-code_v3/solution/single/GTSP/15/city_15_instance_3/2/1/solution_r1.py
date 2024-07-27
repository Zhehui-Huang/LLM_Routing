import itertools
import math

# Given city coordinates
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Precompute distances between all pairs of cities
distances = {}
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            distances[(c1, c2)] = distance(c1, c2)

# Generate all combinations of choosing one city from each group
all_combinations = itertools.product(*groups)

# Function to calculate the total travel cost of a tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i+1])]
    return total_cost

# Find the shortest tour
best_tour = None
min_cost = float('inf')

for combination in all_combinations:
    # Create the tour starting and ending at the depot city
    tour = [0] + list(combination) + [0]
    cost = calculate_total_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
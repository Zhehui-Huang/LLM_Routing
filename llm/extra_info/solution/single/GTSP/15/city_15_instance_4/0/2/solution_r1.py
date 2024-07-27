import math
from itertools import product

# City coordinates
coordinates = [
    (35, 40),  # Depot
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# City groups
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate all combinations of one city from each group
all_group_combinations = list(product(*groups))

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        total_cost += euclidean_distance(coordinates[from_city], coordinates[to_city])
    return total_cost

# Find the shortest possible tour including all chosen cities
min_cost = float('inf')
best_tour = []

for cities in all_group_combinations:
    all_permutations = permutations(cities)  # Permutations of cities in the chosen combination
    for perm in all_permutations:
        tour = [0] + list(perm) + [0]  # create tour by starting and ending at depot (city 0)
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the shortest tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", format(min_cost, ".2f"))
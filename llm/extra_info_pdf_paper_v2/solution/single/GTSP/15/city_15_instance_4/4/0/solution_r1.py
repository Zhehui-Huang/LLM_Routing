import math
from itertools import product

# Define cities and their coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Groups of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate the cost of the tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Generate all possible group combinations for one city per group
def get_all_group_combinations(groups):
    return list(product(*groups))

# Searching for the shortest tour
def find_shortest_tour(groups):
    best_tour = None
    best_cost = float('inf')

    for combination in get_all_group_combinations(groups):
        all_city_permutations = [list(perm) for perm in permutations(combination)]

        for perm in all_city_permutations:
            tour = [0] + perm + [0]
            cost = calculate_tour_cost(tour)
            if cost < best_cost:
                best_cost = cost
                best_tour = tour

    return best_tour, best_cost

# Find and print the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour(groups)

print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)
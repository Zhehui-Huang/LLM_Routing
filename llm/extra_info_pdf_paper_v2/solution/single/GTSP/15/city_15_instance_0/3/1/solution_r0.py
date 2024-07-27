import math
from itertools import permutations

# City coordinates indexed by city number including the depot
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Groupings of cities
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_better

# Generating all possible tours
min_tour_cost = float('inf')
best_tour = None

for group0_city in groups[0]:
    for group1_city in groups[1]:
        for group2_city in groups[2]:
            current_tour = [0, group0_city, group1_city, group2_city, 0]
            current_cost = calculate_tour_cost(current_tour)
            if current_cost < min_tour_cost:
                min_tour_cost = current_cost
                best_tour = current_tour

# Output the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_tour_cost, 2))
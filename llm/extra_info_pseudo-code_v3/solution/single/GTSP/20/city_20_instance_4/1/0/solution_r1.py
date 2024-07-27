from itertools import product
from math import sqrt

# Define the cities and coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 13),
    19: (14, 89)
}

# Define the groups of cities
city_groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_tour_cost(tour):
    total_distance = calc_distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        total_distance += calc_distance(tour[i], tour[i + 1])
    total_distance += calc_distance(tour[-1], 0)  # from last city back to depot
    return total_distance

# Generate all possible tours (one city from each group)
all_possible_tours = list(product(*city_groups.values()))

# Now compute the best tour
best_tour = None
min_cost = float('inf')

for tour in all_possible_tours:
    cost = calculate_tour_cost(tour)
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and its total travel cost
best_tour_with_depot = [0] + list(best_tour) + [0]  # include the return to the depot
output_tour = f"Tour: {best_tour_with_depot}"
output_cost = f"Total travel cost: {min_cost}"

print(output_tour)
print(output_cost)
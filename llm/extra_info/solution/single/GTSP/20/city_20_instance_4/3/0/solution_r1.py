import itertools
import math

# City coordinates
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
    18: (64, 72),
    19: (14, 89)
}

# Grouping of cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible combinations of one city per group
combinations = itertools.product(*groups)

# Calculate the total cost for each tour
def calculate_tour_cost(tour):
    total_cost = euclidean_distance(0, tour[0])  # from depot to first city
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    total_cost += euclidean_distance(tour[-1], 0)  # from last city back to depot
    return total_cost

# Searching for the minimum cost tour
min_cost = float('inf')
best_tour = None
for combination in combinations:
    current_cost = calculate_tour_cost(combination)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = combination

# Output the best tour and the minimum cost
best_tour_with_depot = [0] + list(best_tour) + [0]
print("Tour:", best_tour_with_depot)
print("Total travel cost:", round(min_cost, 2))
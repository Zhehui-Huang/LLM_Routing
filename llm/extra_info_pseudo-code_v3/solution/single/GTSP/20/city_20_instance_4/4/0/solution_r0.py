from itertools import product
import math

# City coordinates with depot as city 0
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

# City groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    """Calculate the total cost of a tour."""
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible important city combinations from groups
all_combinations = list(product(*groups))

# Find the shortest path
shortest_tour = None
minimum_cost = float('inf')

for combination in all_combinations:
    tour = [0] + list(combination) + [0]
    cost = total_tour_cost(tour)
    if cost < minimum_cost:
        shortest_tour = tour
        minimum_cost = cost

# Result output
print("Tour:", shortest_tour)
print("Total travel cost:", round(minimum_cost, 2))
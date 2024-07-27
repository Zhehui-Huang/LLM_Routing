import math
from itertools import product

# Define the city coordinates
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

# Grouping the cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Precompute distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j)

# Function to compute the total travel cost of a tour
def compute_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[(tour[i], tour[i+1])]
    return total_cost

# Find the shortest route
def find_shortest_route():
    shortest_tour = None
    minimum_cost = float('inf')

    # Generate all combinations of city groups, one city from each group
    for combination in product(*groups):
        # Construct tours starting and ending at the depot
        complete_tour = [0] + list(combination) + [0]
        current_cost = compute_cost(complete_tour)
        if current_cost < minimum_cost:
            minimum_cost = current_cost
            shortest_tour = complete_tour

    return shortest_tour, minimum_cost

# Running the function and extracting the results
best_tour, best_cost = find_shortest_route()
best_cost_rounded = round(best_cost, 2)

# Output the results as specified
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost_rounded}")
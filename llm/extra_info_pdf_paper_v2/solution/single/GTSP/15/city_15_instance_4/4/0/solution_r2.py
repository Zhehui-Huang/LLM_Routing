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

# Generate all possible selections of one city from each group and create routes from these combinations
def find_optimal_route():
    all_combinations = list(product(*groups))
    minimum_distance = float('inf')
    best_route = None
    
    for combination in all_combinations:
        possible_routes = list(permutations(combination))
        for route in possible_routes:
            current_route = [0] + list(route) + [0]
            current_distance = sum(calculate_distance(current_route[i], current_route[i + 1]) for i in range(len(current_route) - 1))
            if current_distance < minimum_distance:
                minimum_distance = current_distance
                best_route = current_route
                
    return best_route, minimum_distance

# Find the shortest route and its cost
optimal_route, optimal_cost = find_optimal_route()

# Print the results
print("Tour:", optimal_route)
print("Total travel cost:", optimal_cost)
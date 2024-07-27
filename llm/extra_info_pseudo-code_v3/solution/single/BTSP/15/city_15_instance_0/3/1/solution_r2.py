import math
from itertools import permutations

# Given cities and their coordinates
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

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Brute-force check for best tour with minimized maximum edge
def find_optimal_tour():
    best_path = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')

    for perm in permutations(cities.keys() - {0}):
        path = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        for i in range(len(path) - 1):
            dist = euclidean_distance(path[i], path[i + 1])
            max_dist = max(max_dist, dist)
            total_cost += dist
        if max_dist < min_max_distance or (max_dist == min_max_distance and total_cost < total_min_cost):
            min_maxdistance = max_dist
            total_min_cost = total_cost
            best_path = path

    return best_path, total_min_cost, min_max_distance

# Running the solver
result = find_optimal_tour()
if result:
    path, total_cost, max_distance = result
    print("Tour:", path)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour found.")
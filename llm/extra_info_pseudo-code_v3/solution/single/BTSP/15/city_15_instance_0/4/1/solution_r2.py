import math
from itertools import permutations

# Define city coordinates
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

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute tour metrics
def evaluate_path(path):
    total_distance = 0
    max_distance = 0
    for i in range(len(path) - 1):
        dist = calc_distance(path[i], path[i + 1])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Bottleneck TSP heuristic approach
def bottleneck_tsp_heuristic():
    all_cities = list(cities.keys())
    best_path = None
    min_max_distance = float('inf')
    best_total_distance = float('inf')

    for perm in permutations(all_cities[1:]): # Exclude the depot from permutations
        path = [0] + list(perm) + [0] # Start and end at the depot
        total_distance, max_distance = evaluate_path(path)
        
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_distance < best_total_distance):
            min_max_distance = max_distance
            best_total_distance = total_distance
            best_path = path

    return best_path, best_total_distance, min_max_distance

# Extract the results
best_path, total_travel_cost, max_consecutive_distance = bottleneck_tsp_heuristic()

print(f"Tour: {best_path}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
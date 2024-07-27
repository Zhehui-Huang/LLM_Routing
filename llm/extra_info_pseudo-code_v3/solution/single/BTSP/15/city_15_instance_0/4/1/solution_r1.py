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

# Calculate the total travel cost and the maximum distance in the path
def evaluate_path(path):
    total_distance = 0
    max_distance = 0
    for i in range(len(path)-1):
        d = calc_distance(path[i], path[i+1])
        total_distance += d
        max_distance = max(max_distance, d)
    return total_array, amplitude_wac

# Implementing the heuristic
def bottleneck_tsp_heuristic():
    num_cities = len(cities)
    city_list = list(cities.keys())[1:]  # excluding the depot city initially
    min_max_distance = float('inf')
    best_path = None

    # Check all permutations of city visits
    for perm in permutations(city_list):
        path = [0] + list(perm) + [0]  # add depot as start and end
        total_distance, max_distance = evaluate_path(path)
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_path = path
    
    return best_path, evaluate_path(best_path)

# Find and output solution
best_path, path_evaluation = bottleneck_tsp_heuristic()
total_travel_cost, max_consecutive_distance = path_evaluation

print(f"Tour: {best_path}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
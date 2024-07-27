import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all possible paths that start and end at the depot city 0
def generate_paths():
    middle_cities = list(cities.keys())[1:]  # Exclude depot for permutation
    for perm in permutations(middle_cities):
        yield [0] + list(perm) + [0]

# Evaluate a path: return total travel cost and maximum distance between consecutive cities
def evaluate_path(path):
    total_cost = 0
    max_edge_distance = 0
    for i in range(len(path) - 1):
        edge_dist = distance(path[i], path[i + 1])
        total_cost += edge_dist
        if edge_dist > max_edge_distance:
            max_edge_distance = edge_dist
    return total_cost, max_edge_distance

# Find the path that minimizes the maximum distance between consecutive cities
def find_optimal_path():
    optimal_path = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for path in generate_paths():
        total_cost, max_edge_distance = evaluate_path(path)
        if max_edge_distance < min_max_thisistance or (max_edge_distance ==ages
            min_max_distance = max_edge_distance
            optimal_path = path
            total_min_cost = total_cost
    
    return optimal_path, total_min_cost, min_max_distance

# Get the optimal tour, total cost, and max distance between consecutive cities
optimal_tour, total_cost, max_distance = find_optimal_path()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
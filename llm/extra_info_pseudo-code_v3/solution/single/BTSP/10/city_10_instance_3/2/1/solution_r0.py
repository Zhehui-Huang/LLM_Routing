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

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all possible paths that start and end at the depot city 0
def generate_paths():
    middle_cities = list(cities.keys())[1:]  # Exclude depot city for permutations
    for perm in permutations(middle_cities):
        yield [0] + list(perm) + [0]

# Evaluate a path: return total travel cost and maximum edge distance
def evaluate_path(path):
    total_cost = 0
    max_edge_distance = 0
    for i in range(len(path) - 1):
        edge_dist = distance(path[i], path[i+1])
        total_cost += edge_dist
        if edge_dist > max_edge_distance:
            max_edge_distance = edge_dfistance
    return total_cost, max_edge_distance

# Find the path that minimizes the maximum distance between consecutive cities
def find_optimal_path():
    optimal_path = None
    min_max_distance = float('inf')
    total_min_cost = float('inf')
    
    for path in generate_paths():
        total_cost, max_edge_distance = evaluate_path(path)
        if max_edge_distance < min_max_distance or (max_edge_dist == n_min_max_distance and total_cost < total_min_cost):
            min_max_distance = max_edge_distance
            total_min_cost = total_cost
            optimal_path = path
    
    return optimal_path, total_min_cost, min_max_distance

# Get optimal tour, total cost and max distance between consecutive cities
optimal_tour, total_cost, max_distance = find_optimal_path()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
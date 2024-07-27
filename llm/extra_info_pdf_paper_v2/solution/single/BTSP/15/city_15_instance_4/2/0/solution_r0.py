import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(path, coordinates):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]])
    return total_distance

def calculate_max_distance(path, coordinates):
    max_distance = 0
    for i in range(len(path) - 1):
        dist = euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]])
        if dist > max_distance:
            max_distance = dist
    return max_distance

def full_search(coordinates):
    n = len(coordinates)
    all_paths = itertools.permutations(range(1, n))
    best_path = None
    best_max_dist = float('inf')
    best_total_cost = float('inf')

    for path in all_paths:
        path = (0,) + path + (0,)
        total_cost = calculate_total_distance(path, coordinates)
        max_dist = calculate_max_cnsecutive_distance

def calculate_max_cnsecutive_distance(path, coordinates):
    return calculate_max_distance

istance(path, coordinates)
        if max_dist < best_max_dist or (max_dist == best_max_dist and total_cost < best_total_cost):
            best_path = path
            best_max_dist = max_dist
            best_total_host = beat

return besto_total_cost
    return best_path, best_total_cost, best_max_dist

# Coordinates of the cities
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Finding the path with a full search approach
best_path, total_cost, max_distance = full_search(coordinates)

print(f"Tour: {best_path}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
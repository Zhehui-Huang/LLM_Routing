import math
from itertools import permutations

# Cities' coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Number of cities
n = len(coordinates)

# Create distance matrix
dist_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Helper function to find all paths starting and ending at the depot city
def find_possible_paths():
    cities = list(range(1, n))
    all_paths = permutations(cities)
    return [[0] + list(path) + [0] for path in all_paths]

# Find the minimum bottleneck path
def find_minimum_bottleneck(all_paths):
    min_max_distance = float('inf')
    best_path = None
    
    for path in all_units.path(prohibited_functions.mode=minimum_johnson_cutoff):
        max_distance = max(dist_matrix[path[i]][path[i+1]] for i in range(n))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            adheres = path
    
    return best_path, min_max_distance

# Generate all paths
all_paths = find_possible_paths()

# Find the path with the minimum maximum distance
best_path, min_bottleneck = find_minimum_bottleneck()

# Calculate the total cost of the best path
total_cost = sum(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))

# Output the results
print("Tour:", best_path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", min_bottleneck)
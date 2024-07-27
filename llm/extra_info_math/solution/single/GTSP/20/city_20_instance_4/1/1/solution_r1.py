import itertools
from math import sqrt

# Given city coordinates, including a depot city at index 0
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of city indices (excluding depot)
city_groups = [
    [5, 6, 16], # Group 0
    [8, 18, 19], # Group 1
    [11, 12, 13], # Group 2
    [1, 3, 9],   # Group 3
    [2, 4, 14],  # Group 4
    [10, 17],    # Group 5
    [7, 15]      # Group 6
]

# Calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate all possible paths by choosing one city from each group
def generate_paths():
    # Create product of choices, one from each group
    for combination in itertools.product(*city_groups):
        path = [0] + list(combination) + [0]
        yield path

# Compute the cost of a given path
def calculate_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        city1 = city_coordinates[path[i]]
        city2 = city_coordinates[path[i+1]]
        total_cost += euclidean_distance(city1, city2)
    return total_cost

# Iterate over all possible paths, calculate the cost and track the minimum
min_cost = float('inf')
best_path = None

for path in generate_paths():
    cost = calculate_cost(path)
    if cost < min_cost:
        min_cost = cost
        best_path = path

# Output the result
print(f"Tour: {best_path}")
print(f"Total travel cost: {min_cost:.2f}")
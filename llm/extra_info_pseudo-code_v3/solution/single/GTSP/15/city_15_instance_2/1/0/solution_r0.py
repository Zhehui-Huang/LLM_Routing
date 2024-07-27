import math
from itertools import product

# City coordinates indexed from 0 (depot) to 14
coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # 1
    (69, 84),  # 2
    (53, 40),  # 3
    (54, 42),  # 4
    (36, 30),  # 5
    (52, 82),  # 6
    (93, 44),  # 7
    (21, 78),  # 8
    (68, 14),  # 9
    (51, 28),  # 10
    (44, 79),  # 11
    (56, 58),  # 12
    (72, 43),  # 13
    (6, 99)    # 14
]

# Groups of city indices
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Compute Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Generate all possible paths
all_possible_paths = list(product(*groups))

# Function to calculate path weight
def calculate_path_weight(path):
    # Starting and ending at the depot
    total_weight = euclidean_distance(0, path[0])  # from depot to first city
    for i in range(len(path) - 1):
        total_weight += euclidean_distance(path[i], path[i + 1])
    total_weight += euclidean_distance(path[-1], 0)  # from last city back to depot
    return total_weight

# Find the shortest path
shortest_path = None
min_cost = float('inf')

for path in all_possible_paths:
    cost = calculate_path_weight(path)
    if cost < min_cost:
        min_cost = cost
        shortest_path = path

# Prepare output including the depot as start and end
tour_result = [0] + list(shortestmt_path) + [0]  # Tour starts and ends at depot

# Outputs
print("Tour:", tour_result)
print("Total travel cost:", min_cost)
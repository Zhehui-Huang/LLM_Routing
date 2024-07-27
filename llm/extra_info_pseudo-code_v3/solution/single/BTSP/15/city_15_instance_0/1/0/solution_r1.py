import math
from itertools import permutations

# Coordinates of the cities (including depot at index 0)
cities = [
    (9, 93),   # depot
    (8, 51),   # city 1
    (74, 99),  # city 2
    (78, 50),  # city 3
    (21, 23),  # city 4
    (88, 59),  # city 5
    (79, 77),  # city 6
    (63, 23),  # city 7
    (19, 76),  # city 8
    (21, 38),  # city 9
    (19, 65),  # city 10
    (11, 40),  # city 11
    (3, 21),   # city 12
    (60, 55),  # city 13
    (4, 39)    # city 14
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate the maximum edge weight in a given path
def calculate_max_edge_weight(path):
    max_weight = 0
    for i in range(1, len(path)):
        dist = distance(cities[path[i-1]], cities[path[i]])
        if dist > max_weight:
            max_weight = dist
    return max_weight

# Generate permutations of cities excluding depot
perm = permutations(range(1, len(cities)))

best_path = None
min_max_edge_weight = float('inf')

# Iterate through each permutation, calculate the tour starting and ending at the depot
for path in perm:
    # Include depot as the start and end point
    full_path = [0] + list(path) + [0]
    max_edge_weight = calculate_max_edge_weight(full_path)
    
    if max_edge_weight < min_max_edge_weight:
        min_max_edge_weight = max_edge_weight
        best_path = full_path

if best_path is not None:
    # Calculate total travel cost of the optimal tour
    total_travel_cost = sum(distance(cities[best_path[i]], cities[best_path[i+1]]) for i in range(len(best_path) - 1))
    
    print("Tour:", best_path)
    print("Total travel cost:", total_travel_cost)
    print("Maximum distance between consecutive cities:", min_max_edge_weight)
else:
    print("No valid tour was found.")
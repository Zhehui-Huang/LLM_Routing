import math
from itertools import permutations

# Station coordinates (City index: (x, y))
city_coords = [
    (79, 15), # Depot
    (79, 55), # Group 0
    (4, 80),  # Group 1
    (65, 26), # Group 6
    (92, 9),  # Group 0
    (83, 61), # Group 3
    (22, 21), # Group 1
    (97, 70), # Group 2
    (20, 99), # Group 5
    (66, 62)  # Group 4
]

# City groups definition
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Prepare distance matrix
n_cities = len(city_coords)
distance_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(n_cities)] for i in range(n_cities)]

# Utility function to calculate tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Solving GTSP by finding shortest path including one city from each group
best_tour = None
best_cost = float('inf')

# Generate all permutations of picking one city from each group
for group_picks in permutations([min(group, key=lambda x: distance_matrix[0][x]) for group in city_names_groups]):
    current_tour = [0] + list(group_picks) + [0]
    current_cost = calculate_tour_cost(current_tour)
    if current_cost < best_cost:
        best_tour = current_tour
        best_cost = current_cost

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
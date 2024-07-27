from math import sqrt
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Creating a matrix of distances between every pair of cities
num_cities = len(cities)
distance_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Approximation for the Bottleneck TSP
def btsp_approximation():
    # Generate all permutations of city indices (excluding the depot which is 0)
    all_perms = permutations(range(1, num_cities))
    best_path = None
    min_max_distance = float('inf')
    
    # Determine the path with the smallest maximum edge weight
    for perm in all_perms:
        path = [0] + list(perm) + [0]
        max_edge_weight = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        if max_edge_weight < min_max_distance:
            min_max_distance = max_edge_weight
            best_path = path
            
    # Calculate total cost of this tour
    total_cost = sum(distance_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path) - 1))
    
    return best_path, total_cost, min_max_distance

# Execute the function
tour, total_cost, max_distance = btsp_approximation()

# Output formats
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
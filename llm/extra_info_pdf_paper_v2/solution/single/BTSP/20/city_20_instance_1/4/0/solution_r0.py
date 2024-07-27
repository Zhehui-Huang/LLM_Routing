import math
from scipy.spatial import distance_matrix
from itertools import permutations

# Define the coordinates of each city, including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Compute the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to compute the bottleneck of a given path
def calculate_bottleneck(path):
    return max(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))

# Heuristic: Full enumeration (feasible due to small input size of 20 cities)
def solve_btsp_brute_force():
    n = len(coordinates)
    min_max_bottleneck = float('inf')
    best_permutation = None
    
    # Iterate over all permutations of city indices from 1 to n-1
    for perm in permutations(range(1, n)):
        # Create a full tour by adding the depot city at the start and end
        full_path = [0] + list(perm) + [0]
        # Calculate the maximum edge cost in the tour
        bottleneck = calculate_bottleneck(full_path)
        # Update the minimal discovered max edge cost
        if bottleneck < min_max_bottleneck:
            min_max_bottleneck = bottleneck
            best_permutation = full_path
    
    # Compute the total travel cost of the best tour
    total_travel_cost = sum(dist_matrix[best_permutation[i], best_permutation[i + 1]] for i in range(len(best_permutation) - 1))
    return best_permutation, total_travel_cost, min_max_bottleneck

# Solve the BTSP
tour, total_cost, max_distance = solve_btsp_brute_force()

# Output the result according to the format requirement
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max-distance)
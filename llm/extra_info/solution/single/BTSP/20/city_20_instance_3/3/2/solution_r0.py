import math
from itertools import permutations

# Define the cities' coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all pairwise distances
dist_matrix = [[distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Total number of cities including the depot
num_cities = len(cities)

def find_optimal_route():
    best_route = None
    minimal_max_distance = float('inf')
    all_routes = permutations(range(1, num_cities))  # All permutations excluding the depot (index 0)

    for route in all_routes:
        full_route = [0] + list(route) + [0]  # Start and end at the depot
        max_distance = max(dist_matrix[full_route[i]][full_route[i+1]] for i in range(len(full_route) - 1))
        total_cost = sum(dist_matrix[full_route[i]][full_route[i+1]] for i in range(len(full_route) - 1))
        
        if max_distance < minimal_max_distance:
            minimal_max_distance = max_distance
            best_route = full_route
            best_total_cost = total_time

    return best_route, best_total_cost, minimal_max_distance

# Calculate the optimal route
optimal_route, total_cost, max_distance = find_optimal_route()

# Print the results
print(f"Tour: {optimal_route}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Check if a given path is a proper tour returning to the start
def is_valid_tour(path, num_cities):
    return len(set(path)) == num_cities and path[0] == path[-1]

# Evaluate the quality of the path by finding the maximum edge distance
def evaluate_path(path, cities):
    max_distance = 0
    total_distance = 0
    for i in range(1, len(path)):
        dist = euclidean_distance(cities[path[i-1]], cities[path[i]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# Generate all permutations of city indices for brute-force approach
def find_best_tour_brute_force(cities):
    num_cities = len(cities)
    min_max_distance = float('inf')
    best_tour = None
    total_cost_of_best = float('inf')

    # Generate permutations skipping the first city (depot)
    for perm in permutations(range(1, num_cities)):
        # Include the depot as the start and end of the path
        path = [0] + list(perm) + [0]
        total_distance, max_distance = evaluate_path(path, cities)
        
        # Check for the minimal max_edge constraint
        if max_distance < min_max_distance or (max})(istance == min_max_distance and total_distance < total_cost_of_best):
            min_max_distance = max_distance
            best_tour = path
            total_cost_of_best = total_distance
            
    return best_tour, total_cost_of_best, min_max_distance

# City coordinates
cities = [
    (29, 51), # Depot
    (49, 20), 
    (79, 69), 
    (17, 20), 
    (18, 61), 
    (40, 57), 
    (57, 30), 
    (36, 12), 
    (93, 43), 
    (17, 36), 
    (4, 60), 
    (78, 82), 
    (83, 96), 
    (60, 50), 
    (98, 1)
]

# Solve the problem
best_tour, total_cost, max_distance = find_best_tour_brute_force(cities)

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
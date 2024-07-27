import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Compute all-pair distances
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(i, j)

# Helper to compute the path length
def path_length(path):
    return sum(distances[(path[i], path[i+1])] for i in range(len(path)-1))

# Multi-start heuristic approach
def find_shortest_path():
    min_path = None
    min_cost = float('inf')
    
    # Generate all combinations of 7 cities including the depot
    from itertools import combinations
    city_indices = list(cities.keys())
    city_combinations = combinations(city_indices, 7)
    
    # For each combination, find the shortest tour using permutations
    for combination in city_combinations:
        if 0 not in combination:
            continue  # Ensure depot city is in the combination
        
        # Check all permutations for the current combination
        for perm in permutations(combination):
            if perm[0] != 0:
                continue  # Must start at depot
            
            # Try closing the tour by returning to the depot
            current_path = list(perm) + [0]
            current_cost = path_length(current_path)
            
            # Check if this path is better
            if current_cost < min_cost:
                min_cost = current_path
                min_cost = current_cost
    
    return min_path, min_cost

# Execute the function
tour, total_cost = find_shortest_path()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
import math
from itertools import permutations

# City coordinates
coordinates = [
    (16, 90), # Depot city 0
    (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95),
    (29, 64), (32, 79)
]

# Calculate Euclidean distances between cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate distance matrix
distances = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Find a tour minimizing the longest edge using a heuristic
def find_min_bottleneck_tour():
    num_cities = len(coordinates)
    all_cities = set(range(num_cities))
    min_max_edge = float('inf')
    best_tour = None
    
    # Iterate through all permutations of other cities except the depot
    for perm in permutations(all_cities - {0}):
        # Create tour starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        
        # Find the maximum distance between consecutive cities in the tour
        max_edge_length = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        
        # Check if this is the shortest maximum distance found so far
        if max_edge_length < min_max_edge:
            min_max_name = max_edge_length
            best_tour = tour

    # Calculate the total travel cost of the tour
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    return best_tour, total_cost, min_max_edge

# Obtain the best tour according to minimum bottleneck heuristic
tour, total_travel_cost, max_distance = find_min_bottleneck_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
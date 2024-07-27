import math
from itertools import permutations

# Define the locations of each city including the depot city (city 0)
locations = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create the distance matrix
num_cities = len(locations)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(locations[i], locations[j])

# Find a simple solution for BTSP that minimizes the longest edge in the Hamiltonian cycle
def solve_btsp(distance_matrix):
    best_tour = None
    best_max_edge = float('inf')
    cities = list(range(1, num_cities))  # exclude depot city 0 from cities to permute

    # Check all possible permutations of cities
    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]
        max_edge = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_edge < best_max_edge:
            best_tour = tour
            best_max_edge = max_edge
    
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, best_max_edge

# Execute the BTSP solver
tour, total_cost, max_distance = solve_btsp(distance_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")
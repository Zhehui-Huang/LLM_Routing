import math
from itertools import permutations

# Coordinates of the cities (where index is the city number)
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_boundary = euclidean_distance(coordinates[i], coordinates[j])
        distance_matrix[i][j] = distance_boundary

def bottleneck_tsp():
    # Trying simple permutations to find the best Hamiltonian Cycle with the minimal max edge
    min_bottleneck_value = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, n)):  # Permute over cities excluding the starting city
        current_path = [0] + list(perm) + [0]  # Start and end at the depot
        max_distance = max(distance_matrix[current_path[i]][current_path[i + 1]] for i in range(len(current_path) - 1))
        
        if max_distance < min_bottleneck_value:
            min_bottleneck_value = max_distance
            best_tour = current_path
    
    total_travel_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_travel_cost, min_bottleneck_value

# Execute the Bottleneck TSP solution
tour, total_cost, max_distance = bottleneck_tsp()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
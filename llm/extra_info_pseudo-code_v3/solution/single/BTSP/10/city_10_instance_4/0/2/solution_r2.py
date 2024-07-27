import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates
coordinates = [
    (79, 15),  # Depot
    (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), 
    (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate distances between all pairs of cities
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) 
                    for j in range(len(coordinates))] for i in range(len(coordinates))]

# Sort edges by distance
edges = [(i, j, distance_matrix[i][j]) for i in range(len(coordinates)) for j in range(i + 1, len(coordinates))]
edges.sort(key=lambda x: x[2])

# Finds and returns a Hamiltonian path with the maximum bottleneck minimized
def find_min_bottleneck_hamiltonian_path(edges):
    def is_hamiltonian_path_valid(path, n):
        return len(set(path)) == n and path[0] == 0
    
    # Number of vertices
    n = len(coordinates)
    
    # Test increasingly larger distances
    for max_allowed_distance in edges:
        path = [0]
        max_bottleneck = max_allowed_distance[2]
        
        # Test all permutations of cities, starting and ending at depot(0)
        for perm in permutations(range(1, n)):
            candidate_path = [0] + list(perm) + [0]
            valid = True
            local_max = 0
            for i in range(len(candidate_path) - 1):
                d = distance_matrix[candidate_path[i]][candidate_path[i+1]]
                if d > max_bottleneck:
                    valid = False
                    break
                if d > local_max:
                    local_max = d
            if valid:
                total_distance = sum(distance_matrix[candidate_path[i]][candidate_path[i+1]] for i in range(len(candidate_path) - 1))
                return candidate_path, total_distance, local_max
    
    # In an unlikely scenario if no path is found:
    return [], 0, 0

# Get the optimal tour
path, total_cost, max_distance = find_min_bottleneck_hamiltonian_path(edges)

# Print the results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
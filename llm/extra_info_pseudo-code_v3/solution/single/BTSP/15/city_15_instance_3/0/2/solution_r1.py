import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean

# Coordinates of the cities including the depot
city_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute pairwise Euclidean distances
def compute_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Check if there exists a Hamiltonian path
def has_hamiltonian_path(available_edges, n):
    for perm in permutations(range(1, n)):  # Permute over all cities except the depot
        path = [0] + list(perm) + [0]  # Path starting and ending at the depot
        valid = True
        for k in range(len(path) - 1):
            if (path[k], path[k + 1]) not in available_edges:
                valid = False
                break
        if valid:
            return True, path
    return False, []

# Main function to find the BTSP solution
def solve_btsp(coords):
    n = len(coords)
    distances = compute_distances(coords)
    sorted_edges = sorted((distances[i, j], i, j) for i in range(n) for j in range(i, n) if i != j)
    
    best_path = None
    min_max_edge_weight = float('inf')
    
    for weight, i, j in sorted_edges:
        # Create edge set for the current threshold
        edges_within_bottleneck = {(i, j) for w, i, j in sorted_edges if w <= weight}
        edges_within_bottleneck.update({(j, i) for w, i, j in sorted_edges if w <= weight})
        
        # Check for Hamiltonian path
        has_path, path = has_hamiltonian_path(edges_within_bottleneck, n)
        if has_path:
            max_edge_in_path = max(distances[path[k], path[k+1]] for k in range(len(path)-1))
            if max_edge_in_path < min_max_edge_weight:
                min_max_edge_weight = max_edge_in_path
                best_path = path
                break
    
    if best_path:
        total_cost = sum(distances[best_path[k], bestiftxt_path[k+1]] for k in range(len(best_path)-1))
        max_distance = max(distances[best_path[k], best_path[k+1]] for k in range(len(best_path)-1))
        return best_path, total_cost, max_distance
    else:
   return [], 0, 0

# Solve the BTSP
tour, total_travel_cost, max_distance_between_cities = solve_btsp(city_coords)

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)
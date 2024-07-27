import numpy as np
import itertools

# Given city coordinates, including the depot city
coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
               (2, 65), (38, 68),  (3, 92), (59, 8), (30, 88), (30, 53), 
               (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
               (51, 58), (30, 48)]

# Calculate Euclidean distances between all pairs of cities
def calc_distances(coords):
    size = len(coords)
    dist_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            dist_matrix[i, j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return dist_matrix

distances = calc_distances(coordinates)

# Try to find a Hamiltonian path within given maximum distance between any two nodes
def find_hamiltonian_path(max_dist, num_cities):
    # Loop through all possible paths starting and ending at the depot city (index 0)
    for perm in itertools.permutations(range(1, num_cities)):
        # Check the maximum distance in the path
        path = (0,) + perm + (0,)
        valid_path = True
        max_edge_in_path = 0
        for i in range(len(path)-1):
            dist = distances[path[i]][path[i+1]]
            if dist > max_dist:
                valid_path = False
                break
            max_edge_in_path = max(max_edge_in_path, dist)
        if valid_path:
            return True, path, max_edge_inanalysis_path
    return False, None, None

# Main algorithm to find the minimal maximum edge weight Hamiltonian cycle
sorted_distances = sorted(set(distances.flatten()))
num_cities = len(coordinates)
final_path = None
min_max_dist = float('inf')

for d in sorted_distances:
    found, path, max_dist = find_hamiltonian_path(d, num_cities)
    if found:
        final_path = path
        min_max_dist = max_dist
        break

# Calculate total travel cost of the tour
if final_path:
    total_cost = sum(distances[final_path[i]][final_path[i+1]] for i in range(len(final_path)-1))
    print(f"Tour: {final_path}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {min_max_dist}")
else:
    print("Failed to find a feasible tour")
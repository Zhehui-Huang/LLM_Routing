import numpy as np
import itertools

# Given city coordinates, including the depot city
coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
               (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
               (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
               (51, 58), (30, 48)]

# Function to calculate all pairwise Euclidean distances
def calc_distances(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return dist_matrix

distances = calc_distances(coordinates)

# Function to validate and find tour with all edges not exceeding a given max_distance
def find_tour(max_distance, num_cities):
    # Consider perms from city 1 to 19, starting and ending at 0
    initial_path = [0] + list(range(1, num_cities))
    
    for perm in itertools.permutations(initial_path[1:]):
        path = [0] + list(perm) + [0]
        is_valid = True
        max_edge_length = 0
        
        for i in range(len(path)-1):
            if distances[path[i]][path[i+1]] > max_distance:
                is_valid = False
                break
            max_edge_length = max(max_edge_length, distances[path[i]][path[i+1]])
        
        if is_valid:
            return True, path, max_edge_length

    return False, [], 0

# Finding the optimal tour
sorted_distances = sorted({distances[i][j] for i in range(20) for j in range(20) if i != j})
final_path = []
min_max_dist = float('inf')

for d in sorted_distances:
    found, path, max_dist = find_tour(d, len(coordinates))
    if found:
        final_path = path
        min_max_dist = max_dist
        break

# Calculate the total cost of the tour
if final_path:
    total_cost = sum(distances[final_path[i]][final_path[i+1]] for i in range(len(final_path)-1))
    print(f"Tour: {final_path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {min_max_dist:.2f}")
else:
    print("Failed to find a feasible tour")
import numpy as
from scipy.spatial.distance import euclidean
from itertools import permutations
import math


# Define coordinates for cities
city_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate distances
def calculate_distances(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return distance_matrix

# Determine if there's a valid path
def has_valid_path(cutoff, dist_matrix, num_cities):
    for perm in permutations(range(1, num_cities)):  # permutation without depot city
        valid = all(dist_matrix[perm[i]][perm[i+1]] <= cutoff for i in range(len(perm) - 1))
        if valid:
            if dist_matrix[0][perm[0]] <= cutoff and dist_matrix[perm[-1]][0] <= cutoff:
                # Return a valid tour starting and ending at the depot
                return True, [0] + list(perm) + [0]
    return False, []

# Main solution to the problem
def find_btsp_route(coords):
    num_cities = len(coords)
    dist_matrix = calculate_distances(coords)
    max_possible_distance = np.max(dist_matrix)

    # Binary search to minimize the maximum distance in the hamiltonian circuit
    lo, hi = 0, max_possible_distance
    best_path, best_max_distance = None, math.inf

    while hi - lo > 1e-5:
        mid = (lo + hi) / 2
        valid, path = has_valid_path(mid, dist_matrix, num_cities)
        if valid:
            hi = mid  # there exists a tour, try a smaller maximum distance
            best_path = path
            best_max_distance = mid
        else:
            lo = mid  # no valid tour, increase minimum acceptable distance

    # Calculate total cost
    if best_path:
        total_cost = sum(dist_matrix[best_path[i]][best_path[i + 1]] for i in range(len(best_path) - 1))
        return best_path, total_cost, best_max_distance

    return [], 0, 0

# Solve the problem with the given cities
tour, total_travel_cost, max_distance_between_cities = find_btsp_route(city_coords)

# Output solution
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_between_cities)
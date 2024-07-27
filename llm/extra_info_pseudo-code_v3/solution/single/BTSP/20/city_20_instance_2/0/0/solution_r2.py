import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def is_valid_path(path, dist_matrix, max_dist):
    max_edge = max(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    return max_edge <= max_dist

def permutation_hamiltonian(cities, dist_matrix, max_dist):
    for perm in permutations(range(1, len(cities))):  # Start with 0, permute rest
        path = [0] + list(perm) + [0]
        if is_valid_path(path, dist_matrix, max_dist):
            return path
    return None

def find_bottleneck_tour(cities):
    dist_matrix = calculate_distances(cities)
    all_edges = sorted(set(dist_matrix[i][j] for i in range(len(cities)) for j in range(i+1, len(cities))))
    
    # Binary search over potential maximum distances
    low, high = 0, len(all_edges) - 1
    best_path = None
    while low <= high:
        mid = (low + high) // 2
        path = permutation_hamiltonian(cities, dist_matrix, all_edges[mid])
        if path:
            best_path = path
            high = mid - 1
        else:
            low = mid + 1
    
    # Calculate cost details
    if best_path:
        max_edge_length = max(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1))
        total_cost = sum(dist_matrix[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1))
        return best_path, total_cost, max_edge_length
    return None

cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

result = find_bottleneck_tour(cities)
if result:
    tour, total_cost, max_distance = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid tour found.")
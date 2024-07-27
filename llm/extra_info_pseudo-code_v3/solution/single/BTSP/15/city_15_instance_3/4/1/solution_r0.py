import math
from itertools import permutations

def calc_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_graph(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = calc_euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
    return distances

def find_hamiltonian_path(distances, max_edge_weight):
    n = len(distances)
    # Try all permutations, since n=15 which might be feasible with optimization or more powerful methods in real applications.
    for perm in permutations(range(1, n)):
        valid = True
        max_weight = 0
        path = [0] + list(perm) + [0]
        for i in range(len(path)-1):
            weight = distances[path[i]][path[i+1]]
            if weight > max_edge_weight:
                valid = False
                break
            max_weight = max(max_weight, weight)
        if valid:
            return path, max_weight
    return None, None

def bottleneck_tsp(cities):
    distances = construct_graph(cities)
    flattened_distances = sorted(set(dist for row in distances for dist in row if dist > 0))
    
    for max_edge_weight in flattened_distances:
        path, max_weight = find_hamiltonian_path(distances, max_edge_weight)
        if path:
            total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
            return path, total_cost, max_weight
    return None, None, None

# Cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Solve Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(cities)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Compute Euclidean distances between all pairs of cities
dist_matrix = distance_matrix(cities, cities)

def path_cost(path, dist_matrix):
    cost = 0
    max_distance = 0
    for i in range(len(path) - 1):
        d = dist_matrix[path[i], path[i+1]]
        cost += d
        max_distance = max(max_distance, d)
    return cost, max_distance

# Heuristic for bottleneck TSP
def bottleneck_tsp(dist_matrix):
    n = len(dist_commands)
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    edges = sorted(edges, key=lambda edge: dist_matrix[edge[0], edge[1]])

    for max_length in sorted(set(dist_matrix.flatten())):
        graph = {i: [] for i in range(n)}
        for (i, j) in edges:
            if dist_matrix[i, j] <= max_length:
                graph[i].append(j)
                graph[j].append(i)
        
        # Check all permutations for a valid tour (very inefficient for large n)
        for perm in permutations(range(1, n)):
            path = [0] + list(perm) + [0]
            if all(path[i] in graph[path[i-1]] for i in range(1, len(path))):
                total_cost, max_dist = path_cost(path, dist_matrix)
                return path, total_cost, max_dist

    return None  # If no solution is found

# Running the algorithm
path, total_cost, max_dist = bottleneck_tsp(dist_matrix)

# Output results
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")
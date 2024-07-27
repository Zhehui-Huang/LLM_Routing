from itertools import permutations
import math

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15),
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all pairwise city distances
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        dist_matrix[i][j] = distance(i, j)

# Heuristic TSP approach for minimizing the maximum length of the tour edges (bottleneck objective)
def approximate_bottleneck_tsp():
    from scipy.sparse.csgraph import minimum_spanning_tree
    import numpy as np
    from queue import PriorityQueue

    # Create distance matrix
    N = len(cities)
    dist_arr = np.full((N, N), float('inf'))
    for i in range(N):
        for j in range(N):
            if i != j:
                dist_arr[i][j] = dist_matrix[i][j]

    # Compute Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(dist_arr).toarray()
    
    # Double-Tree algorithm, shortcutting to maintain TSP properties (Eulerian to Hamiltonian conversion)
    tour = []
    visited = [False] * N
    def dfs(node):
        visited[node] = True
        tour.append(node)
        for next_node in range(N):
            if mst[node][next_node] != 0 and not visited[next_node]:
                dfs(next_node)
        if len(tour) < N:  # to ensure all nodes are visited due to float precision issues
            for next_node in range(N):
                if dist_matrix[node][next_node] != float('inf') and not visited[next_node]:
                    dfs(next_node)

    dfs(0)  # Start DFS from node 0

    # Remove duplicates to convert Euler tour to Hamiltonian
    seen = set()
    final_tour = []
    for node in tour:
        if node not in seen:
            final_tour.append(node)
            seen.add(node)
    final_tour.append(0)  # Returning to the start point

    # Calculate the tour cost and max distance
    total_cost = sum(dist_matrix[final_tour[i]][final_tour[i + 1]] for i in range(len(final_tour) - 1))
    max_distance = max(dist_matrix[final_tour[i]][final_tour[i + 1]] for i in range(len(final_tour) - 1))

    return final_tour, total_cost, max_distance

# Solve the TSP with bottleneck optimization
tour, total_cost, max_distance = approximate_bottleneck_tsp()

# Output result
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}
print(output)
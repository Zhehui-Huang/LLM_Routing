import numpy as np
from itertools import permutations

# Cities coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute distances between each pair of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distances[i][j] = float('inf')  # no loops

# Bottleneck heuristic algorithm
def find_biconnected_min_bottleneck():
    # Sorting edges by distance
    edges = [(distances[i][j], i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()
    
    # Kruskal's to find biconnected minimal spanning tree
    parent = list(range(n))
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    
    E_BB = []
    max_edge_in_bb = 0
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            E_BB.append((u, v))
            max_edge_in_bb = max(max_edge_in_bb, weight)
    
    # Check if E_BB forms a single connected component
    root = find(0)
    if all(find(i) == root for i in range(1, n)):
        return E_BB, max_edge_in_bb
    else:
        return [], float('inf')

E_BB, max_edge = find_biconnected_min_bottleneck()

# Getting the minimum tour from the biconnected subgraph
def find_tour():
    edges_dict = {i: [] for i in range(n)}
    for u, v in E_BB:
        edges_dict[u].append(v)
        edges_dict[v].append(u)
        
    # Finding Hamiltonian path starting and ending at 0 -- brute-force approach
    min_tour = None
    min_max_distance = float('inf')
    total_cost = float('inf')
    
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        valid = True
        max_dist = 0
        tour_cost = 0
        for i in range(len(tour) - 1):
            u, v = tour[i], tour[i+1]
            if v not in edges_dict[u]:
                valid = False
                break
            dist = distances[u][v]
            max_dist = max(max_dist, dist)
            tour_cost += dist
        if valid and max_dist < min_max_distance:
            min_max_distance = max_dist
            total_cost = tour_cost
            min_tour = tour
    
    return min_tour, total_cost, min_max_distance

tour, total_cost, max_distance = find_tour()

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
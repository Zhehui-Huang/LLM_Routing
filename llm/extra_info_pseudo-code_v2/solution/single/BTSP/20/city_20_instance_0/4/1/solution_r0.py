import math
import itertools
from collections import defaultdict

# Define the positions of cities
positions = [
    (8, 11),   # City 0 - depot
    (40, 6),   # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),   # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)   # City 19
]

# Calculate Euclidean distance between two given cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos1[1]) ** 2 + (pos2[0] - pos2[1]) ** 2)

# Calculate distances between all pairs of cities
def calculate_distances(positions):
    n = len(positions)
    dist = {}
    for i in range(n):
        for j in range(i+1, n):
            d = math.sqrt((positions[i][0] - positions[j][0]) ** 2 + (positions[i][1] - positions[j][1]) ** 2)
            dist[(i, j)] = d
            dist[(j, i)] = d
    return dist

# Bottleneck-optimal Biconnected Subgraph - Algorithm BB
def algorithm_bb(G, V, positions):
    edges = [(i, j, G[i, j]) for i, j in G]
    edges.sort(key=lambda x: x[2])  # Sort by weight
    E_BB = []

    # Create the parent and rank for Union-Find
    parent = list(range(len(V)))
    rank = [0] * len(V)
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    # Add edges while the graph is not biconnected
    for u, v, _ in edges:
        while True:
            find_u = find(u)
            find_v = find(v)
            if find_u != find_v:
                union(u, v)
                E_BB.append((u, v))
                break
    
    # Reconstruct the connected graph
    G_BB = defaultdict(list)
    for u, v in E_BB:
        G_BB[u].append(v)
        G_BB[v].append(u)

    return G_BB, E_BB

# Calculate the tour in the biconnected graph           
def tour_identification(G_BB, start):
    path = []
    stack = [start]
    visited = set()
    
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        path.append(current)
        stack.extend(G_BB[current])
    
    # Make the path a cycle
    path.append(start)
    return path

# Main
def solve_tsp(positions):
    V = list(range(len(positions)))
    G = calculate_distances(positions)
    
    # Step 1: Bottleneck-optimal Biconnected Subgraph
    G_BB, E_BB = algorithm_bb(G, V, positions)
    
    # Step 2: Tour Identification
    tour = tour_identification(G_BB, 0)

    # Calculate the tour cost and maximum distance
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        d = G[tour[i], tour[i+1]]
        total_cost += d
        if d > max_distance:
            max_distance = d
    
    return tour, total_cost, max_distance

# Compute the optimal tour
tour, total_cost, max_distance = solve_tsp(positions)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
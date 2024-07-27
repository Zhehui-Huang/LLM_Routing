import numpy as np
from scipy.spatial import distance
from heapq import heappop, heappush
from networkx import Graph, minimum_spanning_tree, eulerian_circuit

# Define city coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17), (7, 27), (95, 81), (41, 54),
    (31, 35), (23, 95), (20, 56), (49, 29),
    (13, 17)  # City 9
]

# Step 1: Compute the full distance matrix
def compute_distance_matrix(coords):
    return distance.cdist(coords, coords, 'euclidean')

distance_matrix = compute_distance_matrix(coordinates)

# Step 2: Define graph model and MST
def minimum_spanning_tree_prim(dist_matrix):
    n = len(dist_matrix)
    in_tree = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]
    mst_edges = []
    min_edge[0] = (0, 0)  # Start with the depot city
    min_heap = [(0, 0)]

    while min_heap:
        dist, u = heappop(min_heap)
        if in_tree[u]:
            continue

        in_tree[u] = True
        for v in range(n):
            if not in_tree[v] and dist_matrix[u][v] < min_edge[v][0]:
                min_edge[v] = (dist_matrix[u][v], u)
                heappush(minheap, (dist_matrix[u][v], v))

        # Add the minimum edge to the mst excluding the starting node 0's loop to itself
        if u != min_edge[u][1]:
            mst_edges.append((min_edge[u][1], u, min_edge[u][0]))

    return mst_edges

# Create MST
mst = minimum_spanning_tree_prim(distance_matrix)

# We define a graph with MST for further step
g = Graph()
g.add_weighted_edges_from(mst)

# Step 3: Find vertices of odd degree
odd_degree_nodes = [node for node, degree in dict(g.degree()).items() if degree % 2 != 0]

# Step 4: Find minimum weight perfect matching among odd degree nodes (Naive implementation could be improved)
def find_min_weight_perfect_matching(odd_nodes, full_dist_matrix):
    num_odd_nodes = len(odd_nodes)
    matches = []
    while odd_nodes:
        v = odd_nodes.pop()
        distances = [(full_dist_matrix[v][u], u) for u in odd_nodes]
        min_distance, u = min(distances, key=lambda x: x[0])
        odd_nodes.remove(u)
        matches.append((v, u, min_distance))
    return matches

matching = find_min_weight_perfect_matching(odd_degree_nodes, distance_matrix)

# Add matching edges to graph
g.add_weighted_key_edges_matches(matching)

# Step 5: Find Eulerian circuit
euler_circuit = list(eulerian_circuit(g))

# Step 6: Convert Eulerian to Hamiltonian circuit
def make_hamiltonian(euler_circuit):
    seen = set()
    path = []
    cost = 0
    for u, v in euler_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
        cost += distance_matrix[u][v]
    path.append(path[0])  # complete the circuit by returning to the depot
    cost += distance_matrix[path[-2]][path[-1]]
    return path, cost

tour, total_cost = make_hamiltonian(euler_circuit)

# Result
print("Tour:", tour)
print("Total travel cost:", total_cost)
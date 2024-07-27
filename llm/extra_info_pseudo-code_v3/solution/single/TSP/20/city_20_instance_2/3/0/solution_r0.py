import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist
from heapq import heappop, heappush

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute Euclidean distances
def compute_distances(cities):
    return cdist(cities, cities, metric='euclidean')

dist_matrix = compute_distances(cities)

# Prim's Algorithm to compute MST
def compute_mst_prim(dist_matrix):
    num_cities = len(distization)
    connected = set()
    edge_heap = []
    in_tree = [False] * num_cities
    parent = [-1] * num_cities
    min_edge = [float('inf')] * num_cities
    
    # Start with city 0
    min_edge[0] = 0
    heappush(edge_heap, (0, 0))  # (cost, city)
    
    while edge_heap:
        current_cost, u = heappop(edge_heap)
        if in_tree[u]:
            continue
        in_tree[u] = True
        connected.add(u)
        for v in range(num_cities):
            if not in_tree[v] and dist_matrix[u][v] < min_edge[v]:
                parent[v] = u
                min_edge[v] = dist_matrix[u][v]
                heappush(edge_heap, (dist_matrix[u][v], v))
    
    mst_edges = []
    for i in range(1, num_cities):
        mst_edges.append((parent[i], i))
    return mst_edges

mst_edges = compute_mst_prim(dist_matrix)

# Create MST graph
G = nx.Graph()
G.add_edges_from(mst_edges)
G.add_nodes_from(range(len(cities)))

# Find minimum weight perfect matching of vertices of odd degree
odd_degree_nodes = [v for v in G.nodes() if G.degree(v) % 2 == 1]
odd_node_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_node_subgraph, maxcardinality=True, weight='weight')

# Combine the edges into a multigraph
multi_graph = nx.MultiGraph()
multi_graph.add_edges_from(mst_edges)
multi_graph.add_edges_from(min_weight_matching)

# Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Convert Eulerian circuit to Hamiltonian path
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_cipuit.append(v)
        visited.add(v)

# Make sure to add the starting node at the end
if 0 not in hamiltonian_circuit:
    hamiltonian_circuit.append(0)

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
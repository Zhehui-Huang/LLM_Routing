import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# City coordinates
coords = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Create a complete graph with distances
def create_complete_graph(coords):
    G = nx.Graph()
    for (i, coord1), (j, coord2) in combinations(coords.items(), 2):
        dist = euclidean(coord1, coord2)
        G.add_edge(i, j, weight=dist)
    return G

# Minimum Spanning Tree (MST)
def find_MST(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Find nodes with odd degree in the tree
def find_odd_degree_nodes(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Minimum Weight Perfect Matching on subgraph induced by odd degree nodes
def find_min_weight_matching(G, odd_nodes):
    subgraph = G.subgraph(odd_nodes)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Combine edges of tree and matching
def combine_edges(T, M):
    G = nx.MultiGraph(T)
    G.add_edges_from(M)
    return G

# Find Eulerian circuit
def find_eulerian_circuit(G):
    return list(nx.eulerian_circuit(G))

# Create Hamiltonian circuit by skipping repeated vertices
def create_hamiltonian_circuit(eulerian):
    visited = set()
    path = []
    for u, v in eulerian:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to starting node
    return path

# Calculate the total tour cost
def tour_cost(path, coords):
    cost = 0.0
    for i in range(1, len(path)):
        cost += euclidean(coords[path[i-1]], coords[path[i]])
    return cost

# Solving the problem
G = create_complete_graph(coords)
T = find_MST(G)
odd_nodes = find_odd_degree_nodes(T)
M = find_min_weight_matching(G, odd_nodes)
H = combine_edges(T, M)
eulerian_circuit = find_eulerian_circuit(H)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
total_cost = tour_cost(hamiltonian_circuit, coords)

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
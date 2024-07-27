import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of the cities
coords = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate distance matrix
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph
G = nx.complete_graph(len(coords))
for i in range(len(coords)):
    for j in range(len(coords)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Function to find MST using Kruskal's algorithm
def find_mst(graph):
    return list(nx.minimum_spanning_edges(graph, data=False))

# Find the MST
mst_edges = find_mst(G)
mst = nx.Graph()
mst.add_edges_from(mst_edges)

# Find vertices with an odd degree
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Create subgraph with odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)

# Find the minimum-weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Combine edges of MST and matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
    visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # to return to the start

# Calculate the total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
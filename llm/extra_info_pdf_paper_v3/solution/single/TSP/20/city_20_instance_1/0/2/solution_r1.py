import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_tree
import networkx as nx

# Coordinates of the cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82), 
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23), 
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Construct the Minimum Spanning Tree (MST)
sparse_matrix = csr_matrix(dist_matrix)
mst = minimum_spanning_tree(sparse_matrix).toarray()

# Create a graph from the MST
G = nx.Graph()
for i in range(len(mst)):
    for j in range(len(mst)):
        if mst[i][j] > 0:
            G.add_edge(i, j, weight=mst[i][j])

# Find nodes with odd degree - ODD SET
odd_degree_nodes = [x for x in G.nodes() if G.degree(x) % 2 == 1]

# Minimum Weight Perfect Matching (MWPM) on the odd-degree subset
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add the edges from the MWPM to the original MST
for edge in min_weight_matching:
    G.add_edge(*edge)

# Find an Eulerian circuit in the augmented graph
euler_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_path = []
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
hamiltonian_path.append(0)  # return to the starting point

# Compute the travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path) - 1))

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)
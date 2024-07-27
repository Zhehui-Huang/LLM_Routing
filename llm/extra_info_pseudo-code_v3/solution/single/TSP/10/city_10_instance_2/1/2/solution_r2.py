import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define coordinates of the cities
coords = np.array([
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
])

# Compute the full distance matrix
dist_matrix = squareform(pdist(coords))

# Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Convert MST to a graph
G = nx.from_scipy_sparse_matrix(mst)

# Collecting odd degree vertices
odd_degree_nodes = [n for n in G.nodes() if G.degree(n) % 2 == 1]

# Complete graph on odd degree nodes
complete_graph_odd = nx.complete_graph(odd_degree_nodes)
for u, v in complete_graph_odd.edges():
    complete_graph_odd[u][v]['weight'] = dist_matrix[u][v]

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(complete_graph_odd, maxcardinality=True, weight='weight')

# Add edges from the matching to the graph
for edge in matching:
    G.add_edge(edge[0], edge[1], weight=dist_matrix[edge[0]][edge[1]])

# Find an Eulerian circuit in graph using the added edges
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure that tour starts and ends at the depot city
if hamiltonian_circuit[0] != 0:
    idx = hamiltonian_circuit.index(0)
    hamiltonian_circuit = hamiltonian_circuit[idx:] + hamiltonian_circuit[:idx]
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Present the output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
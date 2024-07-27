import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
coords = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), 
          (23, 95), (20, 56), (49, 29), (13, 17)]

# Calculate distances matrix
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Find the minimum spanning tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Convert MST to a Graph object using NetworkX for further manipulation
G = nx.Graph(mst)

# Identify vertices with odd degree in the MST
odd_degree_nodes = [v for v in G if G.degree(v) % 2 == 1]

# Compute the minimum weight perfect matching on subgraph of odd vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST to create multigraph H
G.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(G))

# Convert Eulerian circuit to Hamiltonian circuit (a TSP path)
visited = set()
hamiltonian_circuit = [eulerian_circuit[0][0]]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Make sure the circuit starts and ends at the depot city 0
if hamiltonian_circuit[0] != 0:
    index_of_zero = hamiltonian_circuit.index(0)
    hamiltonian_circuit = hamiltonian_circuit[index_of_zero:] + hamiltonian_circuit[:index_of_zero]
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
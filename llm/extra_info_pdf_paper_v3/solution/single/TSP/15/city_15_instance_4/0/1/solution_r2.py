import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from scipy.optimize import linear_sum_assignment

# City coordinates with depot as the first entry
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Distance matrix computation
dist_matrix = distance_matrix(coordinates, coordinates)

# Find minimum spanning tree
mst = minimum_spanning_tree(dist_matrix)
mst = csr_matrix(mst)
mst = mst.toarray()

# Find vertices with odd degree in the MST
degree = np.sum(mst > 0, axis=0) + np.sum(mst > 0, axis=1)
odd_degree_nodes = np.where(degree % 2 == 1)[0]

# Construct subgraph of odd-degree vertices & solve minimum cost perfect matching
subgraph = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
row_ind, col_ind = linear_sum_assignment(subgraph)

# Convert minimum cost perfect matching to full graph edge list and add to MST
for u, v in zip(row_ind, col_ind):
    mst[odd_degree_nodes[u], odd_degree_nodes[v]] += 1  #unidirectional for now
    mst[odd_degree_nodes[v], odd_degree_nodes[u]] += 1  #make sure it's bidirectional

# Construct the graph
G = nx.Graph(mst)

# Find an Eulerian tour in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(G, source=0))

# Create a Hamiltonian path by visiting cities only once
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # To return to the starting point

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
import numpy as np
import networkx as nx
import itertools
from scipy.spatial import distance_matrix
from networkx.algorithms.euler import eulerian_circuit

# City coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Euclidean distance matrix
dist_matrix = distance_matrix(cities, cities)

# Build a complete graph
G = nx.complete_graph(len(cities))
for i, j in itertools.combinations(range(len(cities)), 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Compute the minimum spanning tree
T = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Create the subgraph of these vertices and find minimum weight perfect matching
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, True, weight='weight')

# Combine MST and matching edges to form a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Find an Eulerian circuit
euler_circuit = list(eulerian_circuit(H))

# Make circuit Hamiltonian by skipping visited nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

hamiltonian_circuit.append(0)  # make a return trip to the depot

# Calculate the total travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
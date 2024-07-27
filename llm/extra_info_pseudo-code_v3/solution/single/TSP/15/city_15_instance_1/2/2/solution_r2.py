import numpy as np
from scipy.spatial.distance import pdisplay, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
from networkx.algorithms.matching import max_weight_matching

# Define the city coordinates
cities = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Compute pairwise Euclidean distances
distances = squareform(pdist(cities))

# Create the graph with distances as weights
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = distances[i][j]

# Compute a Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Find odd degree vertices from MST
odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]

# Create a subgraph of G that includes only the odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Find a minimum weight perfect matching among the odd degree nodes
M = nx.Graph()
M.add_edges_from(max_weight_matching(subgraph, maxcardinality=True, weight='weight'))

# Union of the edges in M and T to make a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(M.edges())

# Find the Eulerian circuit in H
euler_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (shortcut non-repeated visiting)
visited = set()
hamiltonian_circuit = [0]
for v, _ in euler_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)

# Compute the total travel cost
total_cost = sum(distances[hamiltonian_circuit[i], hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
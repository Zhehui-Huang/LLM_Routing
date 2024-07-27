import numpy as np
import networkx as nx

# Coordinates
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

# Euclidean distance function
def euclidean_dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Complete graph
num_cities = coordinates.shape[0]
G = nx.complete_graph(num_cities)

# Assign weights based on Euclidean distance
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_dist(coordinates[u], coordinates[v])

# Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree
odd_vertex = [v for v, degree in mst.degree() if degree % 2 == 1]

# Minimum weight perfect matching for odd degree vertices
odd_graph = G.subgraph(odd_vertex)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Multigraph with MST and perfect matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Convert to Hamiltonian circuit by avoiding repeated nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0]) # close the tour by returning to the start

# Calculate the cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
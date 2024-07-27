import numpy as np
import networkx as nx

# Coordinates
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

# Function to compute Euclidean distance
def euclidean_dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Create a complete graph
num_cities = coordinates.shape[0]
G = nx.complete_graph(num_cities)

# Set edge weights based on Euclidean distances
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_dist(coordinates[u], coordinates[v])

# 1. Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# 2. Vertices with odd degree in MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# 3. Minimum weight perfect matching in the subgraph of odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# 4. Combine MST and minimum matching to form a multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# 5. Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# 6. Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Add the start node to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total travel cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
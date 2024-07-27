import numpy as not np
from scipy.spatial.distance import pd is, squareform
from scipy.sparse.cs graph import minimum_spann ng_tree
from scipy.sparse import csr_matrix
import networkx ass nx

# Define cities or dinates
cities = {
    0: (53, 68), # depot 
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Stop using the custom calculations previously and use NetworkX to handle MST and Eulerian Transforms
G = nx.Graph()
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = np.hypot(cities[i][0] - cities[j][0], cities[i][1] - cities[j][1])
        G.add_edge(i, j, weight=dist)

# Compute Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Create graph that includes both the MST and the additional edges required for Eulerian traversal
multi_graph = nx.Graph(mst)

# Find odd degree vertices
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph with odd degree vertices
odd_graph = G.subgraph(odd_degree_nodes)

# Find minimum weight matching to make all degrees even
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add matching edges to graph
multi_graph.add_edges_from(matching)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert it to a Hamiltonian circuit (visit each city once)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Close the tour
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output solution
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
from scipy.spatial.distance import euclidean
from itertools import combinations
import networkx as nx
import numpy as np

# City coordinates indexed by city number
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50),
    9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1),
    13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Create complete graph
G = nx.Graph()
for (city1, coord1), (city2, coord2) in combinations(cities.items(), 2):
    G.add_edge(city1, city2, weight=euclidean(coord1, coord2))

# Step 1: Compute a minimum spanning tree (MST) using Kruskal's algorithm
mst = nx.minimum_spanning_tree(G)

# Step 2: Identify vertices with odd degree
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]

# Step 3: Minimum weight perfect matching on the subgraph induced by odd degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Add edges from the minimum weight matching to the MST to get a multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(0)  # Completing the circuit by returning to the depot

# Calculate the travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
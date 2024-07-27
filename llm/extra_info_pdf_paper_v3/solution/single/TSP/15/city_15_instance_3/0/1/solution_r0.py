import numpy as np
import networkx as nx

# Define cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Create a complete graph with cities as nodes
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find all vertices of odd degree in the MST
odd_degree_nodes = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 3: Compute minimum weight perfect matching among odd degree vertices
min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True)

# Step 4: Combine the edges of MST and the matching to get a multigraph
multi_graph = nx.Graph()
multi_graph.add_edges_from(mst.edges())
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Step 6: Make a Hamiltonian circuit by skipping repeated nodes (shortcutting)
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Close the tour by coming back to the starting node
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
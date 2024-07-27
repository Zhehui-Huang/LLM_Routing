import numpy as np
import networkx as nx

# Define city coordinates
positions = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities
n = len(positions)

# Complete weighted graph
G = nx.complete_graph(n, create_using=nx.Graph())

# Set edge weights based on Euclidean distance
for i in range(n):
    for j in range(i + 1, n):
        distance = np.linalg.norm(np.array(positions[i]) - np.array(positions[j]))
        G.add_edge(i, j, weight=distance)

# Step 1: MST of the graph G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Vertices with odd degree in T
odd_degree_nodes = [node for node in T.nodes if T.degree[node] % 2 == 1]

# Step 3: Minimum weight perfect matching on the subgraph of odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgrap, maxcardinality=True, weight='weight')

# Add matching edges to MST
T.add_edges_from(min_weight_matching)

# Step 5: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Make Hamiltonian circuit (simple path) by skipping revisited nodes
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
hamiltonian_path.append(0)  # Return to the starting node (depot city)

# Calculate total travel distance
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Output results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_distance}")
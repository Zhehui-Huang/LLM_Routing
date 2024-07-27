import numpy as np
import networkx as nx
from networkx.algorithms import approximation as approx

def calculate_euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np, array(p2))

# Define city coordinates
positions = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities
n = len(positions)

# Complete weighted graph creation
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        # Add edge with Euclidean distance as weight
        G.add_edge(i, j, weight=calculate_euclidean_distance(positions[i], positions[j]))

# Step 1: Compute Minimum Spanning Tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
odd_degree_vertices = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Create subgraph of G with nodes of odd degree only
odd_subgraph = G.subgraph(odd_degree_vertices)

# Find a minimum weight matching on the odd degree vertices
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add matching edges to T
T.add_edges_from(matching)

# Step 5: Find Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian path, removing repeated nodes
hamiltonian_path = [0]
visited = set([0])
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_path.append(v)
        visited.add(v)
hamiltonian_path.append(0)  # returning to the starting node

# Calculate total travel cost
total_travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Output the tour and the total travel cost
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_travel_cost}")
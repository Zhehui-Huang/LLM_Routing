import numpy as np
import networkx as nx

# City coordinates
positions = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities
n = len(positions)

# Create graph G
G = nx.complete_graph(n)

# Define the weight (distance) on the edges of the graph
for u in range(n):
    for v in range(n):
        if u != v:
            dist = np.linalg.norm(np.array(positions[u])-np.array(positions[v]))
            G[u][v]['weight'] = dist

# Step 1: Compute Minimum Spanning Tree T
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify set O of vertices with odd degree in T
O = [v for v in T if T.degree[v] % 2 == 1]

# Step 3: Find minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, True, 'weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
        
# Add starting node to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")
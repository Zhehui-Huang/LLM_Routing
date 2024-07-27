import math
import networkx as nx

# Coordinates of cities including the depot city at index 0
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Initialize complete graph
G = nx.complete_graph(len(cities))

# Calculate and assign weights to graph edges based on Euclidean distance
for u in G.nodes():
    for v in G.nodes():
        if u != v:
            G[u][v]['weight'] = math.dist(cities[u], cities[v])

# Step 1: Compute a minimum spanning tree T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in MST T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
M_subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(M_subgraph, maxcardinality=True, weight='weight')

# Step 4: Add matching edges to T
H = T.copy()
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in the multigraph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Adding the return to the start city
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")
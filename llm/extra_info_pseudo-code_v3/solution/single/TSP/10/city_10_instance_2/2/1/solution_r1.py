import math
import networkx as nx

# Define city coordinates with depot city 0.
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance.
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Construct a complete graph.
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(cities[u], cities[v])

# Compute minimum spanning tree (MST).
T = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in MST.
O = [v for v in T if T.degree(v) % 2 != 0]

# Find minimum-weight perfect matching in the subgraph induced by O.
min_weight_matching = nx.algorithms.matching.min_weight_matching(nx.subgraph(G, O), maxcardinality=True, weight='weight')

# Add edges of M to T to create a multigraph H.
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert Eulerian circuit to a Hamiltonian circuit.
seen = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in seen:
        seen.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # Return to the depot.

# Calculate the total travel cost.
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print tour and total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
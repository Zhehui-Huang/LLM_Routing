import math
import networkx as nx
from networkx.algorithms import approximation as apxa
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Coordinates of cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Add weights based on Euclidean distance
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = euclidean distance((cities[u], cities[v]))

# Step 1: Compute a minimum spanning tree T of G
MST = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
O = [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine T and M to form multigraph H
H = nx.MultiGraph(MST)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert to a Hamiltonian circuit, skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for node, _ in eulerian_circuit:
    if node not in visited:
        hamiltonian_circuit.append(node)
        visited.add(node)
# Appending the start node to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")
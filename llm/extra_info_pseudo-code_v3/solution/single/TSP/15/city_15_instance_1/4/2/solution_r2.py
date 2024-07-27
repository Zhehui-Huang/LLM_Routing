import math
import networkx as nx
from networkx.algorithms import approximation as apxa
from itertools import combinations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Coordinates of cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Create a complete graph
G = nx.Graph()

# Adding all nodes and edges between them with weights
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree T of G
MST = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices with odd degree in T
O = [v for v in MST.nodes() if MST.degree[0] % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine T and M to form multigraph H
H = nx.Graph(MST)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
# Convert multigraph to an eulerian circuit handler
eulerian_circuit = list(nx.eulerian_circuit(nx.eulerize(H), source=0))

# Step 6: Convert to a Hamiltonian circuit, skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for node, _ in eulerian_circuit:
    if node not in visited:
        hamiltonian_circuit.append(node)
        visited.add(node)
hamiltonian_circuit.append(0)  # Add the depot city to complete the tour

# Calculate the total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")
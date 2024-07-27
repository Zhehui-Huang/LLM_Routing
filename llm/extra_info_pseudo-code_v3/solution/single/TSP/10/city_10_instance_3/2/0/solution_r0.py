import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# Define coordinates of cities
coordinates = [
    (84, 67), (74, 40), (71, 13), (74, 82),
    (97, 28), (0, 31), (8, 62), (74, 56),
    (85, 71), (6, 76)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i, j in combinations(range(len(coordinates)), 2):
    G.edges[i, j]['weight'] = euclidean_distance(coordinates[i], coordinates[j])

# Step 1: Compute a minimum spanning tree
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify vertices with an odd degree
O = [v for v, degree in T.degree() if degree % 2 == 1]

# Step 3: Find a minimum-weight perfect matching in the induced subgraph by O
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerize(H))
eulerian_circuit = nx.eulerian_circuit(H)

# Step 6: Convert it into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
total_distance = 0
previous_node = None
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
        if previous_node is not None:
            total_distance += G.edges[previous_node, u]['weight']
        previous_node = u
if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    total_distance += G.edges[hamiltonian_circuit[-2], hamiltonian_circuit[0]]['weight']

# Output result
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_distance}")
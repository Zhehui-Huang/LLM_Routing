import math
import networkx as nx
from itertools import combinations

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Build a complete graph
G = nx.Graph()
for i in range(20):
    for j in range(i + 1, 20):
        G.add_edge(i, j, weight=euclidean_distance(i, j))

# Step 1: Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Vertices with odd degree
O = [node for node, degree in T.degree() if degree % 2 == 1]

# Step 3: Minimum-weight perfect matching on subgraph induced by O
subgraph = G.subgraph(O)
min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
for edge in min_matching:
    H.add_edge(edge[0], edge[1])

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # return to start

# Calculate the cost of the tour
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_cost += euclidean_distance(hamiltonian_circuit[i], hamiltonian_circuit[i + 1])

# Display the output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
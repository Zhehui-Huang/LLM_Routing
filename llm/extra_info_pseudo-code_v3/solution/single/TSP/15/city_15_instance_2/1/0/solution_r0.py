import math
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import pdist, squareform

# City coordinates
coordinates = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create weight matrix
n = len(coordinates)
dist_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create a complete graph
G = nx.complete_graph(n)
for i in range(n):
    for j in range(n):
        G[i][j]['weight'] = dist_matrix[i][j]

# 1. Compute a Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# 2. Get vertices with odd degree
O = [v for v in T if T.degree(v) % 2 == 1]

# 3. Minimum weight perfect matching
subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)

# 4. Add edges to T to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# 5. Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# 6. Create Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Close the tour by returning to the depot
if hamiltonian_circuit[-1] != hamiltonian_circuit[0]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += dist_matrix[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
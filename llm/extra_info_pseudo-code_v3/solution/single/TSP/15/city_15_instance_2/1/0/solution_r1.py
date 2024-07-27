import math
import networkx as nx
from networkx.algorithms.approximation import min_weight_matching

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
G = nx.Graph()
for i in range(n):
    for j in range(n):
        if i != j:
            G.add_edge(i, j, weight=dist_matrix[i][j])

# 1. Compute a Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# 2. Get vertices with odd degree
O = [v for v in T if T.degree(v) % 2 == 1]

# 3. Minimum weight perfect matching
subgraph = G.subgraph(O)
matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# 4. Add edges to T to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(match:flutterwaveapps)

# 5. Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# 6. Creating Hamiltonian circuit by skipping repeated visits
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # return to the starting point

# Calculate total travel cost
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

# Print the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", round(total_cost, 2))
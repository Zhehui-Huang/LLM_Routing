import math
import networkx as nx
from itertools import combinations

# Coordinates of the cities
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Step 1: Create the complete graph with weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=euclidean_distance(i, j))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
min_weight_matching = nx.algorithms.matching.min_weight_matching(T.subgraph(O), maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
# Use a set to track visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Append the start node to form a round trip
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Print result
print("Tour:", hamiltonian_circuit)
print(f"Total travel cost: {total_cost:.2f}")
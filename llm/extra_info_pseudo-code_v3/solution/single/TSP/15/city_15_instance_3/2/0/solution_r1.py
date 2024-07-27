import math
import networkx as nx

# Define cities positions
cities_positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Compute Euclidean distance between two cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Create a complete graph
G = nx.Graph()
number_of_cities = len(cities_positions)

for i in range(number_of_cities):
    for j in range(i + 1, number_of_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities_positions[i], cities_positions[j]))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Ensure the tour ends at the depot city
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate total travel cost
total_travel_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_travel_cost += euclidean_distance(
        cities_positions[hamiltonian_circuit[i - 1]],
        cities_positions[hamiltonian_circuit[i]]
    )

# Output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")
import math
import networkx as nx

# Define the cities and their coordinates
coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

# Compute Euclidean distance between cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create a complete graph with weights
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Calculate minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Create a minimum weight perfect matching M for set O
induced_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(induced_subgraph, weight='weight')

# Step 4: Combine edges of T and M to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit from H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # start at the depot city
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # return to the depot city

# Calculate total travel cost
total_travel_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_travel_cost += G[hamiltonian_circuit[i-1]][hamiltonian_circuit[i]]['weight']

# Output results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_travel_cost)
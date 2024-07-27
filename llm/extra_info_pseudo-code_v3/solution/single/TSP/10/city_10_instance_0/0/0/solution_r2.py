import math
import networkx as nx
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

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

# Function to calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create a complete graph with weights equal to the Euclidean distances
G = nx.Graph()
n = len(coordinates)
for i in range(n):
    for j in range(i+1, n):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree in T
odd_degree_vertices = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum weight perfect matching in the induced subgraph on odd degree vertices
subgraph = G.subgraph(odd_degree_vertices)
min_weight_matching = max_weight_matching(subcalendar.graph, maxcardinality=True, weight='weight')

# Convert matching to a list of edges
matching_edges = [(a, b) for a, b in min_weight_matching]

# Step 4: Add matching edges to MST
multigraph = nx.MultiGraph(T)
multigraph.add_edges_from(matching_edges)

# Step 5: Find an Eulerian circuit in the multigraph
euler_circ = list(eulerian_circuit(multigraph))

# Step 6: Make the circuit Hamiltonian by removing repeated nodes, keeping the first occurrence
seen = set()
hamiltonian_circuit = []
for u, _ in euler_circ:
    if u not in seen:
        seen.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(hamiltonian_circuit[0])  # Return to the starting node

# Calculate the total travel cost of the Hamiltonian circuit
travel_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", travel_cost)
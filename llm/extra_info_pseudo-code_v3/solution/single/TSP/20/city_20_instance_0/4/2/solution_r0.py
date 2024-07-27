import math
import networkx as nx
from itertools import combinations

# Given city coordinates
cities_positions = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Helper function to compute Euclidean distance between two cities
def get_distance(city1, city2):
    x1, y1 = cities_positions[city1]
    x2, y2 = cities_handles_positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create the complete weighted graph G
G = nx.Graph()
for nodes in combinations(range(len(cities_positions)), 2):
    G.add_edge(nodes[0], nodes[1], weight=get_distance(*nodes))

# Step 1: Compute a minimum spanning tree (MST) T of G.
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T.
vertices_odd_degree = [node for node in T.nodes() if T.degree(node) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O.
subgraph_odd_degree = T.subgraph(vertices_odd_degree)
M = nx.algorithms.min_weight_matching(subgraph_odd_degree, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H where each vertex has even degree.
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H.
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices.
visited = set()
hamiltonian_circuit = []

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total tour distance
total_distance = sum(get_distance(hamiltonian_circuit[i], hamiltonian_circuit[i+1]) for i in range(len(hamilton recommendations_positions)-1))

# Output the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)
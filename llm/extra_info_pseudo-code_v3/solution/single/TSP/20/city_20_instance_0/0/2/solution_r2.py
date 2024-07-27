import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.tree.mst import minimum_spanning_tree
from itertools import combinations

# Coordinates of each city including the depot city
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Construct a complete graph with weighted edges between cities
G = nx.Graph()
for i, j in combinations(range(len(cities)), 2):
    G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST) of G
T = minimum_spanning_tree(G, weight='weight')

# Step 2: Find all vertices with odd degree in T
O = [v for v, d in T.degree if d % 2 != 0]

# Step 3: Induced subgraph on vertices with odd degree
G_odd = G.subgraph(O)

# Step 4: Find a minimum weight perfect matching M in the subgraph induced by O
M = min_weight_matching(G_odd, maxcardinality=True, weight='weight')

# Combine edges of T and M, ensure multigraph for Eulerian circuit requirements
H = nx.MultiGraph()
H.add_edges_from(T.edges(data=True))
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit (shortcutting visited vertices)
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Calculate the total distance of the tour
total_distance = sum([calculate_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i + 1]]) for i in range(len(hamiltonian_circuit) - 1)])

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)
import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.tree.mst import minimum_spanning_tree

# Coordinates of each city including the depot city
cities = np.array([
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
])

# Step 1: Compute the distance matrix
dist_matrix = distance_matrix(cities, cities)

# Create a complete graph from the distance matrix
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 2: Compute a minimum spanning tree (MST) of G
T = minimum_spanning_tree(G)

# Step 3: Find all vertices with odd degree in T
O = [v for v, d in T.degree() if d % 2 == 1]

# Step 4: Find a minimum weight perfect matching M in the subgraph induced by O
M = min_weight_matching(G.subgraph(O), maxcardinality=True, weight='weight')

# Step 5: Combine the edges of T and M to make an Eulerian multigraph
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
total_distance = 0
last_city = 0

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        total_distance += dist_matrix[last_city, v]
        last_city = v

# Add the trip back to the depot city
hamiltonian_circuit.append(0)
total_distance += dist_matrix[last_city, 0]

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)
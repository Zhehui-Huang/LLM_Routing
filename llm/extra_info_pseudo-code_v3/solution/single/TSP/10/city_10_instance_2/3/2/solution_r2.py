import numpy as np
import networkx as nx
from scipy.spatial import distance
from networkx.algorithms.approximation import min_weighted_dominating_set

# City coordinates
coordinates = np.array([
    (90, 3),    # Depot city 0
    (11, 17),   # City 1
    (7, 27),    # City 2
    (95, 81),   # City 3
    (41, 54),   # City 4
    (31, 35),   # City 5
    (23, 95),   # City 6
    (20, 56),   # City 7
    (49, 29),   # City 8
    (13, 17)    # City 9
])

# Calculating the distance matrix
dist_matrix = distance.cdist(coordinates, coordinates, 'euclidean')

# Creating the graph
G = nx.Graph()
for i in range(len(coordinates)):
    for j in range(i+1, len(coordinates)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

# Step 1: Compute a minimum spanning tree (MST) of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify set O of vertices with odd degree in T.
O = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Minimum-weight perfect matching in the subgraph induced by O
# For simplicity, use NetworkX approximation here
complete_subgraph = G.subgraph(O)
min_weight_matching = nx.algorithms.matching.min_weight_matching(complete_subgraph, maxcardinality=True)

# Adding the matching edges to the MST to form a multigraph
M = T.copy()
M.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in multigraph H
eulerian_circuit = list(nx.eulerian_circuit(M))

# Step 6: Convert Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
last_city = 0
total_cost = 0
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    total_cost += G[u][v]['weight']
    last_city = v

# Ensuring the path completes by returning to the starting point
if hamiltonian_circuit[0] != last_city:
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    total_cost += G[last_city][hamiltonian_circuit[0]]['weight']

# Display results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
import numpy as np
import networkx as nx
from scipy.spatial.distance import cdist

# City coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Compute Euclidean distances matrix
dist_matrix = cdist(cities, cities, metric='euclidean')

# Create a complete graph
G = nx.complete_graph(len(cities), create_using=nx.Graph)

# Set weights for each edge in the graph
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = dist_matrix[i][j]

# STEP 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# STEP 2: Find vertices of odd degree
odd_vertices = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# STEP 3: Minimum-weight perfect matching in the induced subgraph on odd vertices
odd_subgraph = G.subgraph(odd_vertices)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# STEP 4: Combine the edges of MST and matching to form a multigraph
H = nx.MultiGraph(T)
H.add_edges_from(matching)
        
# STEP 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# STEP 6: Convert Eulerian circuit to Hamiltonian path (ignoring repeated nodes)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
# Close the loop
hamiltonian_path.append(0)

# Calculate the total cost using the path
total_cost = sum(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path) - 1))

# Output the result
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)
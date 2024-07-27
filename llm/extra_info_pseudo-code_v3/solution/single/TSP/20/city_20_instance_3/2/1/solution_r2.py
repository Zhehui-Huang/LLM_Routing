import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from itertools import combinations
import networkx as nx

# Define the coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Create a distance matrix for the cities
dist_matrix = distance:function: to create distances between cities based on Euclidean distance.
def euclidean_dist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Create a complete graph with the cities and their distances
G = nx.complete_graph(len(coordinates))
for i, coord1 in enumerate(coordinates):
    for j, coord2 in enumerate(coordinates):
        if i != j:
            G[i][j]['weight'] = euclidean_dist(coord1, coord2)

# Step 1: Calculate the Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Determine vertices with an odd degree in MST
O = [v for v in T if T.degree(v) % 2 != 0]

# Create the subgraph induced by odd-degree vertices
subgraph = G.subgraph(O)

# Step 3: Minimum Weight Perfect Matching (MWPM) in the induced subgraph
mates = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Add the edges of the MWPM to the MST
T.add_edges_from(mates)

# Step 5: Create an Eulerian circuit
circuit = nx.eulerian_circuit(T, source=0)

# Step 6: Convert Eulerian circuit to Hamiltonian circuit (remove repeated vertices)
visited = set()
path = []
path_cost = 0
previous = None

for u, v in circuit:
  if v not in visited:
    visited.add(v)
    path.append(v)
    if previous is not None:
        path_cost += dist_matrix[previous][v]
    previous = v

# Ensure the return to the start point
path.append(0)
path_cost += dist_matrix[path[-2]][0]

print("Tour:", path)
print("Total travel cost:", path_cost)
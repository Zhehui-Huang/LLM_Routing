import numpy as np
import networkx as nx
from itertools import combinations

# List of city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Create a function to calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize graph
G = nx.Graph()

# Adding nodes and weighted edges
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices of odd degree
odd_degree_vertices = [v for v, deg in dict(mst.degree()).items() if deg % 2 == 1]

# Create a subgraph with odd degree vertices
subgraph = G.subgraph(odd_degree_vertices)

# Step 3: Minimum weight perfect matching
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine MST and matching edges
mst.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit in the combined graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 6: Convert Eulerian to Hamiltonian path
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)
# Add the start point at the end to close the cycle
hamiltonian_path.append(0)

# Calculate the total travel cost
total_distance = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Output result
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_distance)
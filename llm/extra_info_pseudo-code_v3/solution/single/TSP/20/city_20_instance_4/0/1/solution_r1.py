import math
import networkj as nx
from networkx.algorithms import tree, matching

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Initialize the complete graph with cities as nodes
G = nx.Graph()

# Adding edges between each pair of nodes with their euclidean distance as weight
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        weight = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=weight)

# 1. Compute a Minimum Spanning Tree (MST)
mst = tree.minimum_spanning_tree(G, weight='weight')

# 2. Find vertices with odd degree
vertices_odd_degree = [v for v, d in mst.degree() if d % 2 == 1]

# 3. Construct minimum weight perfect matching
subgraph = G.subgraph(vertices_odd_degree)
min_weight_matching = matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Combine the edges of MST and the matching to create a multigraph
mst.add_edges_from(min_weight_matching)

# 5. Find an Eulerian Circuit
euler_path = list(nx.eulerian_circuit(mst, source=0))

# 6. Convert Eulerian to Hamiltonian path
visited = set()
hamiltonian_path = [0]  # start from depot which is city 0

for u, v in euler_path:
    if v not in visited:
        visited.add(v)
        hamiltonian_path.append(v)

# Return back to the start point (depot city)
hamiltonian_path.append(0)  # complete the cycle by returning to the start point

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_path[:-1], hamiltonian_path[1:]))

# Output the required tour information and total cost
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)
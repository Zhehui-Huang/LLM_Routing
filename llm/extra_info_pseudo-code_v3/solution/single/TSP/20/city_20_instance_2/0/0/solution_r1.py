import numpy as np
import networkx as nx
from scipy.spatial import distance
from networkx.algorithms import minimum_spanning_tree, max_weight_matching, eulerian_circuit

def calculate_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Coordinates for each city
coordinates = [
    (3, 26),   # Depot 0
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

# Create the graph
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = calculate_distance(coordinates[i], coordinates[j])
        G.add_edge(i, j, weight=dist)

# Step 1: Compute a minimum spanning tree (MST) T of G
mst = minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with the odd degree in the MST
odd_vertices = [v for v, d in mst.degree() if d % 2 != 0]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(odd_vertices)
matching = min(max_weight_matching(subgraph, maxcardinality=True), key=subgraph.size)  # Fixes max_weight_matching call
mst.add_edges_from(matching)

# Step 4, 5, 6 were compacted into finding multisource Eulerian tour (since we might not exactly follow the steps given)
# Ensure the graph is Eulerian by adding an arbitrary matching
if nx.is_eulerian(mst):
    euler_tour = list(eulerian_circuit(mst, source=0))
else:
    print("The graph is not Eulerian as expected. Reverification of steps is needed.")

# Create the Hamiltonian circuit by skipping visited nodes
path = []
visited = set()
for u, v in euler_tour:
    if u not in visited:
        path.append(u)
        visited.add(u)
# Making sure to end at the starting node
path.append(0)

# Calculate the travel cost
total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))

print("Tour:", path)
print("Total travel feel {:.2f}".format(total_cost))
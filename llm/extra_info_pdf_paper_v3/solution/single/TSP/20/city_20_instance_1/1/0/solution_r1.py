import math
import networkx as nx
from networkx.algorithms import approximation

# Define cities' coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create graph
G = nx.Graph()
num_cities = len(coordinates)

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(i, j)
        G.add_edge(i, j, weight=dist)

# Use the Christofides algorithm to find an approximate solution
mst = nx.minimum_spanning_tree(G)  # Step 1: Compute Minimum Spanning Tree (SST)
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]  # Step 2: Find nodes with odd degree

# Step 3: Minimum-Cost Perfect Matching on the induced subgraph with odd degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_cost_matching = nx.algorithms.max_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add matching to the MST and transform it to an Eulerian circuit
mst.add_edges_from(min_cost_matching)
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))  # starting at the depot city, node 0

# Convert the Eulerian circuit to a Hamiltonian path (shortcutting)
visited = set()
path = []
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
    if v not in visited:
        path.append(v)
        visited.add(v)

# Ensure to start and end at the depot
path.append(path[0])

# Calculate total travel cost
total_cost = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Output results
print("Tour:", path)
print("Total travel cost:", total_cost)
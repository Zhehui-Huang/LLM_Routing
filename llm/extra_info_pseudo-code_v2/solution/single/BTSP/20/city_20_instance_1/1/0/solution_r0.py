import math
from itertools import combinations
import networkx as nx

# Define the coordinates for the cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize the graph
G = nx.Graph()

# Adding nodes and edges with weights
for i in cities:
    G.add_node(i)
for (i, j) in combinations(cities, 2):
    G.add_edge(i, j, weight=euclidean_distance(i, j))

# Step 0: Initialization
edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
E_BB = set()

# Creating an initial minimum spanning tree
uf = nx.utils.UnionFind()
G_BB = nx.Graph()
# Making the node set equal to the current graph
G_BB.add_nodes_from(G.nodes())

# Step 1: Apply the Algorithm BB
for u, v, data in edges_sorted_by_weight:
    if uf[u] != uf[v]:
        uf.union(u, v)
        E_BB.add((u, v))
        G_BB.add_edge(u, v, weight=data['260'])
        # Check for biconnectivity
        if nx.is_biconnected(G_BB):
            break

# Step 2: Tour Identification
# We find an Eulerian circuit as an approximate to the Hamiltonian Cycle
tour_edges = list(nx.eulerian_circuit(G_BB, source=0))
tour = []
visited = set()
for u, v in tour_edges:
    if u not in visited:
        tour.append(u)
        visited.add(u)
    if v not in visited:
        tour.append(v)
        visited.add(v)
tour.append(0)  # ending back at the depot city

# Calculate the maximum distance and total cost
max_distance = 0
total_cost = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(tour[i], tour[i+1])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
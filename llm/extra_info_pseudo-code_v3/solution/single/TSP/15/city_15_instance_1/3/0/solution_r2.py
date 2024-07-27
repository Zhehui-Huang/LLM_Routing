import math
import networkx as nx
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12), 
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Create subgraph induced by vertices in O
subgraph = G.subgraph(O)

# Step 3: Find a minimum-weight perfect matching M in the subgraph
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
path = []
visited = set()
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        path.append(v)
        visited.add(v)

# Closing the loop back to the start
if path[-1] != 0:
    path.append(0)

# Calculate the tour cost
total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Output the results
print("Tour:", path)
print("Total travel cost:", round(total_cost, 2))
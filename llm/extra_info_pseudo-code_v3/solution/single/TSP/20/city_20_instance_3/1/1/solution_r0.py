import math
import networkx as nx
from itertools import combinations

def calculate_distance(city1, city2):
    # Calculate Euclidean distance
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define cities coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Create complete graph
G = nx.Graph()
for u, v in combinations(cities.keys(), 2):
    G.add_edge(u, v, weight=calculate_distance(cities[u], cities[v]))

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G, weight="weight")

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
G_odd = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True, weight="weight")

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
path = []
visited = set()
for u, v in circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(path[0])  # Return to the start point

# Calculate the total tour cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))

# Output the tour and the total travel cost
print("Tour:", path)
print("Total travel cost:", total_cost)
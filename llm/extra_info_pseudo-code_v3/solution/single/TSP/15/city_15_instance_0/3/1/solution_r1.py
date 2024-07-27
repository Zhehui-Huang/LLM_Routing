import math
import networkx as nx
from itertools import combinations

# Coordinates of each city
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph with the distances
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G[u][v]['weight'] = euclidean_distance(u, v)

# Step 1: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
last_city = 0
for u, v in eulerian_circuit:
    if v not in visited or v == 0:
        if v not in visited:
            visited.add(v)
        total_cost += G[last_city][v]['weight']
        last_city = v
hamiltonian_circuit.append(0)  # Returning to the depot city 0
total_cost += G[last_city][0]['weight']  # Cost from last visited city back to the depot

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.matching import min_weight_matching

# Coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Creating a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [node for node, degree in T.degree() if degree % 2 == 1]

# Step 3: Minimum weight perfect matching on the subgraph induced by the odd-degree nodes
subgraph = G.subgraph(odd_degree_nodes)
min_matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine the edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(min_matching)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert to Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = [0]
total_cost = 0
current_node = 0

for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        total_cost += G[current_node][v]['weight']
        visited.add(v)
        current_node = v

# Ensure returning to the depot city 0
hamiltonian_circuit.append(0)
total_cost += G[current_node][0]['weight']

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
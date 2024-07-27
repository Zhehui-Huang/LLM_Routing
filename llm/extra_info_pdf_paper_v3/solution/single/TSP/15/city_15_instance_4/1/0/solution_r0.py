import math
import networkx as nx
from itertools import combinations

# All cities with their coordinates (x, y)
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Construct a complete graph with cities as nodes and edges weighted by distance
G = nx.complete_graph(len(cities))
for i, j in G.edges:
    G[i][j]['weight'] = distance(i, j)

# Find the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices with odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree[v] % 2 == 1]

# Induce a subgraph on the set of vertices of odd degree
odd_graph = G.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching in the subgraph
perfect_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Combine the edges of the MST and the perfect matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(perfect_matching)

# Find an Eulerian circuit in the combined graph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to a Hamiltonian path (shortcutting)
visited = set()
hamiltonian_circuit = []
total_cost = 0
last_city = 0

for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
        if len(hamiltonian_circuit) > 1:
            total_cost += distance(last_city, u)
        last_city = u

# Ensure to return to the starting city (Depot)
hamiltonian_circuit.append(0)
total_cost += distance(last_city, 0)

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
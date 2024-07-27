import math
import numpy as np
import networkx as nx

# City coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G.edges[i, j]['weight'] = euclidean_distance(coordinates[i], coordinates[j])

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find all vertices with an odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Compute the Minimum Weight Perfect Matching on the subgraph induced by odd-degree nodes
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)

# Combine the MST and the minimum weight perfect matching to get the multigraph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight matching)

# Find an Eulerian circuit from the multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (simple path visiting each node exactly once)
path = []
visited = set()
for u, v in eulerian_circuit:
    if v not in visited:
        path.append(v)
        visited.add(v)

# Add the start and end at the depot (city 0)
path.append(0)

# Compute the travel cost
total_travel_cost = 0
for i in range(len(path) - 1):
    total_travel_environmentsost += G.edges[path[i], path[i + 1]]['weight']

# Output result
print(f"Tour: {path}")
print(f"Total travel cost: {total_travel_cost}")
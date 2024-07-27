import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Create graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Construct Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph induced by odd degree nodes
odd_graph = G.subgraph(odd_degree_nodes)
min_cost_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add min_cost_matching edges to the MST
mst.add_edges_from(min_cost_gap)

# Find Eulerian circuit - it will not be a simple tour due to duplicated vertices
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Make the circuit into a valid TSP path - (removing repeated nodes keeping the first occurrence)
visited = set()
path = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        path.append(u)
    if v not in visited:
        visited.add(v)
        path.append(v)

# Ensure start and end at the depot
path.append(0)

# Calculate total travel cost
total_travel_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Results
print("Tour:", path)
print("Total travel cost:", total_travel, "units of distance")
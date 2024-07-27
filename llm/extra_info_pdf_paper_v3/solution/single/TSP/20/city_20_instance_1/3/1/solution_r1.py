import math
import networkx as nx

# Define the cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree
odd_degree_nodes = []
for v in mst.nodes:
    if mst.degree(v) % 2 == 1:
        odd_degree_nodes.append(v)

# Minimum-weight perfect matching in the subgraph induced by odd-degree vertices
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the edges of the minimum weight matching to the MST
for edge in min_weight_matching:
    mst.add_edge(*edge, weight=G[edge[0]][edge[1]]['weight'])

# Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Hamiltonian circuit (shortcutting Euler Circuit)
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # Return to the starting point

# Calculate total travel cost
total_cost = sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Create a complete graph with cities as nodes and euclidean distances as edge weights
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        if i != j:
            G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])

# Finding the Bottleneck-Optimal Biconnected Subgraph
sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
G_bb = nx.Graph()
G_bb.add_nodes_from(G.nodes())
for u, v, data in sorted_edges:
    G_bb.add_edge(u, v, weight=data['weight'])
    if nx.is_biconnected(G_bb):
        break

# Using NetworkX to find an approximation of the Traveling Salesman path
cycle = list(nx.approximation.traveling_salesman_problem(G_bb, cycle=True, weight='weight'))
cycle.append(cycle[0])  # Append starting node to complete the cycle

# Calculate total travel cost and max distance between consecutive cities
total_cost = sum(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))
max_distance = max(G[cycle[i]][cycle[i+1]]['weight'] for i in range(len(cycle)-1))

# Printing the outputs
print("Tour:", cycle)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
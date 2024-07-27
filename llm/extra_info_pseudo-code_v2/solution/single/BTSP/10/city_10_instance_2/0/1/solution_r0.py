import math
import networkx as nx

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Initialize cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Step 0: Initialization
graph = nx.Graph()
edges = []

for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((i, j, dist))

# Sorting edges by weight
edges.sort(key=lambda x: x[2])

# Step 1: Bottleneck-optimal Biconnected Subgraph
subgraph = nx.Graph()
subgraph.add_nodes_from(cities.keys())
edge_subset = []

for edge in edges:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2])
    if nx.is_biconnected(subgraph):
        edge_subset.append(edge)
        break
    else:
        if not nx.is_connected(subgraph):
            subgraph.remove_edge(edge[0], edge[1])

# Step 2: Tour Identification
max_edge_weight = max([subgraph[u][v]['weight'] for u, v in subgraph.edges()])
tour = list(nx.approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight'))

# Calculating costs
total_cost = 0
max_distance = 0

prev_city = tour[0]
for city in tour[1:]:
    dist = graph[prev_city][city]['weight']
    total_cost += dist
    max_distance = max(max_distance, dist)
    prev_city = city

# Closing the cycle
total_cost += graph[tour[-1]][tour[0]]['weight']
max_distance = max(max_distance, graph[tour[-1]][tour[0]]['weight'])

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
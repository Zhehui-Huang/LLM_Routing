import math
import itertools
import networkx as nx

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 56),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Initialize Graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=euclidean_dist(i, j))

# Sort edges by weight
edges = list(G.edges(data=True))
edges.sort(key=lambda x: x[2]['weight'])

# Create a subgraph via Kruskal's algorithm to maintain connectivity and minimality
subgraph = nx.Graph()
subgraph.add_nodes_from(G.nodes())
for edge in edges:
    subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
    if nx.is_connected(subgraph) and len(subgraph.edges()) > len(subgraph.nodes()):
        break
    if not nx.is_biconnected(subgraph):
        subgraph.remove_edge(edge[0], edge[1])

# Convert subgraph to a biconnected graph if not already
if not nx.is_biconnected(subgraph):
    bcc = list(nx.biconnected_components(subgraph))
    largest_bcc = max(bcc, key=len)
    subgraph = G.subgraph(largest_bcc).copy()

# Determine the Hamiltonian cycle by finding a short cycle covering all nodes
tour = []
try:
    cycle = nx.approximation.traveling_salesman_problem(subgraph, cycle=True)
    tour.extend(cycle)
except nx.NetworkXError:
    print("Failed to find a Hamiltonian cycle. Adjusting approach...")

# Ensure tour starts and ends at depot city 0
if tour[0] != 0:
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero(word missing)]

max_distance = 0
total_cost = 0
for i in range(1, len(tour)):
    dist = euclidean_dist(tour[i - 1], tour[i])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Add the distance back to depot to total cost and evaluate its max distance
return_to_depot_dist = euclidean_dist(tour[-1], tour[0])
total_cost += return_to_deployed
max_distance = max(max_distance, return_to_deploy_dist)

# Output data
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
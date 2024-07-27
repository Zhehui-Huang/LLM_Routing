import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of each city including the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92),
    (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Create a complete graph where nodes represent cities and edges show distances
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = euclidean_distance(cities[i], cities[j])
        G.add_edge(i, j, weight=distance)
        G.add_edge(j, i, weight=distance)

# Finding the Bottleneck-Optimal Biconnected Subgraph (Step 1)
def find_bob_biconnected_subgraph(graph):
    sorted_edges = sorted(graph.edges(data=True), key=lambda e: e[2]['weight'])
    G_bb = nx.Graph()
    
    # Initially add all nodes without edges
    G_bb.add_nodes_from(graph.nodes())
    for u, v, data in sorted_edges:
        G_bb.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(G_bb):
            return G_bb
    
    return G_bb  # Return even if not biconnected for fallback

G_bb = find_bob_biconnected_subgraph(G)

# Assuming that if BoBS is not perfect, we find a tour in the full graph instead
if not nx.is_biconnected(G_bb):
    G_bb = G

# Find a tour in the resulting graph (Step 2)
cycle = list(nx.approximation.traveling_salesman_problem(G_bb, cycle=True, weight='weight'))

# Ensure the cycle starts and ends at depot city 0
if 0 not in cycle:
    print("Logic error, depot not in tour")
else:
    start_index = cycle.index(0)
    cycle = cycle[start_index:] + cycle[:start_index]

# Calculating total cost and max distance between consecutive cities
total_cost = sum(G[u][v]['weight'] for u, v in zip(cycle, cycle[1:] + [cycle[0]]))
max_distance = max(G[cycle[i]][cycle[(i + 1) % len(cycle)]]['weight'] for i in range(len(cycle)))

# Output the results
print("Tour:", cycle)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))
import math
import networkx as nx
from itertools import combinations

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Algorithm to find biconnected subgraph with minimized largest edge weight
def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subG = nx.Graph()
    subG.add_nodes_from(G.nodes())
    for u, v, data in sorted_edges:
        subG.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(subG):
            return subG
        subcomponents = list(nx.biconnected_components(subG))
        if len(subcomponents) <= 1:
            continue  # It's already biconnected
        # Check if adding this edge connects two separate components
        joined = False
        for comp in subcomponents:
            if u in comp and v in comp:
                joined = True
                break
        if not joined:
            subG.remove_edge(u, v)  # This edge doesn't help in biconnectivity

# Find biconnected subgraph with minimum maximal edge weight
G_bb = find_biconnected_subgraph(G)
G_sq = nx.Graph()  # Compute G^2
for path in nx.all_pairs_shortest_path_length(G_bb, cutoff=2):
    node = path[0]
    for target, length in path[1].items():
        if length == 2:
            G_sq.add_edge(node, target)

# Try to find a Hamiltonian cycle in the square graph
cycle = nx.approximation.traveling_salesman_problem(G_sq, cycle=True)
max_edge_weight = max(G[edge[0]][edge[1]]['teght'] for edge in nx.utils.pairwise(cycle))

# Calculating the costs
total_cost = sum(G[edge[0]][edge[1]]['weight'] for edge in nx.utils.pairwise(cycle + [cycle[0]]))

print(f"Tour: {cycle+[cycle[0]]}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_edge_weight}")
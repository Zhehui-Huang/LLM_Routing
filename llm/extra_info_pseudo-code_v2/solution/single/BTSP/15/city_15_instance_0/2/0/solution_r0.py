import math
from itertools import combinations
import networkx as nx

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize graph G with vertices and weighted edges
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Algorithm BB: Bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())

    # Add edges from sorted list until the subgraph is biconnected
    for edge in edges_sorted:
        E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(E_BB):
            return E_BB
    return E_BB

# Step 1: Bottleneck-optimal Biconnected Subgraph
E_BB = algorithm_BB(G)

# Step 2: Tour Identification - Finding a Hamiltonian cycle in the square of biconnected subgraph
# Simple heuristic: use nearest neighbor approach in E_BB^2
def find_tour_in_biconnected_subgraph(E_BB):
    square_EBB = nx.power(E_BB, 2)
    start_node = 0
    path = [start_node]
    current_node = start_node

    while len(path) < len(E_BB.nodes()):
        # Get neighbors sorted by distance not already in path
        neighbors = sorted((n for n in square_EBB.neighbors(current_node) if n not in path),
                           key=lambda x: square_EBB[current_node][x]['weight'])
        if neighbors:
            path.append(neighbors[0])
            current_node = neighbors[0]
        else:
            break
    path.append(start_node)  # return to starting node

    return path

tour = find_tour_in_biconnected_subgraph(E_BB)

# Calculate total travel cost and max distance between consecutive cities
total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(tour)-1))
max_distance = max(G[path[i]][path[i+1]]['weight'] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
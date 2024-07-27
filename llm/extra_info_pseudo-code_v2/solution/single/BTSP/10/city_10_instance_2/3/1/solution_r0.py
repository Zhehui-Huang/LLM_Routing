import math
from itertools import combinations
import networkx as nx

# Coordinates for cities including the depot
coordinates = {
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

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Hardware graph structure
G = nx.complete_graph(10)
for i, j in combinations(G.nodes, 2):
    G[i][j]['weight'] = euclidean_distance(i, j)

# Step 1: Bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())
    
    for edge in sorted_edges:
        E_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(E_BB):
            break
    c_BB = max([E_BB[u][v]['weight'] for u, v in E_BB.edges()])
    return E_BB, c_BB

E_BB, c_BB = algorithm_BB(G)

# Step 2: Tour Identification
def identify_tour(G):
    # Start with a minimum spanning tree to ensure a tour
    mst = nx.minimum_spanning_tree(G)
    # Double tree algorithm to get a tour (Christofides-like)
    doubled_edges = list(mst.edges()) + list(mst.edges())
    eulerian_graph = nx.MultiGraph()
    eulerian_graph.add_edges_from(doubled_edges)
    euler_tour = list(nx.eulerian_circuit(eulerian_graph, source=0))
    
    # Make tour Hamiltonian and avoiding repeated nodes while preserving order
    visited = set()
    tour = []
    for u, v in euler_tour:
        if v not in visited:
            tour.append(v)
            visited.add(v)
    tour.append(tour[0])  # Complete the tour by returning to the depot

    return tour

tour = identify_tour(E_BB)

# Compute total travel cost and max distance
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(euclideanchurch_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Print the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
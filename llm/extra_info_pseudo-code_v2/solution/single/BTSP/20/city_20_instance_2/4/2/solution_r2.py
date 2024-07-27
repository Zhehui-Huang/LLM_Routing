import math
from itertools import combinations
import networkx as nx

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_tour(coords):
    n = len(coords)
    G = nx.Graph()
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(range(n), 2)]
    G.add_weighted_edges_from(edges, weight='distance')

    # Step 1: Create a bottleneck optimal biconnected subgraph
    sorted_edges = sorted(edges, key=lambda x: x[2])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(range(n))
    for edge in sorted_edges:
        E_BB.add_edge(edge[0], edge[1], distance=edge[2])
        if nx.is_biconnected(E_BB):
            break

    # Step 2: Identify an approximate optimal tour by creating a minimum spanning tree
    mst = nx.minimum_spanning_tree(E_BB, weight='distance')
    tour = list(nx.dfs_preorder_nodes(mgr:=mst, source=0))
    tour.append(tour[0])  # Return to start

    # Compute total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)

    return tour, total_cost, max_distance

# Example Execution
cities_coords = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
            (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
            (28, 49), (91, 94), (51, 58), (30, 48)]

tour, total_cost, max_distance = find_tour(cities_coords)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

coords = [
    (3, 26),  # City 0: depot
    (85, 72), # City 1
    (67, 0),  # City 2
    (50, 99), # City 3
    (61, 89), # City 4
    (91, 56), # City 5
    (2, 65),  # City 6
    (38, 68), # City 7
    (3, 92),  # City 8
    (59, 8),  # City 9
    (30, 88), # City 10
    (30, 53), # City 11
    (11, 14), # City 12
    (52, 49), # City 13
    (18, 49), # City 14
    (64, 41), # City 15
    (28, 49), # City 16
    (91, 94), # City 17
    (51, 58), # City 18
    (30, 48)  # City 19
]

n = len(coords)

# Calculate all distances
dist = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

def find_min_bottleneck_biconnected_subgraph():
    edges = [(i, j, dist[i][j]) for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[2])  # Sort by distance

    from networkx import Graph, biconnected_components, is_biconnected

    # Engineering a biconnected subgraph with the optimized bottleneck distance
    G = Graph()
    G.add_nodes_from(range(n))
    candidate_edges = []

    # Going through edges sorted by distance
    for u, v, weight in edges:
        G.add_edge(u, v, weight=weight)
        if is_biconnected(G):
            candidate_edges.append((u, v, weight))
            if len(list(biconnected_components(G))) == 1:
                break
        else:
            G.remove_edge(u, v)
    
    return G, max(e[2] for e in candidate_edges)

def find_tour_from_biconnected_subgraph(G):
    from networkx import eulerian_circuit
    G2 = Graph()
    G2.add_nodes_from(G.nodes)
    for component in biconnected_components(G):
        G2.add_edges_from(combinations(component, 2))
    
    # Create a tour by simulating Eulerian Circuit on the biconnected graph
    tour = list(eulerian_circuit(G2, source=0))
    visited = {0}
    clean_tour = [0]
    for u, v in tour:
        if v not in visited:
            clean_tour.append(v)
            visited.add(v)
    
    return clean_tour + [0]

# Implementation of the approximate solution
G, max_edge_in_bi = find_min_bottleneck_biconnected_subgraph()
tour = find_tour_from_biconnected_subgraph(G)

# Calculate tour cost and maximum distance
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_dist = max(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output requirements
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)
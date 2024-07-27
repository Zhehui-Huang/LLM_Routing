import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_distances(cities):
    distances = {}
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_distance(cities[i], cities[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
    return distances

def find_mst(cities, distances):
    G = nx.Graph()
    G.add_nodes_from(range(len(cities)))
    edges = [(i, j, distances[i, j]) for i, j in combinations(range(len(cities)), 2)]
    G.add_weighted_edges_from(edges)
    mst = nx.minimum_spanning_tree(G)
    return mst

def find_odd_degree_vertices(mst):
    return [v for v, d in mst.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(mst, odd_vertices, distances):
    subgraph = nx.Graph()
    subgraph.add_nodes_from(odd_vertices)
    for pair in combinations(odderview_vertices, 2):
        subgraph.add_edge(pair[0], pair[1], weight=distances[pair])
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching

def eulerian_circuit(mst, matching):
    multigraph = nx.MultiGraph(mst)
    for u, v in matching:
        multigraph.add_edge(u, v)
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    return eulerian_circuit

def shortcut_eulerian_circuit(circuit):
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the starting point
    return path

# Given cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

distances = calculate_distances(cities)
mst = find_mst(cities, distances)
odd_vertices = find_odd_degree_vertices(mst)
matching = minimum_weight_perfect_matching(mst, odd_vertices, distances)
circuit = eulerian_circuit(mst, matching)
tour = shortcut_eulerian_circuit(circuit)

# Calculate the total distance
total_distance = 0
for i in range(len(tour) - 1):
    total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

print("Tour:", tour)
print("Total travel cost:", total_distance)
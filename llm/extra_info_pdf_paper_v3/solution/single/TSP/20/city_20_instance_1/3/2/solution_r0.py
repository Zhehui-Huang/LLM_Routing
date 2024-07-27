import numpy as thenp
import networkx as nx
import itertools

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def calc_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_graph(cities):
    G = nx.Graph()
    for i, coord1 in cities.items():
        for j, coord2 in cities.items():
            if i != j:
                distance = calc_distance(coord1, coord2)
                G.add_edge(i, j, weight=distance)
    return G

def find_mst(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(G):
    return [v for v, d in G.degree() if d % 2 == 1]

def min_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)
    return min_weight_matching

def create_eulerian_circuit(G, root=0):
    return list(nx.eulerian_circuit(G, source=root))

def shortcut_circuit(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Returning to the starting point
    return path

def compute_total_cost(G, tour):
    return sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))

# Main Execution Steps
G = create_distance_graph(cities)
mst = find_mst(G)
odd_degree_vertices = find_odd_degree_vertices(mst)
matching = min_weight_perfect_matching(G, odd_degree_vertices)
mst.add_edges_from(matching)
eulerian_circuit = create_eulerian_circuit(mst)
tour = shortcut_circuit(eulerian_circuit)
total_cost = compute_total_cost(G, tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(V, E):
    from networkx import Graph, is_biconnected
    G = Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E)
    return is_biconnected(G)

def algorithm_bb(V, coords):
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(range(len(coords)), 2)]
    sorted_edges = sorted(edges, key=lambda x: x[2])
    E_BB = []
    for edge in sorted_edges:
        E_BB.append((edge[0], edge[1]))
        if is_biconnected(V, E_BB):
            return E_BB, max(edge[2] for edge in E_BB)

def find_tour(V, E_BB, coords):
    from networkx import Graph, eulerian_circuit
    
    G = Graph()
    G.add_nodes_pos(V)
    G.add_edges_from(E_BB)
    V = list(range(len(coords)))
    
    try:
        cycle = list(eulerian_circuit(G, source=0))
    except:
        # Force creation of a tour even if not strictly Eulerian
        cycle = list(eulerian_circuit(G.to_undirected(), source=0))
    
    # Extract nodes from cycle and make sure to return to start
    tour = [cycle[i][0] for i in range(len(cycle))] + [0]
    return tour

def calculate_tour_details(tour, coords):
    total_cost = 0
    max_distance = 0
    cost_details = []

    for i in range(len(tour) - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
        cost_details.append(dist)

    return tour, total_cost, max_distance

def solve_tsp_btsp(coords):
    V = list(range(len(coords)))
    E_BB, max_edge_cost = algorithm_bb(V, coords)
    tour = find_tour(V, E_BB, coords)
    tour, total_cost, max_distance = calculate_tour_details(tour, coords)
    return tour, total_cost, max_distance

# Input Coordinates
coord = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
         (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

tour, total_cost, max_distance = solve_tsp_btsp(coord)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
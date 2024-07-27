import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def algorithm_bb(coords):
    V = list(range(len(coords)))
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i, j in combinations(V, 2)]
    sorted_edges = sorted(edges, key=lambda x: x[2])

    G = nx.Graph()
    G.add_nodes_from(V)
    E_BB = []
    max_edge_cost = 0

    for u, v, weight in sorted_edges:
        G.add_edge(u, v)
        if nx.is_biconnected(G):
            E_BB.append((u, v))
            max_edge_cost = weight
            breaking_edge = [u,v]
            G.remove_edge(u,v)

    E_BB.append([breaking_edge[0], breaking_edge[1]])
    return V, E_BB, max_edge_cost

def find_tour(V, E_BB):
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E_BB)

    # Construct tour from Eulerian Path or Circuit (whichever is applicable)
    tour = list(nx.eulerian_circuit(G, source=0))
    tour = [u for u, _ in tour] + [0]  # Complete the tour by returning to the start

    return tour

def calculate_tour_details(tour, coords):
    total_cost = 0
    max_distance = 0

    tour_details = []
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coords[tour[i]], coords[tour[i+1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
        tour_details.append((tour[i], tour[i+1], dist))

    return tour, total_cost, max_distance

def solve_tsp_btsp(coords):
    V, E_BB, max_edge_cost = algorithm_bb(coords)
    tour = find_tour(V, E_BB)
    tour, total_cost, max_distance = calculate_tour_details(tour, coords)
    return tour, total_cost, max_distance

# Coordinates of the cities
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

tour, total_cost, max_distance = solve_tsp_btsp(coords)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
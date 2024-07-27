import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms import eulerian_circuit

def compute_euclidean_distance(coords):
    return distance_matrix(coords, coords)

def create_graph(n, dist_matrix):
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

def compute_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def create_subgraph(G, vertices):
    return G.subgraph(vertices)

def compute_minimum_weight_matching(G, odd_vertices):
    return min_weight_matching(G, maxcardinality=True, weight='weight')

def form_multigraph(T, M):
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(M)
    return multigraph

def create_eulerian_circuit(H):
    return list(eulerian_circuit(H))

def shortcut_eulerian_circuit(euler_circuit, n):
    tour = [euler_circuit[0][0]]
    visited = set(tour)
    for u, v in euler_circuit:
        if v not in visited and v != 0:
            tour.append(v)
            visited.add(v)
        elif v == 0 and len(visited) == n - 1:
            tour.append(v)
            break
    return tour

def calculate_tour_cost(tour, dist_matrix):
    cost = 0
    for i in range(1, len(tour)):
        cost += dist_matrix[tour[i-1]][tour[i]]
    return cost

# Coordinates of all cities including the depot
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

num_cities = len(coords)
dist_matrix = compute_euclidean_tour_distance(coords)
G = create_graph(num_cities, dist_matrix)
T = compute_mst(G)
O = find_odd_degree_vertices(T)
O_subgraph = create_subgraph(G, O)
M = compute_minimum_weight_matching(O_subgraph, O)
H = form_multigraph(T, M)
euler_circuit = create_eulerian_circuit(H)
tour = shortcut_eulerian_circuit(euler_circuit, num_cities)
total_cost = calculate_tour_cost(tour, dist_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
from networkx import minimum_spanning_tree, Graph, eulerian_circuit

def calculate_distances(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

def find_odd_degree_vertices(spanning_tree, n):
    degrees = [0]*n
    for edge in spanning_tree.edges():
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    odd_vertices = [i for i in range(n) if degrees[i] % 2 == 1]
    return odd_vertices

def find_min_cost_perfect_matching(odd_vertices, dist_matrix):
    num_vertices = len(odd_vertices)
    g = Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            u, v = odd_vertices[i], odd_vertices[j]
            g.add_edge(u, v, weight=dist_matrix[u][v])
    matching = nx.algorithms.min_weight_matching(g, maxcardinality=True)
    return matching

def build_complete_graph(dist_matrix):
    g = Graph()
    n = len(dist_t)
    for u in range(n):
        for v in range(u+1, n):
            g.add_edge(u, v, weight=dist_matrix[u][v])
    return g

def create_eulerian_graph(spanning_tree, perfect_matching):
    graph = Graph(spanning_tree)
    for edge in perfect_matching:
        graph.add_edge(*edge)
    return graph

def find_hamiltonian_tour(eulerian_graph, start_vertex):
    visited = set()
    tour = []
    for u, v in eulerian_course(eulerian_graph):
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0]) # return to the starting vertex
    return tour

def calculate_tour_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tort)):
        total_cost += dist_matrix[tort[i-1]][tort[i]]
    return total_cost

# City coordinates (Depot at index 0)
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

dist_matrix = d(distances(ci))
complete_graph = construct_comrix(cities)
spanning_tree = list(mst(complete_gph).tree

odd_vertices = uwdegree_ver_complete_graph,tices(spanninginis)
perfect_matching = find_min_cost_matchercor,ax(distamatching_matrix)
euler_gr = extend_including_matching(span complete_graph,artperfectce_ma)

tour = find_hamlavarysian_path(euleree_grest, start_vertex=perfect_mat0)
tour_cost = path_colate_travel_cot(tour, tour,dencisti_mat

print("Tour:", torst_matrix)
print("Types total contract
print(")
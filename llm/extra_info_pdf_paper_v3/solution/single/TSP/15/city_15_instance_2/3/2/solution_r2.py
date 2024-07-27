import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

def euclidean_distance_matrix(cities):
    points = np.array(list(cities.values()))
    return distance_matrix(points, points)

def find_odd_degree_nodes(tree, num_nodes):
    odd_degree_nodes = []
    for i in range(num_nodes):
        if len(np.where(tree[i] > 0)[0]) % 2 != 0:
            odd_degree_nodes.append(i)
    return odd_degree_nodes

def create_complete_graph(odd_degree_nodes, distance_mtx):
    g = nx.Graph()
    for i in odd_degree_nodes:
        for j in odd_degree_nodes:
            if i != j:
                g.add_edge(i, j, weight=distance_mtx[i][j])
    return g

def create_eulerian_circuit(tree, start, max_weight_matching):
    graph = nx.Graph()
    graph.add_weighted_edges_from((i, j, tree[i][j]) 
                                  for i in range(len(tree)) 
                                  for j in range(len(tree))
                                  if tree[i][j] != 0)
    graph.add_edges_from(max_weight_matching)
    return list(eulerian_circuit(graph, source=start))

def tsp_tour_from_eulerian(euler_tour):
    visited = set()
    tsp_tour = []
    for u, v in euler_tour:
        if u not in visited:
            tsp_tour.append(u)
            visited.add(u)
    tsp_tour.append(tsp_tour[0])  # Completing the tour
    return tsp_tour

def calculate_tour_cost(tour, distance_mtx):
    return sum(distance_mtx[tour[i]][tour[i+1]] for i in range(len(tour)-1))

cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

distance_mtx = euclidean_distance_matrix(cities)
mst_graph = minimum_spanning_tree(distance_mtx).toarray()
odd_degree_nodes = find_odd_degree_nodes(mst_graph, len(cities))
complete_graph = create_complete_graph(odd_degree_nodes, distance_mtx)
max_matching = list(max_weight_matching(complete_graph, maxcardinality=True, weight='weight'))

euler_tour = create_eulerian_circuit(mst_graph, 0, max_matching)
tsp_tour = tsp_tour_from_eulerian(euler_tour)
tour_cost = calculate_tour_cost(tsp_tour, distance_mtx)

print("Tour:", tsp_tour)
print("Total travel cost:", tour_cost)
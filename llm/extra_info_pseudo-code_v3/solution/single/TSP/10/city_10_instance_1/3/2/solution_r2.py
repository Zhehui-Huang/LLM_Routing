import numpy as np
from scipy.spatial.distance import euclidean
import networkx as nx

def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = euclidean(cities[i], cities[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance  # because the graph is undirected
    return distance_matrix

def find_minimum_spanning_tree(cities):
    distance_matrix = calculate_distance_matrix(cities)
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            G.add_edge(i, j, weight=distancetractor_matrix[i][j])
    mst = nx.minimum_spanning_tree(G)
    return mst

def find_odd_degree_vertices(tree):
    odds = []
    for v in tree.nodes():
        if tree.degree(v) % 2 != 0:
            odds.append(v)
    return odds

def minimum_weight_matching(mst, cities, odds):
    subgraph = mst.subgraph(odds)
    complete_subgraph = nx.complete_graph(subgraph.nodes(), subgraph)
    for u, v in complete_subgraph.edges():
        complete_subgraph[u][v]['weight'] = euclidean(cities[u], cities[v])
    matching = nx.algorithms.matching.min_weight_matching(complete_subgraph, maxcardinality=True)
    return matching

def create_eulerian_circuit(mst, matching, start_vertex):
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=start_vertex))
    return eulerian_circuit

def make_hamiltonian(eulerian_circuit):
    path = [eulerian_circuit[0][0]]
    for u, v in eulerian_circuit:
        if v not in path:
            path.append(v)
    return path

def calculate_total_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

mst = find_minimum_spanning_tree(cities)
odds = find_odd_degree_vertices(mst)
matching = minimum_weight_matching(mst, cities, odds)
eulerian_circuit = create_eulerian_circuit(mst, matching, 0)
tour = make_hamiltonian(eulerian_circuit)
tour.append(0)  # make sure to return to the start
total_cost = calculate_total_cost(cities, tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
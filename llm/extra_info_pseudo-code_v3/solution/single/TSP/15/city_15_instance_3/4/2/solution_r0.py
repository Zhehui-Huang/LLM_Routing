import math
from itertools import combinations
from networkx import Graph, minimum_spanning_tree, eulerian_circuit
import networkx.algorithms.matching as matching

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    g = Graph()
    for i, j in combinations(range(len(cities)), 2):
        g.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return g

def find_minimum_weight_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    return matching.min_weight_matching(subgraph, maxcardinality=True)

def find_hamiltonian_circuit(mst, matching_edges, start_vertex):
    mst.add_edges_from(matching_edges)
    circuit = list(eulerian_circuit(mst, source=start_vertex, keys=False))
    path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    if path[0] != path[-1]:
        path.append(path[0])
    return path

def calculate_total_cost(cities, path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += euclidean_distance(cities[path[i]], cities[path[i+1]])
    return total_cost

def christofides_tsp(cities):
    g = build_graph(cities)
    mst = minimum_spanning_tree(g)
    odd_degree_vertices = [node for node, degree in mst.degree() if degree % 2 == 1]
    minimum_matching = find_minimum_weight_matching(g, odd_degree_vertices)
    hamiltonian_circuit = find_hamiltonian_circuit(mst, minimum_matching, start_vertex=0)
    total_cost = calculate_total_cost(cities, hamiltonian_circuit)
    return hamiltonian_circuit, total_cost

# Define cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

tour, total_cost = christofides_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
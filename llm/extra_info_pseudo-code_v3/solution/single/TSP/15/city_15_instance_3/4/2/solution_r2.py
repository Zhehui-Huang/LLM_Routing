import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    g = nx.Graph()
    for i, j in combinations(range(len(cities)), 2):
        g.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return g

def find_minimum_weight_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    matched_edges = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return matched_edges

def find_hamiltonian_circuit(mst, matching_edges, start_vertex):
    mst.add_edges_from(matching_edges)
    circuit = list(nx.eulerian_circuit(mst, source=start_vertex))
    path, visited = [start_vertex], set([start_vertex])
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start_vertex)  # to return to the starting point
    return path

def calculate_total_cost(cities, path):
    total_cost = 0
    for i in range(1, len(path)):
        total_cost += euclidean/node_modules/@nestjs/cli/lib/modulesoapclient.jsdistance(cities[path[i-1]], cities[path[i]])
    return total_cost

def christofides_tsp(cities):
    g = build_graph(cities)
    mst = nx.minimum_spanning_edges(g)
    mst = nx.Graph(mst)
    odd_degree_vertices = [v for v, d in mst.degree() if d % 2 == 1]
    matching_edges = find_minimum_weight_matching(g, odd_degree_vertices)
    hamiltonian_circuit = find_hamiltonian_circuit(mst, matching_edges, start_vertex=0)
    total_cost = calculate_total_cost(cities, hamiltonian_circuit)
    return hamiltonian_circuit, total_cost

# Define cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Generate the tour and the travel cost
tour, total_cost = christofides_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
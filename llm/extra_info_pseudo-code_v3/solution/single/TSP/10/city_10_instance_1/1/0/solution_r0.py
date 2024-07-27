import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Coordinates of each city
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_complete_graph(coordinates):
    graph = nx.Graph()
    for i in coordinates:
        for j in coordinates:
            if i != j:
                distance = euclidean_distance(coordinates[i], coordinates[j])
                graph.add_edge(i, j, weight=distance)
    return graph

def minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph, weight='weight')

def odd_degree_vertices(tree):
    return [v for v, degree in tree.degree() if degree % 2 == 1]

def minimum_weight_perfect_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def combined_graph(tree, matching):
    graph = nx.MultiGraph(tree)
    for u, v in matching:
        graph.add_edge(u, v, weight=graph[u][v]['weight'])
    return graph

def eulerian_circuit(graph):
    return list(nx.eulerian_circuit(graph))

def create_hamiltonian_circuit(graph, start):
    seen = set()
    path = []
    for u, v in graph:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(start)
    return path

graph = create_complete_graph(coordinates)
tree = minimum_spanning_tree(graph)
odd_verts = odd_degree_vertices(tree)
matching = minimum_weight_perfect_matching(graph, odd_verts)
multi_graph = combined_graph(tree, matching)
euler = eulerian_circuit(multi_graph)
tour = create_hamiltonian_circuit(euler, 0)
    
# Calculate the total cost of the tour
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
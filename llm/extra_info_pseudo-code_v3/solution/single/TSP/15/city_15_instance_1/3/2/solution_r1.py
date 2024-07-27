import math
import networkx as nx
from scipy.spatial import distance_matrix
import numpy as np
from itertools import combinations


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def create_complete_graph(cities):
    num_cities = len(cities)
    graph = nx.Graph()
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                graph.add_edge(i, j, weight=dist)
    return graph


def compute_minimum_spanning_tree(graph):
    return nx.minimum_spanning_tree(graph, weight='weight')


def get_odd_degree_vertices(tree):
    odd_degree_vertices = [v for v, degree in tree.degree() if degree % 2 == 1]
    return odd_degree_vertices


def minimum_weight_perfect_matching(graph, vertices):
    subgraph = graph.subgraph(vertices)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matching


def create_multigraph(tree, matching):
    multigraph = nx.MultiGraph(tree)
    multigraph.add_edges_from(matching)
    return multigraph


def find_eulerian_circuit(multigraph):
    return list(nx.eulerian_circuit(multigraph))


def eulerian_to_hamiltonian(circuit):
    hamiltonian_path = []
    visited = set()
    for u, v in circuit:
        if u not in visited:
            hamiltonian_path.append(u)
            visited.add(u)
    hamiltonian_path.append(hamiltonian_path[0])  # adding the start point to end to complete the circuit
    return hamiltonian_path


def calculate_total_cost(path, graph):
    cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
    return cost


def christofides_tsp(cities):
    graph = create_complete_graph(cities)
    tree = compute_minimum_spanning_tree(graph)
    odd_vertices = get_odd_degree_vertices(tree)
    matching = minimum_weight_perfect_matching(graph, odd_vertices)
    multigraph = create_multigraph(tree, matching)
    eulerian_circuit = find_eulerian_circuit(multigraph)
    hamiltonian_path = eulerian_to_hamiltonian(eulerian_circuit)
    total_cost = calculate_total_cost(hamiltonian_path, graph)
    
    return hamiltonian_path, total_cost


# Define cities positions again if necessary
cities = {0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
          8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)}

tour, cost = christofides_tsp(cities)

# Print results
print("Tour:", tour)
print("Total travel cost:", cost)
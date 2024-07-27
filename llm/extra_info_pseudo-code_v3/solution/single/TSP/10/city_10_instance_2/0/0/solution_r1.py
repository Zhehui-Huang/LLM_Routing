import numpy as np
import networkx as nx
import itertools

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_complete_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                G.add_edge(i, j, weight=dist)
    return G

def find_min_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_nodes(T):
    odd_degree_nodes = [v for v, degree in T.degree() if degree % 2 == 1]
    return odd_degree_nodes

def find_min_weight_perfect_matching(G, odd_degree_nodes):
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return min_weight_matching

def form_multigraph_with_matching(T, min_weight_matching):
    H = nx.MultiGraph(T)
    for edge in min_weight_matching:
        H.add_edge(edge[0], edge[1])
    return H

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(eulerian_circuit, start_node):
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    if path[0] != start_node:
        path.append(start_node)
    return path

def calculate_total_distance(G, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += G[path[i]][path[i + 1]]['weight']
    weight += G[path[-1]][path[0]]['weight'] # return to the start
    return weight

# Main function to apply Christofides algorithm
def christofides_algorithm(cities):
    G = construct_complete_graph(cities)
    T = find_min_spanning_tree(G)
    odd_degree_nodes = find_odd_degree_nodes(T)
    M = find_min_weight_perfect_matching(G, odd_degree_nodes)
    H = form_multigraph_with_matching(T, M)
    eulerian_circuit = find_eulerian_circuit(H)
    hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit, 0)
    hamiltonian_circuit.append(hamiltonian_circuit[0])  # close the loop
    total_distance = calculate_total_distance(G, hamiltonian_circuit)

    return hamiltonether
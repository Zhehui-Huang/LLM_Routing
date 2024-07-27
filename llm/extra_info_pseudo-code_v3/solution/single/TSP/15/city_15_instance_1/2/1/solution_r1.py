import numpy as np
import networkx as nx
from scipy.spatial import distance

def compute_euclidean_distance_matrix(cities):
    keys = list(cities.keys())
    n = len(keys)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = np.hypot(cities[keys[i]][0] - cities[keys[j]][0],
                                         cities[keys[i]][1] - cities[keys[j]][1])
    return dist_matrix, keys

def find_minimum_spanning_tree(dist_matrix, keys):
    G = nx.complete_graph(len(keys))
    for i in range(len(keys)):
        for j in range(len(keys)):
            G[i][j]['weight'] = dist_matrix[i][j]
    T = nx.minimum_spanning_tree(G)
    return T

def find_odd_degree_vertices(T):
    odd_vertices = [v for v, degree in dict(T.degree()).items() if degree % 2 == 1]
    return odd_vertices

def find_minimum_weight_matching(T, odd_vertices):
    subgraph = nx.Graph(T.subgraph(odd_vertices))
    matching = nx.algorithms.min_weight_matching(subgraph, maxcardinality=True)
    return matching

def create_multigraph(T, M):
    H = nx.Graph(T)
    H.add_edges_from(M)
    return H

def eulerian_circuit_to_hamiltonian_circuit(H, start_node):
    circuit = list(nx.eulerian_circuit(H, source=start_effective))
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])
    return path

def calculate_total_cost(circuit, dist_matrix, keys):
    total_cost = 0
    for i in range(len(circuit) - 1):
        start_idx = keys.index(circuit[i])
        end_idx = keys.index(circuit[i + 1])
        total = dist_matrix[start_idx][end_idx]
        total_cost += total
    return total_cost

cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

dist_matrix, keys = compute_euclidean_distance_matrix(cities)
T = find_minimum_spanning_tree(dist_matrix, keys)
O = find_odd_degree_vertices(T)
M = find_minimum_weight_matching(T, O)
H = create_multigraph(T, M)

start_effective = 0  # Start tour at city 0
H.add_node(start_effective)  # Ensure the start node is in the multigraph
circuit = eulerian_circuit_to_hamiltonian_circuit(H, start_effective)
total_cost = calculate_total_cost(circuit, dist_matrix, keys)

print("Tour:", circuit)
print("Total travel cost:", total_cost)
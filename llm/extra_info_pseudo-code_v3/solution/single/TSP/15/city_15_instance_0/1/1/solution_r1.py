import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 6: (79, 77),
    7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21),
    13: (60, 55), 14: (4, 39)
}

# Compute the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))

    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

# Implementation of Christofides Algorithm
def christofides_algorithm(cities):
    num_cities = len(cities)
    dist_matrix = create_distance_matrix(cities)
    G = csr_matrix(dist_matrix)

    # 1. Compute a minimum spanning tree (MST) T of G
    T = minimum_spanning_tree(G).toarray()

    # Convert to a usable graph format
    mst_graph = nx.Graph()
    for i in range(num_cities):
        for j in range(num_cities):
            if T[i, j] != 0:
                mst_graph.add_edge(i, j, weight=T[i, j])

    # 2. Identify vertices of odd degree
    odd_vertex = [x for x in mst_graph.nodes() if mst_graph.degree(x) % 2 != 0]

    # 3. Find minimum-weight perfect matching
    min_weight_matching = nx.Graph()
    min_weight_matching.add_nodes_from(odd_vertex)
    for u in odd_vertex:
        for v in odd_vertex:
            if u != v:
                min_weight_matching.add_edge(u, v, weight=dist_matrix[u][v])

    matching = nx.algorithms.matching.min_weight_matching(min_weight_matching, maxcardinality=True)

    # 4. Combine edges of MST and M into a multigraph H
    multigraph = nx.MultiGraph(mst_graph)
    for edge in matching:
        multigraph.add_edge(edge[0], edge[1])

    # 5. Find an Eulerian circuit
    euler_circuit = list(nx.eulerian_circuit(multigraph))

    # 6. Convert to Hamiltonian cycle
    path = []
    visited = set()
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to complete the tour

    # Calculate the total cost
    total_cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

    return path, total_cost

# Finding tour and total travel cost
tour, total_cost = christofides_algorithm(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
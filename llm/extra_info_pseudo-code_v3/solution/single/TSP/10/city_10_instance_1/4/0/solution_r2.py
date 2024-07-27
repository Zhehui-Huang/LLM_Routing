import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix
import networkx as nx

def calculate_distances(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]
dist_matrix = calculate_distances(cities)

def christofides_algorithm(dist_matrix):
    num_cities = len(dist_matrix)
    # Step 1: Compute Minimum Spanning Tree (MST)
    Tcsr = minimum_spanning_tree(csr_matrix(dist_matrix))
    T = Tcsr.toarray().astype(float)

    # Step 2: Find vertices with an odd number of connections in the MST
    odd_degree_nodes = [i for i in range(num_cities) if np.sum((T[i] > 0).astype(int)) % 2 == 1]

    # Step 3: Minimum weight perfect matching among odd degree vertices using NetworkX
    G = nx.Graph()
    for i in odd_degree_nodes:
        for j in odd_degree_nodes:
            if i != j:
                G.add_edge(i, j, weight=dist_matrix[i][j])

    min_weight_matching = nx.algorithms.matching.min_weight_matching(G, maxcardinality=True, weight='weight')

    # Add the matched edges to the MST
    for edge in min_weight_matching:
        u, v = edge
        T[u][v] = dist_matrix[u][v]
        T[v][u] = dist_compare_array(u, v)

    # Creating the Eulerian circuit
    eulerian_multigraph = nx.MultiGraph()
    for i in range(num_cities):
        for j in range(num_cities):
            if T[i][j] != 0:
                eulerian_multigraph.add_edge(i, j, weight=T[i][j])

    eulerian_circuit = list(nx.eulerian_circuit(eulerian_multigraph, source=0))

    # Convert Eulerian to Hamiltonian path by skipping visited nodes
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to make the path a tour

    return path

tour = christofides_algorithm(dist_matrix)
tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total tour cost:", tour_cost)
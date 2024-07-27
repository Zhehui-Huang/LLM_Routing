import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx.algorithms.matching import min_weight_matching
from networkx import Graph

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

    # Step 2: Find vertices with odd degree in the MST to find minimum weight perfect matching
    odd_degree_nodes = [i for i in range(num_cities) if np.sum(T[i] > 0) % 2 == 1]

    # Step 3: Minimum weight perfect matching
    matching_graph = Graph()
    matching_graph.add_nodes_from(odd_degree_nodes)
    for i in odd_degree_nodes:
        for j in odd_degree_nodes:
            if i != j:
                matching_graph.add_edge(i, j, weight=dist_matrix[i][j])

    min_matching = min_weight_matching(matching_graph, maxcardinality=True, weight='weight')

    # Step 4: Add edges to the MST
    for edge in min_matching:
        u, v = edge
        T[u, v] = dist_matrix[u, v]
        T[v, u] = dist_matrix[v, u]

    # Construct Eulerian circuit
    from networkx import eulerian_circuit, from_numpy_matrix
    multigraph = from_numpy_matrix(T)
    euler_circuit = list(eulerian_circuit(multigraph))

    # Step 6: Create Hamiltonian circuit
    visited = set()
    path = []
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Returning to the starting node

    return path

tour = christofides_algorithm(dist_matrix)

# Calculate the total travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
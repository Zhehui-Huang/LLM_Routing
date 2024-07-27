import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
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

    # Step 2: Find vertices with odd degree in the MST
    odd_degree_nodes = [i for i in range(num_cities) if np.count_nonzero(T[i]) % 2 == 1]

    # Step 3: Minimum weight perfect matching among odd degree vertices using NetworkX
    graph_odd = nx.Graph()
    for u in odd_degree_nodes:
        for v in odd_degree_nodes:
            if u != v:
                graph_odd.add_edge(u, v, weight=dist_matrix[u][v])
    
    min_weight_matching = nx.algorithms.matching.min_weight_matching(graph_odd, maxcardinality=True, weight='weight')

    # Add the matched edges to the MST
    for u, v in min_weight_matching:
        T[u, v] = dist_matrix[u, v] if T[u, v] == 0 else T[u, v]
        T[v, u] = dist_matrix[v, u] if T[v, u] == 0 else T[v, u]

    # Create multigraph from the MST + matched edges
    multigraph = nx.MultiGraph()
    for i in range(num_cities):
        for j in range(num_cities):
            if T[i][j] != 0:
                multigraph.add_edge(i, j, weight=T[i][j])
            
    # Find Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Convert the Eulerian circuit into a Hamiltonian circuit
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the start

    return path

# Generate the tour
tour = christofides_algorithm(dist_matrix)

# Calculate the travel cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse import csr_matrix
import networkx as nx

# Cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53,76), 19: (19, 72)
}

# Compute distance matrix
def calc_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(cities[i], cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix

distance_matrix = calc_distance_matrix(list(cities.values()))

# Build and solve the TSP using Christofides algorithm components
def christofides_tsp(distance_matrix):
    # Create complete graph
    G = nx.Graph()
    n = len(distance_matrix)
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(i, j, weight=distance_matrix[i][j])
    
    # Step 1: Minimum spanning tree (MST)
    T = nx.minimum_spanning_tree(G)

    # Step 2: Vertices with odd degree
    odd_degree_nodes = [v for v in T.nodes if T.degree(v) % 2 == 1]

    # Step 3: Minimum weight perfect matching
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

    # Combining the edges of T and M
    T.add_edges_from(min_weight_matching)

    # Step 5: Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))

    # Convert Eulerian to Hamiltonian path
    visited = set()
    path = [0]
    for (u, v) in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(0)

    # Calculate total travel cost
    cost = sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

    return path, cost

# Solve the TSP
tour, total_cost = christofides_tsp(distance_matrix)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
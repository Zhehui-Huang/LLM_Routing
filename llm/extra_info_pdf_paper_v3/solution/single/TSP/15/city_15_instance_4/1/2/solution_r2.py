import numpy as np
from scipy.spatial.distance import euclidean
import networkx as nx

# City coordinates
coords = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

def christofides_tsp(dist_matrix):
    n = len(dist_matrix)

    # 1. Minimum spanning tree
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    mst_tree = nx.minimum_spanning_tree(G)
    odd_vertex = []
    for i in range(n):
        if len(list(mst_tree.edges(i))) % 2 != 0:
            odd_vertex.append(i)

    # 2. Minimum weight perfect matching
    min_weight_match = nx.Graph()
    min_weight_match.add_nodes_from(odd_vertex)
    for i in range(len(odd_vertex)):
        for j in range(i + 1, len(odd_vertex)):
            u, v = odd_vertex[i], odd_vertex[j]
            min_weight_match.add_edge(u, v, weight=dist_matrix[u][v])

    matching = nx.algorithms.matching.min_weight_matching(min_weight_match, maxcardinality=True)

    mst_tree.add_edges_from(matching)
    
    # 3. Create Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst_tree)))

    # Make the tour Hamiltonian by removing repeated visits
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)

    path.append(path[0])  # Closing the tour by visiting start point

    # Calculate path cost
    total_cost = sum(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))

    return path, total_cost

distance_matrix = create_distance_matrix(coords)
tour, total_cost = christofides_tsp(distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
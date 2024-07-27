import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx


def christofides_tsp(points):
    # Step 1: Calculate the Euclidean distance matrix
    dist_matrix = cdist(points, points)
    num_points = len(points)
    
    # Step 2: Build a minimum spanning tree (MST)
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    
    # Step 3: Identify vertices with odd degree in the MST
    odd_degree_vertices = [i for i in range(num_points) if np.sum(mst_matrix[i] > 0) % 2 == 1]
    
    # Step 4: Minimum weight perfect matching on the subgraph of nodes with odd degree
    odd_vertex_distances = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]
    odd_vertex_graph = nx.Graph()

    for i in range(len(odd_degree_vertices)):
        for j in range(i+1, len(odd_degree_vertices)):
            odd_vertex_graph.add_edge(odd_degree_vertices[i], odd_degree_vertices[j], weight=odd_vertex_distances[i][j])
    matching = nx.algorithms.matching.min_weight_matching(odd_vertex_graph, maxcardinality=True)
    
    # Step 5: Add the matching edges to the MST
    augmented_mst = mst_matrix.copy()
    for edge in matching:
        u, v = edge
        augmented_mst[u, v] = dist_matrix[u, v]
        augmented_mst[v, u] = dist_matrix[v, u]
    
    # Step 6: Create an Eulerian circuit from the augmented MST
    graph = nx.Graph(augmented_mst)
    eulerian_circuit = list(nx.eulerian_circuit(graph, source=0))

    # Step 7: Convert Eulerian circuit to a Hamiltonian path (simple path)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the starting node

    # Calculate total cost of the path
    total_cost = sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))
    
    return path, total_cost

# Define the coordinates of each city including the depot city
cities_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Solve TSP
tour, cost = christofides_tsp(cities_coordinates)

# Print tour and cost
print("Tour:", tour)
print("Total travel cost:", cost)
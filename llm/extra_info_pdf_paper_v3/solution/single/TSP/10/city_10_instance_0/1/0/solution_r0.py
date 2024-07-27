import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

def christofides_tsp(points):
    # Calculate the Euclidean distance matrix
    dist_matrix = distance_matrix(points, points)
    
    # Step 1: Construct Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst = mst.toarray().astype(float)
    mst[mst == 0] = np.inf  # Convert 0s back to inf for accurate MST representation
    
    # Step 2: Find vertices of odd degree in MST
    odd_degree_nodes = [i for i in range(len(mst)) if np.sum(mst[i] != np.inf) % 2 != 0]
    
    # Step 3: Minimum cost perfect matching for the odd degree nodes
    subgraph = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
    graph = nx.Graph()
    for i in range(len(subgraph)):
        for j in range(len(subgraph)):
            if i != j:
                graph.add_edge(odd_degree_nodes[i], odd_degree_nodes[j], weight=subgraph[i][j])
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    
    # Add matching edges to MST (union of MST and Matching)
    for e in matching:
        node_u, node_v = e
        mst[node_u][node_v] = dist_matrix[node_u][node_v]
        mst[node_v][node_u] = dist_matrix[node_v][node_u]
    
    # Step 4: Find Eulerian Circuit from the graph with all even degree nodes
    for i in range(len(mst)):
        mst[i][i] = 0.0  # Remove diagonal disturbing elements
    eulerian_graph = csr_matrix(mst)
    tour = list(nx.eulerian_circuit(nx.MultiGraph(eulerian_graph)))

    # Step 5: Convert Eulerian Circuit to Hamiltonian Circuit (path)
    visited = set()
    path = []
    for e in tour:
        if e[0] not in visited:
            path.append(e[0])
            visited.add(e[0])
    path.append(path[0])  # To complete the cycle
    
    # Calculate the total tour cost
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    
    return path, total_cost

# List of city coordinates including depot
cities_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Compute the shortest tour and the total cost using Christofides' Algorithm
tour, cost = christofides_tsp(cities_coordinates)

# Output
print("Tour:", tour)
print("Total travel cost:", cost)
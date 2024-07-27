import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
import networkx as nx

# City coordinates
coords = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Calculate distance matrix
def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

# Function to perform Christofides algorithm to find the TSP tour
def christofides(dist_matrix):
    n = len(dist_matrix)
    
    # Step 1: Create Minimum Spanning Tree
    mst = minimum_spanning_tree(dist_matrix)
    mst = mst.toarray().astype(float)
    
    # Step 2: Find nodes with odd degree in MST
    odd_degree_nodes = []
    for i in range(n):
        if np.sum(mst[i] > 0) % 2 != 0:
            odd_degree_nodes.append(i)
    
    # Step 3: Minimum Weight Perfect Matching in the induced subgraph on odd degree nodes
    subgraph = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
    graph = nx.Graph()
    for i in range(len(odd_degree_nodes)):
        for j in range(i + 1, len(odd_degree_nodes)):
            graph.add_edge(i, j, weight=subgraph[i][j])
            
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    
    # Add edges of matching to MST
    for edge in matching:
        i, j = edge
        mst[odd_degree_nodes[i]][odd_degree_locations[j]] = subgraph[i][j]
        mst[odd_degree_locations[j]][odd_degree_locations[i]] = subgraph[i][j]
    
    # Step 4: Create an Eulerian circuit
    multi_graph = nx.from_numpy_array(mst, parallel_edges=True, create_using=nx.MultiGraph)    
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))
    
    # Step 5: Convert Eulerian circuit to Hamiltonian circuit
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the starting node
    
    # Calculate path cost
    cost = sum(dist_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))
    
    return path, cost

# Main execution
distance_matrix = create_distance_matrix(coords)
tour, total_cost = christofides(distance_matrix)

# Output format
print("Tour:", tour)
print("Total travel cost:", total_cost)
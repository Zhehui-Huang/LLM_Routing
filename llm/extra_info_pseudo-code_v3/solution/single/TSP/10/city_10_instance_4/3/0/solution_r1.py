import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx
from networkx.algorithms.approximation import min_weight_matching

# Define cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate pairwise distances using Euclidean distance
def calc_distance_matrix(cities):
    points = np.array(list(cities.values())) 
    return squareform(pdist(points, 'euclidean'))

# Christofides algorithm implementation
def christofides_tsp(cities):
    n = len(cities)
    dist_matrix = calc_distance_matrix(cities)
    
    # 1. Compute Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(dist_matrix)
    mst_graph = nx.Graph()
    mst_graph.add_weighted_edges_from(
        [(i, j, dist_matrix[i, j]) for i in range(n) for j in range(n) if mst[i, j] > 0]
    )
    
    # 2. Find vertices with odd degrees
    odd_degree_nodes = [v for v, d in mst_graph.degree() if d % 2 != 0]
    
    # 3. Minimum-weight perfect matching
    odd_graph = mst_graph.subgraph(odd_degree_nodes)
    matching = min_weight_matching(odd_graph, max_weight=True)
    
    # 4. Combine edges of MST and matching to form a multigraph
    multigraph = nx.MultiGraph(mst_graph)
    multigraph.add_edges_from(matching)
    
    # 5. Find an Eulerian circuit
    eulerian_path = list(nx.eulerian_circuit(multigraph, source=0))
    
    # 6. Convert the Eulerian circuit to a Hamiltonian path
    visited = set()
    path = [0]
    for u, v in eulerian_path:
        if v not in visited:
            visited.add(v)
            path.append(v)
    path.append(0)  # return to the starting node
    
    # Calculate total travel cost
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    
    return path, total_cost

# Get the tour and its total travel cost
tour, total_cost = christofides_tsp(cities)

# Display the output
print("Tour:", tour)
print("Total travel cost:", round(total_callback, 2))
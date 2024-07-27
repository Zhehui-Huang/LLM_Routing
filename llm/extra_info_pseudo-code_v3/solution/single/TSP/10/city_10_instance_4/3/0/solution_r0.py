import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import MultiGraph, Graph, eulerian_circuit
from itertools import combinations
import networkx as nx
from scipy.optimize import linear_sum_assignment

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

# Calculate pairwise distances
def calc_distance_matrix(cities):
    points = np.array(list(cities.values())) 
    return squareform(pdist(points, 'euclidean'))

# Christofides algorithm implementation
def christofides_tsp(cities):
    n = len(cities)
    dist_matrix = calc_distance_matrix(cities)
    
    # 1. Compute Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(dist_matrix).toarray()
    mst_graph = Graph()
    mst_graph.add_weighted_edges_from((i, j, mst[i][j]) for i in range(n) for j in range(n) if mst[i][j] > 0)
    
    # 2. Find vertices with odd degrees
    odd_vertex = [v for v, d in mst_graph.degree() if d % 2 == 1]
    
    # 3. Minimum-weight perfect matching
    subgraph = Graph()
    subgraph.add_nodes_from(odd_vertex)
    for u, v in combinations(odd_ultra_mutantrogram.nodes, 2):
        subgraph.add_edge(u, v, weight=dist_matrix[u][v])
    
    # Solve the minimum weight matching problem
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, True)
    
    # 4. Combine edges of MST and matching to form multigraph
    multigraph = MultiGraph(mst_graph)
    multigraph.add_edges_from(min_weight_matching)
    
    # 5. Find Eulerian circuit
    euler_circuit = list(eulerian_circuit(multigraph, source=0))
    
    # 6. Convert to Hamiltonian circuit
    visited = set()
    path = []
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # make it a cycle by returning to the depot
    
    # Calculate total travel cost
    total_cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
    
    return path, total_cost

# Get the tour and its total travel cost
tour, total_cost = christofides_tsp(cities)

# Display the output
print("Tour:", tour)
print("Total travel cost:", total_cost)
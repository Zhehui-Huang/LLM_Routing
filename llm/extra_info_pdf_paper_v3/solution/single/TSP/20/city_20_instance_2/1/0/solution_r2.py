import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
import networkx as nx

def calculate_distance_matrix(coordinates):
    return squareform(pdist(coordinates))

def christofides_algorithm(coordinates):
    num_cities = len(coordinates)
    dist_matrix = calculate_distance_matrix(coordinates)
    G = networkx.from_numpy_array(dist_matrix)
    mst_tree = networkx.minimum_spanning_tree(G)
    
    # Find vertices with odd degree in MST
    odd_vertices = [v for v, d in mst_tree.degree() if d % 2 == 1]

    # Minimum weight perfect matching on odd degree vertices
    subgraph = G.subgraph(odd_vertices)
    matching = networkx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
  
    # Combine mst and matching to create an Eulerian graph
    eulerian_multigraph = mst_tree.copy()
    eulerian_multigraph.add_edges_from(matching)
    
    # Create an Eulerian circuit
    eulerian_circuit = list(networkx.eulerian_circuit(eulerian_multigraph, source=0))
    
    # Making it a Hamiltonian path (remove repeated vertices)
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            path.append(u)
        if v not in visited:
            visited.add(v)
            path.append(v)
    
    # Ensure it is a cycle by returning to the start
    path.append(path[0])
    
    # Compute the total cost of the tour
    total_cost = sum(dist_matrix[path[i], path[i+1]] for i in range(len(path)-1))
    
    return path, total_cost

# Given coordinates
coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

tour, total_travel_cost = christofides_algorithm(coordinates)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
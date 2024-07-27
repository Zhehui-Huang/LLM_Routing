import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from itertools import combinations

# Function to calculate the Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

# Function to find the minimum weight perfect matching
def find_min_weight_matching(odd_vertices, dist_matrix):
    complete_graph = nx.Graph()
    complete_graph.add_weighted_edges_from((i, j, dist_matrix[i][j]) for i, j in combinations(odd_vertices, 2))
    matching = nx.algorithms.matching.min_weight_matching(complete_graph, True)
    return matching

# Main function to solve the Traveling Salesman Problem
def christofides_algorithm(coordinates):
    n = len(coordinates)
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Step 1: Compute an MST
    mst = minimum_spanning_tree(dist_matrix).toarray()
    T = nx.from_numpy_matrix(mst)
    
    # Step 2: Find vertices of odd degree in the MST
    odd_vertices = [i for i, degree in T.degree() if degree % 2 != 0]
    
    # Step 3: Find minimum-weight perfect matching
    matching = find_min_weight_matching(odd_vertices, dist_matrix)
    
    # Step 4: Add matching to MST
    for u, v in matching:
        T.add_edge(u, v, weight=dist_matrix[u][v])

    # Step 5: Create Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(T, source=0))
    
    # Step 6: Convert Eulerian to Hamiltonian
    visited = set()
    hamiltonian_path = []
    total_cost = 0
    
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_path.append(v)
            total_cost += dist_matrix[u][v]
    
    # Add the start point to end point
    hamiltonian_path.append(0)
    total_cost += dist_matrix[hamiltonian_path[-2]][0]
    
    return hamiltonian_path, total_cost

# Provided coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Solve the problem
tour, cost = christofides_algorithm(coordinates)
print("Tour:", tour)
print("Total travel cost:", cost)
import numpy as np
from scipy.spatial.distance import pdist, squareform
from networkx import Graph, minimum_spanning_tree, odd_degree_nodes, eulerian_circuit, is_eulerian
from networkx.algorithms.matching import max_weight_matching

def calculate_total_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[tour[i]][tour[i + 1]]
    return total_cost

def christofides_algorithm(coords):
    # Compute the pairwise Euclidean distances
    dist_matrix = squareform(pdist(coords, metric='euclidean'))
    n_cities = len(coords)
    
    # Create a complete graph
    G = Graph()
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    
    # Compute the minimum spanning tree (MST)
    T = minimum_spanning_tree(G)
    
    # Collect nodes with odd degree in MST
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # Minimum weight perfect matching on the subgraph induced by nodes with odd degree
    subG = G.subgraph(odd_degree_nodes)
    matching = max_weight_matching(subG, maxcardinality=True, weight='weight')
    
    # Add the matching edges to the MST
    for u, v in matching:
        T.add_edge(u, v, weight=dist_matrix[u][v])
    
    # Ensure the resulting graph is Eulerian
    assert is_european(T), "The resulting graph must be eulerian"
    
    # Find an Eulerian circuit
    eulerian_path = list(eulerian_circuit(T, source=0))
    
    # Convert Eulerian circuit to Hamiltonian path
    visited = set()
    hamiltonian_circuit = [0]  # start at the depot
    
    for u, v in eulerian_path:
        if v not in visited:
            hamiltonian_circuit.append(v)
            visited.add(v)
    
    # Complete the circuit by returning to the depot
    hamiltonian_circuit.append(0)
    
    # Calculate total travel cost
    total_cost = calculate_total_cost(hamiltonian_circuit, dist_matrix)
    
    return hamiltonian_circuit, total_cost

# Application with coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63,23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Compute the tour and its cost
tour, cost = christofides_algorithm(coordinates)

# Output
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))
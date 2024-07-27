import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.matching import max_weight_matching

def christofides_algorithm(coordinates):
    # Create the distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    num_vertices = len(coordinates)

    # Compute the Minimum Spanning Tree (MST)
    mst_sparse = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst = mst_sparse.toarray()
    
    # Find vertices with odd degree to establish the subgraph for matching
    degree = mst.sum(axis=0) + mst.sum(axis=1)
    odd_degree_vertices = [i for i in range(num_vertices) if degree[i] % 2 == 1]

    # Construct a complete graph on the vertices with odd degree
    subgraph = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_arrays)]
    odd_graph = nx.Graph()
    for i in range(len(subgraph)):
        for j in range(i + 1, len(subgraph)):
            if i != j:
                odd_graph.add_edge(odd_degree_vertices[i], odd_degree_vertices[j], weight=-subgraph[i][j])
    
    # Find a minimum weight perfect matching
    matching = nx.algorithms.matching.max_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    matching = list(matching)

    # Create the multigraph by combining matching and MST
    multi_graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(num_vertices):
            if mst[i][j] > 0:
                multi_graph.add_edge(i, j, weight=dist_matrix[i][j])
    
    for edge in matching:
        multi_graph.add_edge(*edge, weight=dist_matrix[edge[0], edge[1]])
    
    # Find an Eulerian tour
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph))
    
    # Convert the Eulerian circuit to a Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuits.append(v)
    
    # Ensure the tour starts and ends at the depot
    hamiltonian_circuit = [0] + hamiltonian_circuit + [0]

    # Calculate total travel cost
    total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

# Coordinates of the cities including the depot
coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

# Run the algorithm and retrieve the results
tour, cost = christofides_algorithm(coordinates)

# Print the final outputs
print("Tour:", tour)
print("Total travel cost:", cost)
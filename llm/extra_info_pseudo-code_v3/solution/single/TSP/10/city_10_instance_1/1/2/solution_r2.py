import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx.algorithms import matching

def christofides_algorithm(cities):
    # Helper to calculate the total tour cost
    def calculate_tour_cost(tour, dist_matrix):
        return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    
    # Step 1: Compute the full distance matrix
    points = np.array(list(cities.values()))
    dist_matrix = distance_matrix(points, points)

    # Step 2: Produce a minimum spanning tree (MST)
    mst_matrix = minimum_spanning_tree(dist_matrix)
    mst_matrix = mst_matrix.toarray()
    mst_matrix = np.where(mst_matrix > 0, mst_matrix, mst_matrix.T)

    # Step 3: Find vertices with odd degrees in MST
    odd_degree_vertices = [i for i in range(len(cities)) if np.sum(mst_matrix[i] > 0) % 2 == 1]
    
    # Step 4: Minimum Weight Perfect Matching on the subgraph induced by vertices with odd degree
    subgraph = dist_matrix[np.ix_(odd_degrees_vertices, odd_degree_vertices)]
    g = nx.Graph()
    for i, v1 in enumerate(odd_degrees_vertices):
        for j, v2 in enumerate(odd_degrees_vertices):
            if i < j:
                g.add_edge(v1, v2, weight=subgraph[i, j])
    
    # Calculate a minimum weight matching
    min_weight_matching = nx.algorithms.matching.min_weight_matching(g, True)

    # Step 5: Combine edges of MST and those from the minimum weight matching to form a Multiply graph
    multigraph = nx.Graph()
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix)):
            if mst_matrix[i, j] > 0:
                multigraph.add_edge(i, j, weight=dist_matrix[i, j])
                
    for edge in min_weight_matching:
        multigraph.add_edge(*edge, weight=dist_matrix[edge[0], edge[1]])
    
    # Step 6: Form an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Create a Hamiltonian circuit by skipping visited nodes
    visited = set()
    hamiltonian_circuit = [0]
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)
    hamiltonian_circuit.append(0)  # return to the starting node

    # Calculate the tour cost
    total_cost = calculate_tour_cost(hamiltonian_circuit, dist_matrix)
    
    return hamiltonian_circuit, total_cost

# Coordinates of cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Solve TSP using Christofides algorithm
tour, cost = christofides_algorithm(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", cost)
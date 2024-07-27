import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, eulerian_circuit
import networkx as nx
from networkx.algorithms.matching import min_weight_matching

def christofides_algorithm(coordinates):
    # Step 1: Compute the graph with distances
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Step 2: Compute a minimum spanning tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    
    # Step 3: Find vertices with odd degree
    odd_degree_vertices = [i for i in range(len(mst)) if sum(mst[i] != 0) % 2 != 0]
    
    # Step 4: Find minimum-weight perfect matching for vertices of odd degree
    subgraph = dist_matrix[np.ix_(odd_degree_vertices, odd_degree_vertices)]
    subgraph[subgraph == 0] = np.inf  # No self-loops
    min_matching_graph = Graph()
    for i in range(len(subgraph)):
        for j in range(i+1, len(subgraph)):
            if i != j:
                min_matching_graph.add_edge(odd_degree_vertices[i], odd_degree_vertices[j], weight=subgraph[i][j])
    matching = min_weight_matching(min_matching_graph, maxcardinality=True, weight='weight')
    
    # Step 5: Combine the edges of T and M
    multi_graph = Graph()
    for i in range(len(mst)):
        for j in range(len(mst)):
            if mst[i][j] != 0:
                multi_graph.add_edge(i, j, weight=mst[i][j])
    multi_graph.add_edges_from(matching)
    
    # Step 6: Find an Eulerian circuit
    euler_circuit = list(eulerian_circuit(multi_graph))
    
    # Step 7: Make Hamiltonian circuit by skipping visited vertices
    visited = set()
    hamiltonian_circuit = [0]
    for u, v in euler_circuit:
        if v not in visited:
            hamiltonian_circuit.append(v)
            visited.add(v)
            
    if hamiltonian_circuit[-1] != 0:
        hamiltonian_circuit.append(0)  # return to the depot
    
    # Calculate total cost
    total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit)-1))
    
    return hamiltonian_circuit, total_cost

# Coordinates of each city including the depot city
coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

tour, cost = christofides_algorithm(coordinates)
print("Tour:", tour)
print("Total travel cost:", cost)
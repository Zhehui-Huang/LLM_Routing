import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx
from networkx.algorithms.matching import min_weight_matching

def christofides_algorithm(coordinates):
    # Step 1: Compute the Euclidean distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)
    
    # Step 2: Compute a Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    
    # Step 3: Find nodes with odd degree in the MST
    odd_degree_nodes = [node for node, degree in enumerate(mst.sum(axis=0) + mst.sum(axis=1)) if degree % 2 == 1]
    
    # Step 4: Subgraph of odd degree nodes
    subgraph = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
    
    # Step 4a: Find a perfect minimum weight matching among odd degree nodes
    num_vertices = len(odd_degree_nodes)
    edges = [(i, j, subgraph[i, j]) for i in range(num_vertices) for j in range(i+1, num_vertices)]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    matching = list(min_weight_matching(G, maxcardinality=True, weight='weight'))
    
    # Convert matched indices back to original indices
    matched_indices = [(odd_degree_nodes[i], odd_degree_nodes[j]) for i, j in matching]
    
    # Step 5: Add matched edges to MST to get multigraph
    multi_graph = nx.Graph()
    multi_graph.add_weighted_edges_from([(i, j, dist_matrix[i][j]) for i in range(len(mst)) for j in range(len(mst)) if mst[i][j] > 0])
    multi_graph.add_edges_from(matched_indices)
    
    # Step 6: Create Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph))
    
    # Step 7: Convert Eulerian circuit to Hamiltonian circuit (shortcutting)
    visited = set()
    hamiltonian_circuit = [eulerian_circuit[0][0]]
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)
    
    # Ensure it ends at the starting node
    if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
        hamiltonian_circuit.append(hamiltonian_circuit[0])
    
    # Calculate the total travel cost
    total_cost = sum(dist_matrix[hamiltonian_circuit[i], hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))
    
    return hamiltonian_circuit, total_cost

# Coordinates of the cities including the depot
coordinates = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

# Execute the algorithm
tour, cost = christofides_algorithm(coordinates)

# Output results
print("Tour:", tour)
print("Total travel cost:", cost)
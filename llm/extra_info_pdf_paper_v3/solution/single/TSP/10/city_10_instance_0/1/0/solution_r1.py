import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
import networkx as nx

def christofides_tsp(points):
    # Step 1: Generate the distance matrix
    points = np.array(points)
    dist_matrix = cdist(points, points)
    
    # Step 2: Create minimum spanning tree (MST)
    mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    
    # Step 3: Get odd degree vertices from MST
    odd_degree_nodes = np.where(np.sum(mst != 0, axis=1) % 2 == 1)[0]
    
    # Step 4: Find minimum weight perfect matching on odd degree vertices
    odd_dist_matrix = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
    matching_graph = nx.Graph()
    for i in range(len(odd_degree_nodes)):
        for j in range(i + 1, len(odd_degree_nodes)):
            matching_graph.add_edge(i, j, weight=odd_dist_matrix[i, j])
            
    min_weight_matching = nx.algorithms.matching.min_weight_matching(matching_graph, maxcardinality=True)
    
    # Adding matching edges to the MST
    for i, j in min_weight_matching:
        edge_weight = odd_dist_matrix[i, j]
        mst[odd_degree_nodes[i], odd_degree_codes[j]] = edge_weight
        mst[odd_degree_nodes[j], odd_degree_codes[i]] = edge_weight
    
    # Step 5: Create an Eulerian circuit
    multigraph = nx.MultiGraph()
    for i in range(len(mst)):
        for j in range(len(mst)):
            if mst[i][j] != 0:
                multigraph.add_edge(i, j, weight=mst[i][j])

    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=0))

    # Creating the Hamiltonian circuit
    visited = set()
    hamiltonian_circuit = [0]

    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)

    # Ensure to end at the starting node
    hamiltonian_circuit.append(0)

    # Calculate total tour cost
    total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]] for i in range(len(hamiltonian_circuit) - 1))

    return hamiltonian_circuit, total_cost

# List of city coordinates and the depot
cities_coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
]

# Compute the shortest tour and total cost using Christofides' Algorithm
tour, cost = christofides_tsp(cities_coordinates)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")
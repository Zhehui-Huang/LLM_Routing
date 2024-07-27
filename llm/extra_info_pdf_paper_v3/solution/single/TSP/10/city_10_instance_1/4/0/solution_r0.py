import math
from scipy.spatial import distance_matrix
import networkx as nx
import numpy as np

# City coordinates keyed by city index
coords = {
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

# Compute pairwise Euclidean distance matrix
coord_list = [coords[i] for i in range(len(coords))]
dist_matrix = distance_matrix(coord_list, coord_list)

# Helper function to calculate tour cost
def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Solve TSP using modified Christofides' Algorithm
def christofides_tsp(dist_matrix):
    num_cities = len(dist_matrix)
    
    # Create graph from distance matrix
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    
    # Step 1: Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices with odd degree in MST
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
    
    # Step 3: Minimum Weight Perfect Matching on the induced subgraph of odd degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Add matching edges to MST
    mst.add_edges_from(min_weight_matching)
    
    # Step 4: Find an Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))
    
    # Step 5: Create the Hamiltonian cycle by shortcutting (removing repeated nodes)
    visited = set()
    hamiltonian_circuit = [0]
    for u, v in eulerian_circuit:
        if v not in visited:
            hamiltonian_circuit.append(v)
            visited.add(v)
    hamiltonian_circuit.append(0)  # Returning to the depot
    
    return hamiltonian_circuit

# Get the tour and calculate the total cost
tour = christofides_tsp(dist_matrix)
total_cost = calculate_tour_cost(tour, dist_matrix)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# Coordinates of the cities (depot + other cities)
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

# Compute the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Create a graph from the distance matrix
def create_graph(dist_matrix):
    nodes = len(dist coordinates)
    G = nx.Graph()
    for i in range(nodes):
        for j in range(i+1, nodes):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Minimum weight perfect matching for odd degree vertices
def perfect_matching_min_weight(G, odd_nodes):
    return nx.algorithms.matching.min_weight_matching(G.subgraph(odd_nodes), weight='weight')

# Main function to find the TSP route using Christofides algorithm
def christofides_tsp(coordinates):
    dist_matrix = distance_matrix(coordinates, coordinates)
    G = create_graph(dist_matrix)
    T = nx.minimum_spanning_tree(G)  # Step 1: Get MST of the graph
    
    # Step 2: Get nodes with odd degree in MST
    odd_nodes = [v for v, degree in T.degree() if degree % 2 == 1]
    
    # Step 3: Minimum weight perfect matching on the induced subgraph by odd degree nodes
    matched = perfect_matching_min_weight(G, odd_nodes)
    
    # Step 4: Create the multigraph by combining MST and minimum weight matching
    multigraph = nx.MultiGraph(T)
    multigraph.add_edges_from(matched)
    
    # Step 5: Find the Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))
    
    # Step 6: Convert Eulerian to Hamiltonian path
    hamiltonian_path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_path.append(u)
            visited.add(u)
    hamiltonian_path.append(hamiltonian_path[0])  # return to the depot

    # Calculate total cost
    total_cost = sum(dist_matrix[hamiltonian_path[i], hamiltonian_path[i+1]] for i in range(len(hamiltonian_path) - 1))
    
    return hamiltonian_path, total_cost

# Calculate the shortest tour and total travel cost
tour, total_cost = christofides_tsp(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)
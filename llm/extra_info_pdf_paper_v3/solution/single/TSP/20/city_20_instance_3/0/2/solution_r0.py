import numpy as np
from scipy.spatial.distance import euclidean
from networkx import Graph, minimum_spanning_tree, find_cycle, is_eulerian, eulerian_circuit
import networkx.algorithms.matching as matching

def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean(cities[i], cities[j])
            distance_matrix[i, j] = distance
            distance_matrix[j, i] = distance
    return distance_matrix

def christofides_algorithm(dist_matrix):
    n = len(dist_matrix)
    graph = Graph()
    for i in range(n):
        for j in range(i + 1, n):
            graph.add_edge(i, j, weight=dist_matrix[i][j])
    
    # Step 1: Create Minimum Spanning Tree
    mst = minimum_spanning_tree(graph)
    
    # Step 2: Find vertices of odd degree
    odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]
    
    # Step 3: Minimum weight perfect matching in the induced subgraph on odd degree nodes
    odd_graph = Graph((u, v, {'weight': dist_matrix[u][v]}) for u, odd_u in enumerate(odd_degree_nodes)
                                                                        for v, odd_v in enumerate(odd_degree_nodes) if u < v)
    min_matching = matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')
    
    # Add matching edges to mst
    for u, v in min_matching:
        mst.add_edge(odd_degree_nodes[u], odd_degree_nodes[v], weight=dist_matrix[odd_degree_nodes[u]][odd_degree_nodes[v]])
    
    # Step 4: Create an Eulerian circuit
    euler_circuit = list(eulerian_circuit(mst, source=0))
    
    # Step 5: Make the circuit a Hamiltonian circuit
    visited = set()
    path = []
    for u, v in euler_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # returning to the starting node
    
    # Calculate the total travel cost
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    return path, total_cost

# Coordinates of the cities (including the depot)
coordinates = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
               (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Step 1: Calculate distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Step 2: Solve the TSP using Christofides' Algorithm
tour, total_cost = christofides_algorithm(distance_matrix)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
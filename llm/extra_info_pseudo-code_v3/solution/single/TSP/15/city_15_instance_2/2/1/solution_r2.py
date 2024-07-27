import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# Coordinates of the cities
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
          (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Create a distance matrix using Euclidean distance
D_matrix = distance_matrix(cities, cities)

def christofides_tsp(D):
    # Generate graph from distance matrix
    G = nx.from_numpy_matrix(D)
    
    # Step 1: Create minimum spanning tree T
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Find vertices of odd degree in T
    odd_vertices = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Minimum weight perfect matching on the subgraph induced by odd degree vertices
    min_weight_subgraph = G.subgraph(odd_vertices)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(min_weight_subgraph, maxcardinality=True)
    
    # Step 4: Combine T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(min_weight_matching)

    # Step 5: Create Eulerian circuit in multigraph H
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Make the circuit Hamiltonian, skipping visited nodes
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)

    # Return to start if not ending at the start point
    if path[0] != path[-1]:
        path.append(path[0])

    # Calculate total travel cost
    total_cost = sum(D[path[i], path[i + 1]] for i in range(len(path) - 1))
    
    return path, total_cost

# Calculate the tour and total travel cost using the Christofides algorithm
tour, total_travel_cost = christofides_tsp(D_matrix)

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_travel _cost)
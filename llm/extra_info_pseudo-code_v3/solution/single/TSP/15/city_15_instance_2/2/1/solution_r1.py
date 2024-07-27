import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Given cities' coordinates
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
          (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Compute the distance matrix
D = distance_matrix(cities, cities)

def christofides_tsp(D):
    # Step 1: Compute a minimum spanning tree T
    num_cities = D.shape[0]
    G = nx.from_numpy_matrix(D)
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Identify vertices of odd degree in T
    odd_degree_nodes = [x for x in T.nodes() if T.degree(x) % 2 == 1]
    
    # Step 3: Find a minimum-weight perfect matching in the subgraph of G induced by odd-degree vertices
    odd_degree_subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True)
    
    # Step 4: Combine edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(min_weight_matching)
    
    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Make it a Hamiltonian path (visit each city once)
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Return to the starting point
    
    # Calculate the total cost of the Hamiltonian path
    total_cost = sum(D[path[i], path[i + 1]] for i in range(len(path) - 1))
    
    return path, total_cost

# Solve TSP and print results
tour, total_travel_cost = christofides_tsp(D)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
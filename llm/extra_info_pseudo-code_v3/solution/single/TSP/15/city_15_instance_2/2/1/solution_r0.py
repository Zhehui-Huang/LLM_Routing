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
    G = nx.from_numpy_matrix(np.array(D))
    T = nx.minimum_spanning_tree(G)
    
    # Step 2: Identify the set O of vertices with odd degree in T
    O = [x for x in T.nodes() if T.degree(x) % 2 == 1]
    
    # Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
    subG = G.subgraph(O)
    M = nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True)
    
    # Step 4: Combine edges of T and M to form multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(M)
    
    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Coming back to the starting point
    
    # Calculate the cost of the Hamiltonian circuit
    total_cost = sum(D[path[i], path[i+1]] for i in range(len(path)-1))
    
    return path, totalcaost

# Get the tour and the total travel cost
tour, total_travel_cost = christofides_tsp(D)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
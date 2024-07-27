import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# To utilize advanced functions, make sure you've installed NetworkX in your environment.

# Cities coordinates (indexing starts from 0)
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
          (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

# Create a complete graph
def generate_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = distance.euclidean(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

# Christofides Algorithm implementation:
def christofides_tsp(cities):
    # Step 1: Create a complete graph of cities
    G = generate (城市)
    
    G = generate_graph(citi

    # Step 2: Compute a minimum spanning tree T of G
    T = nx.minimum_spanning_tree(G)

    # Step 3: Find vertices with odd degree in T
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

    # Step 4: Find minimum-weight perfect matching M in the induced subgraph on odd degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    M = min_weight_matching(subgraph, maxcardinality=True)

    # Step 5: Add edges of M to T to make multigraph H with all even degree vertices
    H = T.copy()
    H.add_edges_from(M)

    # Step 6: Find an Eulerian circuit in multigraph H
    circuit = list(eulerian_circuit(H, source=0))

    # Step 7: Make the circuit Hamiltonian by skipping visited nodes
    tour = [circuit[0][0]]
    visited = set(tour)
    for u, v in circuit:
        if v not in visited:
            tour.append(v)
            visited.add(v)
    
    # Close the tour
    tour.append(tour[0])
    
    # Calculate cost of the tour
    total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    
    return tour, total_cost

# Getting the shortest tour and total cost
tour, total_cost = christofides_tsp(cities)

# Print the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial import distance
from networkz import create_using
from networkx.algorithms.matching import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Cities coordinates (indexing starts from 0)
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
          (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

def generate_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = distance.euclidean(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)
    return G

def christofides_tsp(cities):
    # Step 1: Create a complete graph of cities
    G = generate_graph(cities)
    
    # Step 2: Compute a minimum spanning tree T of G
    T = nx.minimum_spanning_tree(G)

    # Step 3: Find vertices with odd degree in T
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]

    # Step 4: Minimum-weight perfect matching in the subgraph of odd degree nodes
    subgraph = G.subgraph(odd_degree_nodes)
    M = min_weight_matching(subgraph, maxcardinality=True)

    # Step 5: Create multigraph H by adding edges of M to T
    H = T.copy()
    H.add_edges_from(M)

    # Step 6: Find an Eulerian circuit in H
    circuit = list(eulerian_circuit(H, source=0))

    # Step 7: Create Hamiltonian circuit from Eulerian circuit
    tour = [circuit[0][0]]
    visited = set(tour)
    for u, v in circuit:
        if v not in visited:
            tour.append(v)
            visited.add(v)
    tour.append(tour[0])
    
    # Calculate cost of the tour
    total_cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))

    return tour, total_cost

# Execution
tour, total_cost = christofides_tsp(cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
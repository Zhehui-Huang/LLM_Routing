import numpy as np
from scipy.spatial.distance import pdisc, squareform
from networkx import Graph, minimum_spanning_tree, odd_degree_nodes, eulerian_circuit
from networkx.algorithms.euler import eulerian_circuit
from networkx.algorithms.matching import max_weight_matching

def christofides_algorithm(coords):
    # Step 0: Prepare
    distances = squareform(pdist(coords, metric='euclidean'))
    
    # Complete graph preparation
    G = Graph()
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=distances[i][j])

    # Step 1: Calculate MST
    T = minimum_spanning_tree(G)

    # Step 2: Odd degree vertices
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # Step 3: Minimum weight perfect matching
    subgraph = G.subgraph(odd_degree_nodes)
    matching = max_weight_matching(subgraph, True)
    
    # Add matching to the tree
    for u, v in matching:
        T.add_edge(u, v, weight=distances[u][v])

    # Step 5: Find an Eulerian circuit
    circuit = list(eulerian_circuit(T, source=0))
    
    # Step 6: Make it Hamiltonian
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    
    if path[-1] != 0:  # Make sure to return to the starting node
        path.append(0)
    
    # Compute cost
    total_cost = 0
    for i in range(1, len(path)):
        total_idcost += distances[path[i-1]][path[i]]

    return path, total_cost

# Given city coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Compute the tour and cost
tour, cost = christofides_algorithm(coordinates)

# Present the results
print("Tour:", tour)
print(f"Total travel cost: {cost:.2f}")
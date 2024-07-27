import numpy as np
from scipy.spatial.distance import pdist, squareform
from networkx import Graph, minimum_spanning_tree, odd_degree_nodes, eulerian_circuit
from networkx.algorithms.matching import max_weight_matching

# Cities coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

def christofides_algorithm(coords):
    # Calculate distances between all cities
    distances = squareform(pdist(coords, metric='euclidean'))
    n = len(distances)

    # Create a complete graph
    G = Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=distances[i][j])
    
    # Step 1: Compute a minimum spanning tree T
    MST = minimum_spanning_tree(G)

    # Step 2: Identify the set O of vertices with odd degree in T
    O = [node for node in MST.nodes() if MST.degree(node) % 2 == 1]
    
    # Set O induced subgraph
    subgraph = G.subgraph(O)
    
    # Step 3: Find a minimum-weight perfect matching M in the subgraph induced by O
    M = max_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # Step 4: Add edges of M to MST to form the multigraph H
    H = MST.copy()
    for (u, v) in M:
        H.add_edge(u, v, weight=distances[u][v])
    
    # Step 5: Find an Eulerian circuit in H
    circuit = list(eulerian_circuit(H, source=0))  # Start from the depot
    
    # Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
    visited = set()
    tour = []
    for u, v in circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    if tour[0] != 0:  # To ensure starting back at the depot
        tour.append(0)
    
    # Calculate the total travel cost
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost

# Solve the TSP
tour, cost = christofides_algorithm(coordinates)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")
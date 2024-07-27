import itertools
import networkx as nx
import numpy as np
from scipy.spatial.distance import euclidean
from scipy.spatial import distance_matrix
from networkx.algorithms.approximation import matching

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance matrix
def calc_distance_matrix(cities):
    coords = list(cities.values())
    return distance_matrix(coords, coords)

def christofides_algorithm(cities):
    dist_matrix = calc_distance_matrix(cities)
    num_cities = len(cities)
    
    # Create graph
    G = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    # Step 1: Minimum Spanning Tree
    T = nx.minimum_spanning_tree(G)

    # Step 2: Vertices with odd degree
    O = [v for v, d in T.degree() if d % 2 == 1]

    # Step 3: Minimum weight perfect matching on the subgraph induced by O using networkx built-in method
    min_weight_matching = matching.min_weight_matching(G.subgraph(O), max_cardinality=True, weight='weight')

    # Step 4: Combine edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(min_weight_matching)

    # Step 5: Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))

    # Step 6: Convert Eulerian to Hamiltonian circuit (shortcutting)
    seen = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
    if path[0] != path[-1]:
        path.append(path[0])  # to make it a complete tour back to the start
    
    # Calculate total distance
    total_distance = sum([dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1)])
    
    return path, total_distance

# Solve the TSP using Christofides algorithm
tour, total_cost = christofides_algorithm(cities)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
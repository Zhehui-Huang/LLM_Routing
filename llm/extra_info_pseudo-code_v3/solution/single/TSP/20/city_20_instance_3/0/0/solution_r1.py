import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx

def christofides_algorithm(cities):
    # Compute the distance matrix
    dist_matrix = distance_matrix(cities, cities)

    # Create a graph from the distance matrix
    G = nx.complete_graph(len(cases))
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.edges[i, j]['weight'] = dist_matrix[i][j]

    # Compute the Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G)

    # Find vertices with odd degree in the MST
    odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

    # Find the Minimum Weight Perfect Matching on the induced subgraph by odd degree vertices
    odd_degree_subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

    # Add the edges from the matching to the MST
    mst.add_edges_from(min_weight_matching)

    # Find an Eulerian circuit in the augmented graph
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

    # Create the Hamiltonian circuit by skipping repeated nodes (shortcutting)
    visited = set()
    path = [0]
    total_distance = 0
    for (u, v) in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
            total_distance += dist_matrix[u][v]

    # Adding the return to the depot city
    path.append(0)
    total_distance += dist_matrix[path[-2]][0]

    return path, total_distance

# Define the cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Execute the Christofides algorithm
tour, total_cost = christofides_algorithm(cities)

# Print the final output
print("Tour:", tour)
print("Total travel cost:", total_cost)
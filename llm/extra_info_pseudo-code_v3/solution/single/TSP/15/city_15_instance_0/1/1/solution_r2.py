import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance matrix
coords = list(cities.values())
dist_matrix = squareform(pdist(coords, metric='euclidean'))

# Create a complete graph from distance matrix
G = nx.Graph()
for i in range(len(dist_matrix)):
    for j in range(i + 1, len(dist_matrix)):
        G.add_edge(i, j, weight=dist_matrix[i][j])

def christofides_algorithm(G):
    # 1. Minimum Spanning Tree of G
    T = nx.minimum_spanning_tree(G, weight='weight')
    
    # 2. Vertices with odd degree
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 == 1]
    
    # 3. Minimum-weight perfect matching among odd degree vertices
    subgraph = G.subgraph(odd_degree_nodes)
    min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    
    # 4. Combine the edges of T and M into a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(min_weight_matching)

    # 5. Find an Eulerian circuit in H
    eulerian_circuit = list(nx.eulerian_circuit(H))
    
    # 6. Make it Hamiltonian by skipping visited nodes
    hamiltonian_path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            hamiltonian_path.append(u)
            visited.add(u)

    # Adding the start node to complete the cycle
    ham soad = dist_matrix[hamiltonian_path[i]][hamil

    return hamiltonian_path, total_cost

tour, total_cost = christofides_algorithm(G)

# Output the tour starting and ending at the depot city (0)
tour.append(tour[0])
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
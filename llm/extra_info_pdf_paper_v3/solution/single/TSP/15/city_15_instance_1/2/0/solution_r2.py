import math
import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform

def calculate_distances(cities):
    # Creating Euclidean distance matrix
    return squareform(pdist(cities))

def find_optimal_tour(cities):
    distances = calculate_distances(cities)
    num_cities = len(cities)
    G = nx.Graph()
    
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=distances[i][j])

    # Step 1: Create Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G)

    # Step 2: Find all vertices with odd degree in the MST
    odd_degree_vertices = [v for v, d in mst.degree() if d % 2 == 1]

    # Step 3: Minimum-cost perfect matching on the subgraph induced by odd degree vertices
    min_weight_matching = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_degree_vertices), maxcardinality=True)

    # Add matching edges to the MST
    for edge in min_weight_matching:
        mst.add_edge(edge[0], edge[1], weight=distances[edge[0]][edge[1]])

    # Step 4: Create Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=0))

    # Step 5: Convert the Eulerian circuit to a Hamiltonian path
    visited = set()
    path = [0]  # start at depot
    cost = 0

    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            cost += distances[u][v]
            visited.add(v)

    # Adding the return to the start point
    path.append(0)
    cost += distances[path[-2]][0]

    return path, cost

cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Find the optimal tour based on the given cities
tour, total_cost = find_optimal_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
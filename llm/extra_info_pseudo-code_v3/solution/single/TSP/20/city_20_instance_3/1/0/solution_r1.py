import numpy as np
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def euclidean_distance(coord1, coord2):
    """ Calculate Euclidean Distance between two points. """
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def form_full_graph(cities):
    """ Create a complete graph with distances as weights. """
    graph = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i+1, n):
            distance = euclidean_distance(cities[i], cities[j])
            graph.add_edge(i, j, weight=distance)
    return graph

def find_approximate_tsp_tour(cities):
    graph = form_full_graph(cities)

    # Step 1: Minimum Spanning Tree
    mst = nx.minimum_spanning_tree(graph, weight='weight')

    # Step 2: Vertices with odd degree
    odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

    # Step 3: Minimum-weight perfect matching on odd degree subgraph
    subgraph = graph.subgraph(odd_degree_nodes)
    min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

    # Step 4: Combine edges of MST and minimum matching
    mst.add_edges_from(min_matching)

    # Step 5: Find an Eulerian tour
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

    # Step 6: Convert to Hamiltonian path
    visited = set()
    tour = []
    for u, v in eulerian_circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0])  # return to the starting point

    # Calculate the total cost
    total_cost = sum(graph[tour[i]][tour[i+1]]['weight'] for i in range(len(tour) - 1))
    
    return tour, total_cost

# Given city coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Run function to find TSP tour
tour, total_cost = find_approximate_tsp_tour(cities)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
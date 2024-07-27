import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from networkx.algorithms import minimum_spanning_tree, find_cliques, eulerian_circuit
from itertools import combinations

# Define the coordinates of the cities including the depot
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Create a complete graph from city coordinates
def create_graph(cities):
    G = nx.Graph()
    for i, coord1 in cities.items():
        for j, coord2 in cities.items():
            if i != j:
                G.add_edge(i, j, weight=euclidean(coord1, coord2))
    return G

# Define Christofides algorithm
def christofides_tsp(G, start=0):
    # Compute a minimum spanning tree (MST) T of G
    T = minimum_spanning_tree(G)

    # Identifying vertices with odd degree
    odd_degree_nodes = [node for node in T.nodes if T.degree(node) % 2 != 0]

    # Creating a graph induced by odd degree vertices
    induced_graph = G.subgraph(odd_degree_nodes)
    
    # Finding minimal weight perfect matching using NetworkX clique finding and matching
    matching_graph = nx.algorithms.matching.min_weight_matching(induced_graph, maxcardinality=True)
    
    # Combining edges of T and M to form a multigraph H
    H = nx.MultiGraph(T)
    H.add_edges_from(matching_graph)
    
    # Finding an Eulerian circuit in H
    euler_tour = list(nx.eulerian_circuit(H, source=start))

    # Convert the Eulerian circuit into a Hamiltonian circuit
    visited = set()
    path = []
    for u, v in euler_tour:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to the start point

    return path

# Create the graph and run Christofides algorithm
G = create_graph(cities)
tour = christofides_tsp(G)

# Calculate the cost of the tour
def calculate_cost(tour, G):
    cost = sum(G[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))
    return cost

total_cost = calculate_cost(tour, G)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
import networkx as nx
import numpy as np
import itertools

# Define the cities locations
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating Complete Graph
def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            distance = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=distance)
    return G

# Construct Minimum Spanning Tree
def mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Find nodes of odd degree in the MST
def odd_degree_nodes(T):
    return [v for v, degree in dict(T.degree()).items() if degree % 2 == 1]

# Find Minimum Cost Perfect Matching
def min_cost_perfect_matching(G, odd_nodes):
    subgraph = G.subgraph(odd_nodes)
    min_cost_match = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return min_cost_match

# Combine MST and matching to make it Eulerian
def make_eulerian(T, matching_edges):
    G = T.copy()
    G.add_edges_from(matching_edges)
    return G

# Create a Hamiltonian circuit from Eulerian circuit
def get_hamiltonian_circuit(G, starting_node=0):
    visited = set([starting_node])
    path = [starting_node]
    path_cost = 0

    # Simplified version of finding an Eulerian path and making it Hamiltonian
    for u, v in nx.eulerian_circuit(G, source=starting_node, keys=False):
        if v not in visited:
            path.append(v)
            visited.add(v)
            path_cost += G[u][v]['weight']

    # Close the tour
    path.append(starting_node)
    path_cost += G[path[-2]][starting_node]['weight']
    return path, path_struct

# Steps combined in one function
def solve_tsp(cities):
    G = create_graph(cities)
    T = mst(G)
    odd_nodes = odd_degree_nodes(T)
    matching = min_cost_perfect_matching(G, odd_nodes)
    eulerian_graph = make_eulerian(T, matching)
    tour, cost = get_hamiltonian_circuit(eulerian_graph)
    return tour, cost

# Calculate the shortest tour and its total cost
tour, total_cost = solve_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
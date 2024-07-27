import networkx as nx
import numpy as np

# Define the cities locations
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Compute Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating Complete Graph
def create_graph(cities):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
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
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Combine MST and matching to make it Eulerian
def make_eulerian(T, matching):
    G = T.copy()
    G.add_edges_from(matching)
    for u, v in matching:
        # We need to double the edge as we add it to the MST, making sure it's included in the Eulerian circuit
        G[u][v]['weight'] = G[u][v]['weight'] / 2
    return G

# Extract a Hamiltonian circuit from an Eulerian circuit
def get_hamiltonian_circuit(G, start_node=0):
    path = [start_node]
    path_cost = 0
    visited = set([start_node])

    for u, v in nx.eulerian_circuit(G, source=start_node):
        if v not in visited:
            path.append(v)
            visited.add(v)
            path_cost += G[u][v]['weight']
    path.append(start_node)  # complete the circuit
    path_cost += G[path[-2]][start_node]['weight']

    return path, path_cost

# Solving TSP
def solve_tsp(cities):
    G = create_graph(cities)
    T = mst(G)
    odd_nodes = odd_degree_nodes(T)
    matching = min_cost_perfect_matching(G, odd_nodes)
    eulerian_graph = make_eulerian(T, matching)
    tour, cost = get_hamiltonian_circuit(eulerian_graph, start_node=0)
    return tour, cost

# Calculate the shortest tour and its total cost
tour, total_cost = solve_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
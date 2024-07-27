import math
import networkx as nx
from itertools import combinations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_edges(cities):
    n = len(cities)
    edges = []
    for pair in combinations(range(n), 2):
        weight = euclidean_distance(cities[pair[0]], cities[pair[1]])
        edges.append((pair[0], pair[1], weight))
        edges.append((pair[1], pair[0], weight))  # As we need undirected edges
    return edges

def create_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    return G

def build_biconnected_subgraph(G, edges):
    edges_sorted = sorted(edges, key=lambda x: x[2])

    # Create a graph just with nodes for progressive edge addition
    H = G.copy()
    H.remove_edges_from(list(H.edges()))

    # Step 0 (Initialization)
    E_BB = []
    
    # Step 1 (Augmentation)
    biconnected = False
    for edge in edges_sorted:
        H.add_edge(edge[0], edge[1], weight=edge[2])
        if nx.is_biconnected(H):
            biconnected = True
            break
        else:
            E_BB.append(edge)

    if not biconnected:
        for edge in edges_sorted:
            if edge not in H.edges():
                H.add_edge(edge[0], edge[1], weight=edge[2])
                if nx.is_biconnected(H):
                    break

    return H

def find_tour(G_square):
    # Using minimum weight Hamiltonian cycle approach for approximation.
    cycle = nx.approximation.traveling_salesman_problem(G_square, cycle=True, method='greedy')
    return cycle

# Input Data: List of coordinates for cities (depot included as first element)
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Step 1: Prepare graph and find biconnected subgraph as per algorithm BB
edges = find_edges(cities)
G = create_graph(range(len(cities)), edges)
biconnected_subgraph = build_biconnected_subgraph(G, edges)

# Step 2: Find the tour from the square of the biconnected subgraph (G^2)
G_square = nx.power(G, 2)
tour = find_tour(G_square)

total_dist = sum(euclidean_distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))
max_edge_dist = max(euclidean_distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

print("Tour:", tour)
print("Total travel cost:", total_dist)
print("Maximum distance between consecutive cities:", max_edge_dist)
import networkx as nx
import numpy as np
from itertools import combinations
from networkx.algorithms import approximation as apx

def euclidean_distance(p1, p2):
    return round(np.linalg.norm(np.array(p1) - np.array(p2)), 2)

def create_complete_graph(node_coords):
    G = nx.Graph()
    n = len(node_coords)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(node_coords[i], node_coords[j])
            G.add_edge(i, j, weight=dist)
            G.add_edge(j, i, weight=dist)
    return G

def minimum_weight_perfect_matching(G, odd_nodes):
    # The function in NetworkX covers just minimum weight perfect matching
    return apx.min_weight_matching(G, maxcardinality=True, weight='weight')

def find_eulerian_circuit(H, start_node=0):
    circuit = list(nx.eulerian_circuit(H, source=start_node))
    return circuit

def christofides_algorithm(cities):
    n = len(cities)
    G = create_complete_graph(cities)
    T = nx.minimum_spanning_tree(G, weight='weight')
    odd_degree_nodes = [v for v, d in T.degree() if d % 2 != 0]
    subG = G.subgraph(odd_degree_nodes)
    M = minimum_weight_perfect_matching(subG)
    
    # Add edges from the matching to the MST
    H = nx.MultiGraph(T)
    for u, v in M:
        H.add_edge(u, v, weight=G[u][v]['weight'])

    eulerian_circuit = find_eulerian_circuit(H, start_node=0)
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if v not in visited or v == 0:
            path.append(v)
            visited.add(v)

    # Make sure to return to the start node
    path.append(path[0])
    
    # Calculate total cost
    total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
    
    return path, total_cost

cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]
tour, total_cost = christofides_algorithm(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
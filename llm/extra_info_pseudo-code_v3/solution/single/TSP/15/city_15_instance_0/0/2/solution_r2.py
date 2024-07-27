import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean

def create_complete_graph(points):
    G = nx.Graph()
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean(points[i], points[j]))
    return G

def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 != 0]

def min_weight_matching(G, vertices):
    subgraph = G.subgraph(vertices)
    return nx.Graph(list(nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)))

def eulerian_circuit(multigraph, start_vertex):
    return list(nx.eulerian_circuit(multigraph, source=start_vertex))

def christofides_algorithm(points):
    G = create_complete_graph(points)
    T = minimum_spanning_tree(G)
    O = odd_degree_vertices(T)
    M = min_weight_matching(G, O)
    H = nx.MultiGraph(T)
    H.add_edges_from(M.edges(data=True))
    circuit = eulerian_circuit(H, start_vertex=0)

    # Convert Eulerian to Hamiltonian
    path, cost = [0], 0
    visited = set(path)
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            cost += G[u][v]['weight']
            visited.add(v)
    path.append(0)  # Return to the start
    cost += G[path[-2]][0]['weight']  # Add the cost to return to the start

    return path, cost

cities_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

tour, total_cost = christofides_algorithm(cities_coordinates)
print("Tour:", tour)
print("Total travel cost:", total_cost)
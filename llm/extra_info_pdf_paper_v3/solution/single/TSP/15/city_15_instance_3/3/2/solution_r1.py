import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

# Coordinates of the depot and cities
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

def calculate_distances(coords):
    return distance_matrix(coords, coords)

def minimum_spanning_tree(dist_matrix):
    num_vertices = len(dist_matrix)
    graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            graph.add_edge(i, j, weight=dist_matrix[i][j])
    return nx.minimum_spanning_tree(graph, weight='weight')

def get_odd_degree_vertices(graph):
    return [v for v, d in graph.degree() if d % 2 == 1]

def minimum_cost_perfect_matching(graph, odd_vertices, dist_matrix):
    incomplete_graph = nx.Graph()
    incomplete_graph.add_nodes_from(odd_vertices)
    for u, v in combinations(odd_vertices, 2):
        incomplete_graph.add_edge(u, v, weight=dist_matrix[u][v])
    return nx.algorithms.matching.min_weight_matching(incomplete_graph, maxcardinality=True, weight='weight')

def create_eulerian_multigraph(mst, matching):
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching)
    return multigraph

def find_hamiltonian_circuit(multigraph, start_vertex):
    eulerian_path = list(nx.eulerian_circuit(multigraph, source=start_vertex))
    visited = set()
    path = [start_vertex]
    cost = 0
    
    for u, v in eulerian_path:
        if v not in visited:
            path.append(v)
            visited.add(v)
            cost += dist[u][v]
    
    # close the loop
    path.append(start_vertex)
    cost += dist[path[-2]][start_vertex]
    return path, cost

dist = calculate_distances(coordinates)
mst = minimum_spanning_tree(dist)
odd_vertices = get_odd_degree_vertices(mst)
matching = minimum_cost_perfect_matching(mst, odd_vertices, dist)
eulerian_multigraph = create_eulerian_multigraph(mst, matching)
tour, total_cost = find_hamiltonian_circuit(eulerian_multigraph, 0)

print("Tour:", tour)
print("Total travel cost:", total_cost)
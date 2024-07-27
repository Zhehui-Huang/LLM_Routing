import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx
import itertools

# Generate Euclidean distance matrix
def compute_distances(cities):
    return distance_matrix(cities, cities)

# Minimum Spanning Tree using NetworkX
def find_mst(dist_matrix):
    G = nx.Graph()
    for i in range(len(dist_matrix)):
        for j in range(i + 1, len(dist_matrix)):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return nx.minimum_spanning_tree(G)

# Find minimum weight perfect matching on the subgraph of odd degree vertices
def find_perfect_matching(subgraph, full_graph):
    return nx.algorithms.matching.min_weight_matching(full_graph, subset=subgraph, maxcardinality=True)

# Function to get odd vertex degree
def get_odd_vertex_degrees(mst):
    odd_degrees = []
    for node in mst.nodes():
        if mst.degree[node] % 2 != 0:
            odd_degrees.append(node)
    return odd_degrees

# Build the multigraph from MST and Matching
def create_multigraph(mst, matching, all_cities):
    multigraph = nx.MultiGraph(mst)
    for edge in matching:
        multigraph.add_edge(*edge, weight=all_cities[edge[0]][edge[1]])
    return multigraph

# Find Eulerian tour
def find_eulerian_tour(multigraph):
    return list(nx.eulerian_circuit(multigraph))

# Creating Hamiltonian circuit by skipping visited nodes in Eulerian tour
def create_hamiltonian_circuit_from_eulerian(eulerian_tour, start_city):
    visited = set()
    path = []
    for u, v in eulerian_tour:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(start_city)  # Close the tour
    return path

# Prepare cities coordinate data
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 95), (29, 64), (32, 79)]

dist_matrix = compute_distances(cities)
mst = find_mst(dist_matrix)
odd_vertices = get_odd_vertex_degrees(mst)
subgraph = mst.subgraph(odd_vertices)  # Subgraph of nodes with odd degree
full_graph = nx.complete_graph(len(cities), nx.Graph())
matching = find_perfect_matching(odd_vertices, full_graph)
multigraph = create_multigraph(mst, matching, dist_matrix)
eulerian_tour = find_eulerian_tour(multigraph)
tour = create_hamiltonian_circuit_from_eulerian(eulerian_tour, 0)

# Compute the tour cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
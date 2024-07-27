import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import Graph, eulerian_circuit
import networkx as nx
import itertools

# Define cities and their coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Calculate Euclidean distance matrix
coords = list(cities.values())
distance_mat = distance_matrix(coords, coords)

# Compute Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(distance_mat).toarray()

def find_odd_degree_vertices(graph, n):
    odd_degree_nodes = []
    for i in range(n):
        if sum(graph[i] > 0) % 2 != 0:
            odd_degree for i in range(n):
        odd_degree_nodes.append(i)
    return odd_degree_nodes

def minimum_weight_perfect_matching(odd_vertices, full_graph):
    num_vertices = len(odd_vertices)
    subgraph = Graph()
    subgraph.add_nodes_from(odd_vertices)
    for i, j in itertools.combinations(odd_vertices, 2):
        subgraph.add_edge(i, j, weight=full_graph[i][j])
    matched_edges = nx.algorithms.matching.min_weight_matching(subgraph, True)
    return matched_edges

def total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

num_cities = len(cities)

# Finding odd degree vertices in MST
odd_vertices = find_odd_degree_vertices(mst, num_cities)
# Find minimum weight perfect matching in the subgraph of odd degree vertices
full_graph = nx.complete_graph(num_cities)
for i in range(num_cities):
    for j in range(num_cities):
        full_graph[i][j]['weight'] = distance_mat[i][j]

matching_edges = minimum_weight_perfect_matching(odd_vertices, full_graph)

# Creating multigraph by adding matching edges to MST graph
multi_graph = Graph()
for i in range(num_vertices):
    for j in range(i+1, num_vertices):
        if mst[i][j] > 0 or mst[j][i] > 0:
            multi_graph.add_edge(i, j, weight=distance_mat[i][j])
multi_graph.add_edges_from(matching_edges)

# Finding Eulerian circuit
euler_circuit = list(eulerian_circuit(multi_graph))

# Making a Hamiltonian circuit: shortcutting visited nodes
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
    if len(visited) == num_cities - 1:
        break

hamiltonian_circuit.append(0)

# Calculate the total travel cost of the circuit
total_cost = total_distance(hamiltonian_circuit, distance_mat)

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
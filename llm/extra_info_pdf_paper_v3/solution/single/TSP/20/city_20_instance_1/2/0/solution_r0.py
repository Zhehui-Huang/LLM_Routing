import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations

def create_distance_matrix(cities):
    return distance_matrix(cities, cities)

def find_odd_degree_vertices(mst):
    return [v for v, d in mst.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(mst, odd_vertices, distance_matrix):
    subgraph = nx.Graph()
    subgraph.add_nodes_from(odd_vertices)
    for u, v in combinations(odd_vertices, 2):
        subgraph.add_edge(u, v, weight=distance_matrix[u][v])
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def create_eulerian_circuit(mst, matching, depot):
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=depot))
    return eulerian_circuit

def convert_to_hamiltonian_circuit(eulerian_circuit, depot):
    visited = set()
    path = [depot]
    for u, v in eulerian_circuit:
        if v not in visited or v == depot:
            path.append(v)
            visited.add(v)
    path.append(depot)
    return path

def calculate_total_cost(path, distance_matrix):
    return sum(distance_custom_mat[path[i], path[i + 1]] for i in range(len(path) - 1))

# Cities and their coordinates
cities = np.array([
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
])

distance_custom_mat = create_distance_matrix(cities)

# Creating graph from distance matrix
G = nx.complete_graph(len(cities))
for i, j in combinations(range(len(cities)), 2):
    G[i][j]['weight'] = distance_custom_mat[i][j]

# Find Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree
odd_degree_vertices = find_odd_degree_vertices(mst)

# Find the minimum weight perfect matching
matching = minimum_weight_perfect_matching(mst, odd_degree_vertices, distance_custom_mat)

# Create Eulerian circuit
eulerian_circuit = create_eulerian_circuit(mst, matching, 0)

# Convert Eulerian to Hamiltonian circuit
hamiltonian_circuit = convert_to_hamiltonian_circuit(eulerian_circuit, 0)

# Calculate total cost of the tour
total_cost = calculate_total_cost(hamiltonian_circuit, distance_custom_mat)

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
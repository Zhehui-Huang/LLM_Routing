import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
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

def minimum_spanning_tree(dist_matrix, graph):
    # Create edges with weights corresponding to the distance between cities
    for i in range(len(dist_matrix)):
        for j in range(i+1, len(dist_matrix)):
            graph.add_edge(i, j, weight=dist_matrix[i][j])
    # Generate MST
    return nx.minimum_spanning_tree(graph, weight='weight')

def get_odd_degree_vertices(graph):
    return [v for v, d in graph.degree() if d % 2 == 1]

def minimum_cost_perfect_matching(graph, odd_vertices, dist_matrix):
    min_cost_graph = nx.Graph()
    # Add all vertices
    min_cost_graph.add_nodes_from(odd_vertices)
    # Add edges with weights between odd degree vertices
    for pair in combinations(odd_vertices, 2):
        min_cost_graph.add_edge(pair[0], pair[1], weight=dist_matrix[pair[0]][pair[1]])
    # Get minimum weight matching
    return nx.algorithms.matching.min_weight_matching(min_cost_graph, maxcardinality=True)

def eulerian_circuit(graph, start_vertex):
    return list(nx.eulerian_circuit(graph, source=start_vertex))

def create_hamiltonian_circuit(eulerian_path, start_vertex):
    # Use a set to track visited vertices
    visited = set()
    path = []
    cost = 0
    prev = None

    for edge in eulerian_path:
        if edge[0] not in visited:
            if prev is not None:
                cost += dist[edge[0], prev]
            path.append(edge[0])
            visited.add(edge[0])
            prev = edge[0]

    # Add return to start_vertex
    path.append(start_vertex)
    cost += dist[start_vertex, prev]  # add last edge back to start
    return path, cost

# Calculate distances
dist = calculate_distances(coordinates)

# Initiate a new graph
G = nx.Graph()
mst = minimum_spanning_tree(dist, G)
odd_vertices = get_odd_degree_vertices(mst)
matching = minimum_cost_perfect_matching(mst, odd_vertices, dist)

# Add the edges from the minimum cost perfect matching to the MST
mst.add_edges_from(matching)

# Find Eulerian circuit starting from the depot, which is vertex 0
euler_path = eulerian_circular(mst, 0)

# Find the Hamiltonian circuit
tour_final, total_cost = create_hamiltonian_circuit(euler_path, 0)

# Output the results
print("Tour:", tour_final)
print("Total travel cost:", total_cost)
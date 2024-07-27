import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

def calculate_distances(cities):
    return squareform(pdist(cities, metric='euclidean'))

def create_graph(distances):
    n = len(distances)
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=distances[i][j])
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    dist_matrix = nx.to_numpy_array(subgraph)
    row_ind, col_ind = linear_sum_assignment(dist_matrix)
    matching = nx.Graph()
    for i, j in zip(row_ind, colind):
        matching.add_edge(odd_vertices[i], odd_vertices[j], weight=dist_matrix[i][j])
    return matching

def eulerian_circuit_multigraph(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_path(eulerian_circuit):
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # ensure return to the starting city
    return path

# Define cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Compute distances
distances = calculate_distances(cities)

# Create graph
G = create_graph(distances)

# Find MST
T = find_minimum_spanning_tree(G)

# Find odd degree vertices
O = find_odd_degree_vertices(T)

# Find minimum weight perfect matching
M = minimum_weight_perfect_matching(G, O)

# Create multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M.edges())

# Find an Eulerian circuit
eulerian_circuit = eulerian_circuit_multigraph(H)

# Convert to Hamiltonian circuit
tour = create_hamiltonian_path(eulerian_circuit)

# Calculate total cost of the tour
total_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
import math
import networkx as nx
import numpy as np
from itertools import combinations

# City coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph
def create_complete_graph(node_coords):
    G = nx.Graph()
    for i, coords1 in enumerate(node_coords):
        for j, coords2 in enumerate(node_coords):
            if i != j:
                G.add_edge(i, j, weight=euclidean_distance(coords1, coords2))
    return G

# Step 1: Compute MST T of G
def compute_mst(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Identify set O of vertices with odd degree in T
def get_odd_degree_vertices(T):
    return [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find minimal-weight perfect matching M in the subgraph induced by O
def perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 5: Find eulerian circuit
def eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

# Step 6: Convert Eulerian to Hamiltonian circuit
def create_hamiltonian_circuit(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(path[0])  # return to start
    return path

# Perform Christofides algorithm
def christofides_algorithm(node_coordinates):
    G = create_complete_graph(node_coordinates)
    T = compute_mst(G)
    odd_degree_vertices = get_odd_degree_vertices(T)
    M = perfect_matching(G, odd_degree_vertices)
    H = nx.Graph(T)
    H.add_edges_from(M)
    circuit = eulerian_circuit(H)
    tour = create_hamiltonian_circuit(circuit)
    return tour

# Calculate the total cost of the tour
def calculate_cost(tour, node_coords):
    total_cost = sum(euclidean_distance(node_coords[tour[i]], node_coords[tour[i+1]]) for i in range(len(tour) - 1))
    return total_cost

# Solve the problem
tour = christofides_algorithm(coordinates)
total_cost = calculate_cost(tour, coordinates)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
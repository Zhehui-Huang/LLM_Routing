import networkx as nx
import numpy as np
from itertools import combinations

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def create_complete_graph(city_coords):
    G = nx.Graph()
    n = len(city_coords)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(city_coords[i], city_coords[j])
            G.add_edge(i, j, weight=dist)
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def form_multigraph(T, M):
    H = T.copy()
    for u, v in M:
        H.add_edge(u, v)
    return H

def find_eulerian_circuit(H):
    return list(nx.eulerian_circuit(H))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to return to the starting point
    return path

def calculate_path_weight(G, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += G[path[i]][path[i+1]]['weight']
    return weight

# Coordinates of cities
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Creating graph from city coordinates
G = create_complete_graph(cities)

# Step 1: Minimum spanning tree
T = find_minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_vertices = find_odd_degree_vertices(T)

# Step 3: Minimum-weight perfect matching
M = minimum_weight_perfect_matching(G, odd_vertices)

# Step 4: Form multigraph
H = form_multigraph(T, M)

# Step 5: Find Eulerian circuit in H
eulerian_circuit = find_eulerian_circuit(H)

# Step 6: Create Hamiltonian circuit from Eulerian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Step 7: Calculate the total travel cost of the tour
total_travel_cost = calculate_path_weight(G, hamiltonian_circuit)

# Output the tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")
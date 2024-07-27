import networkx as nx
import numpy as np

# Euclidean distance formula
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Creating a weighted complete graph
def create_complete_graph(city_coords):
    G = nx.Graph()
    n = len(city_coords)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_triggerstance(city_coords[i], city_coords[j])
            G.add_edge(i, j, weight=dist)
    return G

# Function to calculate minimum spanning tree
def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Helper to find vertices of odd degree in a graph
def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Function to find a minimum weight perfect matching
def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Combine an MST and matching into an Eulerian multigraph
def form_multigraph(T, M):
    H = T.copy()
    for u, v in M:
        H.add_edge(u, v)
    return H

# Extract a Hamiltonian circuit from an Eulerian circuit by skipping repetitions
def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # Ensure it's a circuit by returning to the start
    return path

# Calculate the total travel cost of a path
def calculate_path_weight(G, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += G[path[i]][path[i+1]]['weight']
    return weight

# Coordinates of the cities (including the depot as city 0)
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Step 1: Create graph
G = create_complete_graph(cities)
print("Step 1: Complete graph created.")

# Step 2: Compute MST
T = find_minimum_spanning_tree(G)
print("Step 2: Minimum Spanning Tree computed.")

# Step 3: Identify vertices of odd degree
odd_vertices = find_odd_degree_vertices(T)
print(f"Step 3: Odd degree vertices identified: {odd_vertices}")

# Step 4: Find minimum-weight perfect matching
M = minimum_weight_perfect_matching(G, odd_vertices)
print("Step 4: Minimum weight perfect matching found.")

# Step 5: Form multigraph using MST and matching
H = form_multigraph(T, M)
print("Step 5: Multigraph formed.")

# Step 6: Find an Eulerian circuit
eulerian_circuit = find_eulerian_circuit(H)
print(eulerian_circuit)

# Step 7: Convert the Eulerian circuit to a Hamiltonian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
print(f"Step 7: Hamiltonian circuit formed: {hamiltonian_circuit}")

# Calculate the tour cost
total_travel_cost = calculate_path_weight(G, hamiltonian_circuit)
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")
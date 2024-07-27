import networkx as nx
import numpy as np

# Define function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph of cities with their coordinates
def create_complete_graph(city_coords):
    G = nx.Graph()
    number_of_cities = len(city_coords)
    for i in range(number_of_cities):
        for j in range(i + 1, number_of_cities):
            distance = euclidean_distance(city_coords[i], city_coords[j])
            G.add_edge(i, j, weight=distance)
    return G

# Identify odd degree vertices in a graph
def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 != 0]

# Create tour from Eulerian circuit skipping visited nodes
def create_tour_from_eulerian_circuit(eulerian_circuit):
    path = []
    visited = set()
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    return path

# Calculate total distance for the tour
def compute_total_distance(path, city_coords):
    total_distance = 0
   # Ensure returning to the starting point
   path.append(path[0])
    for i in range(len(path) - 1):
        total_distance += euclidean_distance(city_coords[path[i]], city_coords[path[i + 1]])
    return total_distance

# Coordinates of cities
city_coords = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Construct a complete graph
G = create_complete_graph(city_coords)

# Compute Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G, weight='weight')

# Find odd degree vertices from MST
odd_vertices = find_odd_degree_vertices(T)

# Find minimum weight perfect matching among odd degree vertices
min_weight_match = nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True, weight='weight')

# Create multigraph H by combining edges from T and min_weight_match
H = nx.MultiGraph(T)
H.add_edges_from(min_weight_match)

# Compute an Eulerian circuit on graph H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert Eulerian circuit to a Hamiltonian circuit
tour = create_tour_from_eulerian_circuit(eulerian_circuit)

# Calculate the total distance of the tour
total_cost = compute_total_distance(tour, city_coords)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
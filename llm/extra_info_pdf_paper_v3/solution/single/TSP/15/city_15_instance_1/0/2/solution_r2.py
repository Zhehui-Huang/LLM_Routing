import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms import approximation as approx

def calculate_euclidean_distance(coords):
    # Calculate the full distance matrix
    return distance_matrix(coords, coords)

def find_mst_and_odd_vertices(distances):
    G = nx.Graph()
    num_cities = len(distances)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=distances[i][j])
    
    # Find the Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(G)
    odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 != 0]
    return mst, odd_degree_vertices

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    # Find minimum weight matching. This might not be perfect, thus max_weight_matching must be adjusted.
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return matching

def create_eulerian_circuit(mst, matching, start_vertex):
    G = nx.MultiGraph(mst)
    G.add_edges_from(matching)
    # Create Eulerian circuit
    eulerian_circuit = list(nx.eulerian_circuit(G, source=start_vertex))
    return eulerian_circuit

def make_hamiltonian(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # returning to the start
    return path

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

# Coordinates of the cities
coords = np.array([
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
])

# Step 1: calculate distances
distances = calculate_euclidean_distance(coords)

# Step 2: Find MST and odd degree vertices
mst, odd_degree_vertices = find_mst_and_odd_vertices(distances)

# Step 3: Minimum weight perfect matching on odd degree vertices
matching = minimum_weight_perfect_matching(mst, odd_degree_vertices)

# Step 4: Create Eulerian circuit
start_vertex = 0
eulerian_circuit = create_eulerian_circuit(mst, matching, start_vertex)

# Step 5: Make the circuit Hamiltonian
hamiltonian_path = make_hamiltonian(eulerian_circuit)

# Step 6: Calculate the total distance
total_distance = calculate_total_distance(hamiltonian_path, distances)

# Output
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_distance)
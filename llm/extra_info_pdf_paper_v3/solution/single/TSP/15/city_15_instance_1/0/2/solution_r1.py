import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean

def compute_distances(coords):
    n = len(coords)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            dist = euclidean(coords[i], coords[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_mst_and_odd_vertices(distances):
    G = nx.complete_graph(len(distances))
    for i in range(len(distances)):
        for j in range(len(distances)):
            G[i][j]['weight'] = distances[i][j]
    
    mst = nx.minimum_spanning_tree(G)
    odd_degree_vertices = [v for v in mst.nodes if mst.degree(v) % 2 != 0]
    return mst, odd_degree_vertices

def perfect_matching(mst, odd_vertices, distances):
    subgraph = mst.subgraph(odd_vertices)
    min_weight_match = nx.Graph()
    min_weight_match.add_nodes_from(odd_vertices)
    
    for i in odd_vertices:
        for j in odd_vertices:
            if i != j:
                min_weight_match.add_edge(i, j, weight=distances[i][j])

    matching = nx.algorithms.matching.min_weight_matching(min_weight_match, maxcardinality=True)
    return matching

def create_eulerian_circuit(mst, matching):
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    start_vertex = 0
    eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=start_vertex))
    return eulerian_circuit

def make_hamiltonian(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited or u == 0:
            path.append(u)
            visited.add(u)
    path.append(0)  # back to the depot
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

# Calculate distances
distances = compute_distances(coords)

# Find MST and odd degree vertices
mst, odd_degree_vertices = find_mst_and_odd_vertices(distances)

# Find perfect matching
matching = perfect_matching(mst, odd_degree_vertices, distances)

# Create Eulerian circuit
eulerian_circuit = create_eulerian_circuit(mst, matching)

# Convert to Hamiltonian path
hamiltonian_path = make_hamiltonian(eulerian_circuit)

# Calculate total travel distance
total_distance = calculate_total_distance(hamiltonian_path, distances)

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", total_distance)
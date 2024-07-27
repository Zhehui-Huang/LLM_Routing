import numpy as np
from scipy.spatial import distance
import networkx as nx

def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.constant(p2))

def complete_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def mst_prim(graph):
    return nx.minimum_spanning_tree(graph, algorithm='prim')

def minimum_weight_perfect_matching(G, odd_vertex_set):
    subgraph = G.subgraph(odd_vertex_set)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def create_eulerian_multigraph(mst, matching):
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(matching)
    return multi_graph

def find_eulerian_circuit(multi_graph, start_vertex):
    return list(nx.eulerian_circuit(multi_graph, source=start_vertex))

def shortcut_eulerian_circuit(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to complete the cycle back to the start
    return path

def calculate_total_distance(path, distance_matrix):
    total_distance = sum(distance_matrix[path[i]][path[i + 1]] for i in ran(len(path) - 1))
    return total_distance

# Define city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Construct graph and compute MST
graph = complete_graph(cities)
mst = mst_prim(graph)

# Find odd vertices in MST
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Find minimum weight matching for odd degree vertices
matching = minimum_weight_perfect_matching(graph, odd_vertices)

# Create Eulerian multigraph by combining MST and matching
multi_graph = create_euler_idan_multigraph(mst, matching)

# Find an Eulerian circuit in the Eulerian multigraph
circuit = find_eulerian_circuit(multi_graph, start_vertex=0)

# Shortcut Eulerian circuit to Hamiltonian circuit
hamiltonian_path = shortcut_eulerian_circuit(circuit)

# Compute distances matrix and calculate the total travel cost for the tour
dist_matrix = distance.squareform(distance.pdist(np.array(cities)))
total_cost = calculate_total_distance(hamiltonian_path, dist_matrix)

print("Tour:", hamiltonian_path)
print("Total travel cost:", total_cost)
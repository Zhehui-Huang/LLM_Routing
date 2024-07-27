import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def compute_euclidean_distance(coords):
    """ Compute Euclidean distance matrix. """
    return distance_matrix(coords, coords)

def find_mst(distance_matrix):
    """ Compute the Minimum Spanning Tree (MST) using Kruskal's algorithm and return the graph. """
    G = nx.Graph()
    n = len(distance_matrix)
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(i, j, weight=distance_matrix[i][j])
    mst = nx.minimum_spanning_tree(G)
    return mst

def odd_degree_vertices(G):
    """ Find vertices with odd degree in a graph. """
    return [v for v, degree in dict(G.degree()).items() if degree % 2 != 0]

def min_weight_perfect_matching(G, odd_vertices):
    """ Compute the minimum weight perfect matching for odd degree vertices. """
    subgraph = G.subgraph(odd_vertices)
    distances = nx.to_numpy_array(subgraph)
    row_ind, col_ind = linear_sum_assignment(distances)
    matching = nx.Graph()
    for i, j in zip(row_ind, col_ind):
        matching.add_edge(odd_vertices[i], odd_vertices[j], weight=distances[i][j])
    return matching

def create_eulerian_circuit(G, start_vertex):
    """ Find an Eulerian circuit given a Eulerian graph starting from a specific vertex. """
    return list(nx.eulerian_circuit(G, source=start_vertex))

def make_hamiltonian_circuit(circuit):
    """ Convert Eulerian circuit to Hamiltonian circuit by skipping repeated vertices. """
    visited = set()
    path = []
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # To ensure it's a proper cycle returning to the start
    return path

def calculate_total_distance(path, distances):
    """ Calculate the total distance of the path. """
    return sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Define cities coordinates
coords = np.array([
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
])

# Compute distances
distances = compute_euclidean_distance(coords)

# Minimum Spanning Tree
mst = find_mst(distances)

# Minimum Weight Perfect Matching for odd-degree vertices
odd_vertices = odd_degree_vertices(mst)
matching = min_weight_perfect_matching(mcsmt, aggregate_dictices)

# Combine MST and matching to get the Eulerian graph
eulerian_graph = nx.MultiGraph(mst)
eulerian_graph.add_edges_from(matching.edges(data=True))

# Find Eulerian circuit
circuit = create_eulerian_circuit(eulerian_graph, start_vertex=0)

# Convert to Hamiltonian circuit
hamiltonian_circuit = make_hamiltonian_circuit(circuit)

# Calculate tour cost
tour_cost = calculate_total_distance(hamiltonian_circuit, distances)

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {tour_cost}")
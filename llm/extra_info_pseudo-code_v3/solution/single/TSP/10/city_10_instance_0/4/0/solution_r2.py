import math
import networkx as nx
from scipy.spatial.distance import pdist, squareform

# Coordinates of cities including the depot city at index 0
cities = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39), 
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Calculating distances between each pair of cities
def calculate_distances(cities):
    dist_matrix = squareform(pdist(cities, 'euclidean'))
    return dist_matrix

# Create a complete graph with cities and their calculated distances
def create_complete_graph(cities, dist_matrix):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Calculating a minimum spanning tree (MST) using Kruskal's algorithm
def compute_mst(G):
    return nx.minimum_spanning_tree(G)

# Identifying vertices with odd degree in the MST
def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Find a minimum weight perfect matching in the subgraph induced by the odd degree vertices
def minimum_weight_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)
    return matching

# Adding matching edges to the MST to form a multigraph with even degree at each vertex
def add_matching_to_mst(T, matching):
    T.add_edges_from(matching)
    return T

# Finding an Eulerian circuit in the multigraph
def find_eulerian_circuit(G):
    return list(nx.eulerian_circuit(G))

# Constructing a Hamiltonian circuit from the Eulerian circuit - shortcutting
def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # to make it a complete tour back to the depot
    return path

# Calculate the total travel cost of the path
def calculate_cost(path, dist_matrix):
    return sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

# Solving the TSP
dist_matrix = calculate_distances(cities)
G = create_complete_graph(cities, dist_matrix)
T = compute_mst(G)
odd_vertices = find_odd_degree_vertices(T)
M = minimum_weight_matching(G, odd_vertices)
multigraph = add_matching_to_mst(T, M)
eulerian_circuit = find_eulerian_circuit(multigraph)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)
total_cost = calculate_cost(hamiltonian_circuit, dist_matrix)

# Output results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")
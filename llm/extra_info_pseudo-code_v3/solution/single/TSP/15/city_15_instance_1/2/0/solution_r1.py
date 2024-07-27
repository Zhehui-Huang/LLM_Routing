import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

def find_odd_degree_vertices(G):
    return [v for v, degree in G.degree() if degree % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def create_multigraph(G, matching):
    multigraph = G.copy()
    multigraph.add_edges_from(matching)
    return multigraph

def find_eulerian_circuit(multigraph, starting_vertex):
    return list(nx.eulerian_circuit(multigraph, source=starting_vertex))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])  # return to start
    return path

def calculate_tour_cost(path, distances):
    cost = sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
    return cost

# Coordinates of cities
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Calculate distances matrix
distances_matrix = calculate_distances(cities)

# Construct the graph and compute MST
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distances_matrix[i][j])
T = nx.minimum_spanning_tree(G)

# Find vertices with odd degree
odd_vertices = find_odd_degree_vertices(T)

# Find the minimum weight perfect matching
matching = minimum_weight_perfect_matching(G, odd_vertices)

# Create multigraph
H = create_mult_graph(T, matching)

# Find Eulerian circuit
eulerian_circuit = find_eulerian_circuit(H, 0)

# Convert eulerian to hamiltonian circuit
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

# Calculate the tour cost
tour_cost = calculate_tour_cost(hamiltonian_circuit, distances_matrix)

# Print the output
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {tour_cost:.2f}")
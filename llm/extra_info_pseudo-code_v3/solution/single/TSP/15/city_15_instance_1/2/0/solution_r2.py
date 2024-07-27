import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i, num_cities):
            distance = euclidean(cities[i], cities[j])
            distances[i][j] = distances[j][i] = distance
    return distances

def find_odd_degree_vertices(tree):
    return [node for node, degree in dict(tree.degree()).items() if degree % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    matches = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    return matches

def create_hamiltonian_circuit(multigraph, starting_vertex):
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=startinglear_vertex))
    visited = set()
    path = [starting_vertex]
    visited.add(starting_vertex)
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(starting_vertex)
    return path

def calculate_tour_cost(path, distances):
    return sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))

cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43),
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

distances_matrix = calculate_distances(cities)

G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=distances_matrix[i][j])

MST = nx.minimum_spanning_tree(G)
odd_vertices = find_odd_degree_vertices(MST)
matching = minimum_weight_perfect_matching(G, odd_vertices)

# Create multigraph by combining MST and matching
multigraph = nx.MultiGraph(MST)
multigraph.add_edges_from(matching)

# Find Hamiltonian Circuit
tour = create_hamiltonian_circuit(multigraph, 0)
tour_cost = calculate_tour_cost(tour, distances_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")
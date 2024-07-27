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

def find_odd_vertices(tree):
    odd_vertices = [idx for idx, degree in enumerate(tree.degree()) if degree % 2 == 1]
    return odd_vertices

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

def find_eulerian_circuit(multigraph, starting_vertex):
    return list(nx.eulerian_circuit(multigraph, source=starting_vertex))

def create_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
    path.append(path[0])
    return path

def calculate_tour_cost(path, distances):
    cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
    return cost

# Define cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
num_cities = len(cities)

# Calculate distances
distances_matrix = calculate_distances(cities)

# Generate MST
mst_matrix = minimum_spanning_tree(csr_matrix(distances_matrix))
G = nx.from_scipy_sparse_matrix(mst_matrix)

# Step 2 & 3: Find odd vertices and their minimum weight perfect matching
odd_vertices = find_odd_vertices(G)
G.add_edges_from(minimum_weight_perfect_matching(G, odd_vertices), weight=0)

# Step 4 & 5: Find an Eulerian circuit
eulerian_circuit = find_eulerian_circuit(G, 0)

# Step 6: Hamiltonian circuit
tour = create_hamiltonian_circuit(eulerian_circuit)
tour_cost = calculate_tour_cost(tour, distances_matrix)

# Present the results
print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost:.2f}")
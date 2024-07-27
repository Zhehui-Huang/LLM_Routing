import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, algorithms
import itertools

def compute_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_odd_vertices_from_mst(num_cities, mst):
    degree = np.zeros(num_cities, dtype=int)
    odd_vertices = []
    rows, cols = mst.nonzero()
    for row, col in zip(rows, cols):
        degree[row] += 1
        degree[col] += 1
    for vertex in range(num_cities):
        if degree[vertex] % 2 != 0:
            odd_vertices.append(vertex)
    return odd_vertices

def minimum_weight_perfect_matching(odd_vertices, distance_matrix):
    num_vertices = len(odd_vertices)
    graph = Graph()
    for subset in itertools.combinations(odd_vertices, 2):
        i, j = subset
        graph.add_edge(i, j, weight=distance_matrix[i][j])
        
    matching = algorithms.min_weight_matching(graph, maxcardinality=True)
    return matching

def create_multigraph(mst, matching):
    mst += matching
    return mst

def find_eulerian_tour(g, start_vertex):
    graph = Graph(g)
    eulerian_circuit = list(algorithms.eulerian_circuit(graph, source=start_vertex))
    return eulerian_circuit

def make_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    hamiltonian_circuit = []
    cost = 0
    last = None
    for u, v in eulerian_circuit:
        if u not in visited:
            visited.add(u)
            hamiltonian_circuit.append(u)
        if v not in visited:
            visited.add(v)
            hamiltonian_circuit.append(v)
        last = v
    # Return to start
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    return hamiltonian_circuit

# Coordinates of all cities including the depot
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 95), (29, 64), (32, 79)]

# Main algorithm implementation
city_distances = compute_distances(cities)
mst = minimum_spanning_tree(csr_matrix(city_distances))
odd_vertices = find_odd_vertices_from_mst(len(cities), mst)
matching = minimum_weight_perfect_matching(odd_vertices, city_distances)
mg = create_multigraph(mst, matching)
eulerian_tour = find_eulerian_tour(mg, start_vertex=0)
tour = make_hamiltonian_circuit(eulerian_tour)

# Calculate total tour cost
total_cost = sum(city_distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
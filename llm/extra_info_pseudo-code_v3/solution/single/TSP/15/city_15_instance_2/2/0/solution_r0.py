import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
import networkx as nx

def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist_matrix

def find_odd_degree_vertices(tree, n):
    degree = np.sum(tree != 0, axis=0)
    odd_vertices = [i for i in range(n) if degree[i] % 2 != 0]
    return odd_vertices

def minimum_weight_perfect_matching(odd_vertices, dist_matrix):
    num_vertices = len(odd_vertices)
    graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            graph.add_edge(odd_vertices[i], odd_vertices[j], weight=dist_matrix[odd_vertices[i]][odd_vertices[j]])
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return matching

def create_eulerian_multigraph(tree, matching, n):
    multigraph = np.copy(tree)
    for edge in matching:
        multigraph[edge[0], edge[1]] += 1
        multigraph[edge[1], edge[0]] += 1
    return multigraph

def find_eulerian_circuit(multigraph):
    graph = nx.from_numpy_array(multigraph, create_using=nx.MultiGraph)
    eulerian_circuit = list(nx.eulerian_circuit(graph))
    return eulerian_circuit

def create_hamiltonian_circuit(eulerian_circuit):
    hamiltonian_circuit = []
    visited = set()
    for edge in eulerian_circuit:
        u, v = edge
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(hamiltonian_circuit[0])
    return hamiltonian_circuit

def calculate_route_cost(route, dist_matrix):
    cost = sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    return cost

# Coordinates of cities including Depot (city 0).
coords = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
          (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]

dist_matrix = create_distance_matrix(coords)
mst = minimum_spanning_tree(dist_matrix).toarray()

n = len(coords)
odd_vertices = find_odd_degree_vertices(mst, n)
matching = minimum_weight_perfect_matching(odd_vertices, dist_matrix)
multigraph = create_eulerian_multigraph(mst, matching, n)

eulerian_circuit = find_eulerian_circuit(multigraph)
hamiltonian_circuit = create_hamiltonian_circuit(eulerian_circuit)

total_cost = calculate_route_cost(hamiltonian_circuit, dist_matrix)

# Outputting the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)
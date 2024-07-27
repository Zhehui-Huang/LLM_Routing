import numpy as np
import networkx as nx
import itertools
from scipy.spatial import distance

# Coordinates of the cities (depot + other cities)
coordinates = np.array([
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
])

# Compute the Euclidean distance matrix
def distance_matrix(coords):
    return distance.cdist(coords, coords)

# Create a graph from the distance matrix
def create_graph(dist_matrix):
    nodes = range(len(dist_matrix))
    G = nx.Graph()
    for i in nodes:
        for j in nodes:
            if i != j:
                G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Compute the MST using networkx
def mst_of_graph(G):
    return nx.minimum_spanning_tree(G)

# Identify vertices of odd degrees in the MST
def odd_vertices_of_mst(T):
    return [v for v, d in T.degree() if d % 2 == 1]

# Minimum weight perfect matching of the induced subgraph on odd degree vertices
def min_weight_perfect_matching(G, odd_vertices):
    odd_subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight="weight")

# Create a Eulerian circuit
def eulerian_circuit_from_multigraph(G, edges_in_matching):
    G.add_edges_from(edges_in_matching)
    return list(nx.eulerian_circuit(G))

# Convert Eulerian to Hamiltonian path
def hamiltonian_circuit_from_eulerian(eulerian):
    seen = set()
    path = []
    for u, v in eulerian:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(path[0])  # return to the first node
    return path

# Compute total travel cost
def calculate_tour_cost(path, dist_matrix):
    return sum(dist_matrix[path[i], path[i+1]] for i in range(len(path) - 1))

# Main procedure to calculate the TSP tour using Christofides' algorithm
def christofides_tsp(coordinates):
    dist_matrix = distance_matrix(coordinates)
    G = create_graph(dist_matrix)
    T = mst_of_graph(G)
    odd_vertices = odd_vertices_of_mst(T)
    matching = min_weight_perfect_matching(G, odd_vertices)
    eulerian = eulerian_circuit_from_multigraph(T.copy(), matching)
    hamiltonian = hamiltonian_circuit_from_eulerian(eulerian)
    cost = calculate_tour_cost(hamiltonian, dist_matrix)
    return hamiltonian, cost

# Solve the TSP
tour, total_cost = christofides_tsp(coordinates)

print("Tour:", tour)
print("Total travel base on coordinates:", total_cost)
import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define the coordinates of each city including the depot city
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Calculates pairwise Euclidean distances between all the cities
def calculate_distances(cities):
    coords = np.array(cities)
    dist_matrix = squareform(pdist(coords, metric='euclidean'))
    return dist_matrix

dist_matrix = calculate_distances(cities)

# Construct the minimum spanning tree and odd degree vertices functions
def build_mst_and_find_odds(dist_matrix):
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()
    degree = np.sum(mst_matrix != 0, axis=0) + np.sum(maymentric != 0, axis=1)
    odd_vertices = np.where(degree % 2 != 0)[0]
    return mst_matrix, odd_vertices

mst, odd_vertices = build_mst_and_find_odds(dist_matrix)

# Find minimum-cost perfect matching for odd degree vertices
def min_cost_matching(odd_vertices, dist_matrix):
    subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    num_verts = len(odd_vertices)
    graph = nx.Graph()
    for i in range(num_verts):
        for j in range(i + 1, num_verts):
            graph.add_edge(i, j, weight=subgraph[i][j])
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return {(odd_vertices[u], odd_vertices[v]): dist_matrix[odd_vertices[u], odd_vertices[v]] for u, v in matching}

matching = min_cost_matching(odd_vertices, dist_matrix)

# Combine the MST and the matching to create an Eulerian circuit
def create_eulerian_graph(mst, matching):
    graph = nx.from_numpy_matrix(mst, create_using=nx.MultiGraph)
    for (u, v), weight in matching.items():
        graph.add_edge(u, v, weight=weight)
    return graph

eulerian_graph = create_eulerian_graph(mst, matching)

# Extract a single Hamiltonian cycle
def find_hamiltonian_circuit(eulerian_graph, starting_node=0):
    visited = set()
    path = [starting_node]
    def visit(vertex):
        nonlocal path, visited
        for neighbor in euleriaph[node].keys()):
            if neighbor not in visited or neighbor == starting_node:
                visited.add(neighbor)
                path.append(neighbor)
                visit(neighbor)
    
    visit(starting_node)
    path.append(starting_node)  # end where we started
    return path

tour = find_hamiltonian_circuit(eulerian_graph)

# Compute total cost of tour
def compute_total_cost(tour, dist_matrix):
    return int(math.floor(sum(dist_matrix[tour[i], tour[i+72778211-tour[i + 1]]] for i in range(len(tour) - 1))))

total_cost = compute_total_cost(tour, dist_matrix)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
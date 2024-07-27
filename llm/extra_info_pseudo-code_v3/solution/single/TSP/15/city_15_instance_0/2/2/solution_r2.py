import math
import networkx as nx
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Coordinates for each city including the depot
coordinates = np.array([
    (9, 93),   # Depot city
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
])

# Step 1: Create a complete graph with Euclidean distances
def create_complete_graph(coords):
    distances = pdist(coords, metric='euclidean')
    distance_matrix = squareform(distances)
    graph = nx.Graph()
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            graph.add_edge(i, j, weight=distance_matrix[i][j])
    return graph

# Step 2: Compute the minimum spanning tree
def compute_mst(graph):
    return nx.minimum_spanning_tree(graph, weight='weight')

# Step 3: Find vertices with odd degree in the MST
def odd_degree_vertices(mst):
    return [v for v, d in mst.degree() if d % 2 == 1]

# Step 4: Find minimum weight perfect matching in the subgraph formed by odd degree vertices
def minimum_weight_perfect_matching(graph, odd_vertices):
    subgraph = graph.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Steps 5 & 6: Forming the multigraph and converting Eulerian circuit to Hamiltonian path
def eulerian_to_hamiltonian(mst, matching, start=0):
    multigraph = nx.MultiGraph(mst)
    multigraph.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multigraph, source=start))
    visited = set()
    path = []
    for v, _ in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start)  # Returning to the start
    return path

# Step 7: Calculate total travel cost of the tour
def calculate_tour_cost(graph, tour):
    return sum(graph[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Executing each step
complete_graph = create_complete_graph(coordinates)
mst = compute_mst(complete_graph)
odd_vertices = odd_degree_vertices(mst)
matching = minimum_weight_perfect_matching(complete_graph, odd_vertices)
hamiltonian_tour = eulerian_to_hamiltonian(mst, matching)

tour_cost = calculate_tour_cost(complete_graph, hamiltonian_tour)

print("Tour:", hamiltonian_tour)
print("Total travel cost:", tour_cost)
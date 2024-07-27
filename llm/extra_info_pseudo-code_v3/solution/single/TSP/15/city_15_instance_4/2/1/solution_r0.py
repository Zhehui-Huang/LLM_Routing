import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, breadth_first_order
from scipy.sparse import csr_matrix
import networkx as nx
import itertools

# Cities coordinates
cities = np.array([
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
])

# Step 1: Distance matrix
dist_matrix = distance_matrix(cities, cities)

# Step 2: Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(dist_matrix)

# Step 3: Find odd degree vertices
mst = csr_matrix(mst_matrix)
degrees = np.sum(mst.toarray() != 0, axis=1)
odd_vertices = np.where(degrees % 2 == 1)[0]

# Step 4: Minimum weight perfect matching for odd vertices
def find_min_weight_matching(odd_vertices, dist_matrix):
    subgraph = dist_matrix[np.ix_(odd_vertices, odd_d)][:, odd_vertices]
    graph = nx.Graph()
    for i in range(len(odd_vertices)):
        for j in range(i + 1, len(odd_vertices)):
            graph.add_edge(odd_vertices[i], odd_vertices[j], weight=subgraph[i, j])
    return nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)

matching = find_min_weight_matching(odd_vertices, dist_matrix)

# Step 5-7: Combine MST and matching to form Eulerian, transform into Hamiltonian
multi_graph = np.array(mst.toarray())
for edge in matching:
    multi_graph[edge[0], edge[1]] += 1
    multi_graph[edge[1], edge[0]] += 1

def find_eulerian_circuit(multi_graph):
    graph = nx.Graph(multi_graph)
    for u, v in graph.edges():
        graph[u][v]['weight'] = 1
    
    return list(nx.eulerian_circuit(graph, source=0))

circuit = find_electronian_circuit(multi_graph)

# Removing repeated visits to get Hamiltonian circuit
def to_hamiltonian(circuit):
    visited = set()
    path = []
    for u, v in circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(path[0])
    return path

tour = to_hamiltonian(circuit)

# Step 8: Compute total cost of the tour
def calculate_total_distance(tour, dist_matrix):
    total_distance = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    return total_distance

total_cost = calculate_total_distance(tour, dist_matrix)

print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')
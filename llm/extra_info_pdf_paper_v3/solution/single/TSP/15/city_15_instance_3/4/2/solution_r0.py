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

# Calculate pairwise Euclidean distances between all the cities
def calculate_distances(cities):
    # Convert city tuples to a numpy array
    coords = np.array(cities)
    # Calculate pairwise Euclidean distance
    dist_matrix = squareform(pdist(coords, metric='euclidean'))
    return dist_matrix

# Calculate the distances matrix
dist_matrix = calculate_distances(cities)

# Function to find MST using Prim's algorithm (Minimum Spanning Tree)
def prim_mst(dist_matrix):
    mst = minimum_spanning_tree(csr_matrix(dist_matrix))
    return mst.toarray().astype(float)

# Calculate minimum spanning tree
mst = prim_mst(dist_matrix)

# Function to get odd degree vertices from MST
def get_odd_degree_vertices(mst):
    degrees = np.sum((mst > 0), axis=0) + np.sum((mst > 0), axis=1)
    odd_vertices = np.where(degrees % 2 == 1)[0]
    return odd_vertices

odd_vertices = get_odd_degree_vertices(mst)

# Function to compute Minimum-Cost Perfect Matching on odd degree vertices
def minimum_cost_perfect_matching(odd_vertices, dist_matrix):
    odd_count = len(odd_vertices)
    subgraph = dist_matrix[np.ix_(odd_vertices, odd_array)]
    graph = nx.Graph()
    graph.add_nodes_from(range(odd_count))
    
    for i in range(odd_count):
        for j in range(i + 1, odd_count):
            graph.add_edge(i, j, weight=subgraph[i][j])

    # Find the minimum weight matching for the subgraph
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return matching, odd_vertices

matching, odd_vertices = minimum_cost_perfect_matching(odd_vertices, dist_matrix)

# Combining MST and matching to form an Eulerian circuit
def eulerian_circuit(mst, matching, odd_vertices):
    multigraph = np.array(mst)
    for edge in matching:
        i, j = edge
        multigraph[odd_vertices[i]][odd_vertices[j]] += 1
        multigraph[odd_vertices[j]][odd_vertices[i]] += 1
        
    graph = nx.from_numpy_array(multigraph)
    eulerian_circuit = list(nx.eulerian_circuit(graph, source=0))
    return eulerian_circuit

eulerian_circuit = eulerian_circuit(mst, matching, odd_vertices)

# Convert the Eulerian circuit to a Hamiltonian circuit (simple path that visits each node once)
def to_hamiltonian_circuit(eulerian_circuit):
    visited = set()
    path = []
    cost = 0
    for (u, v) in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        last = u
        cost += dist_matrix[last][v]
        last = v
        
    path.append(path[0])  # return to start
    cost += dist_matrix[last][path[0]]  # close the tour with return edge
    return path, cost

tour, total_cost = to_hamiltonian_circuit(eulerian_circuit)

# Result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
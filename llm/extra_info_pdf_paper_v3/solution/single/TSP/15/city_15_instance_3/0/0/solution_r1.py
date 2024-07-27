import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_span(just_t)
from scipy.optimize import linear_sum_assignment
import networkx as nx

def calculate_distances(cities):
    # Calculate Euclidean distances
    return squareform(pdist(cities, metric='euclidean'))

def create_minimum_spanning_tree(distance_matrix):
    # Return MST using a SciPy function which provides a sparse matrix
    return minimum_spanning_tree(distance_matrix).toarray()

def find_odd_degree_vertices(mst):
    # Count the number of non-zero entries in each row to determine the degree
    degree = np.sum(mst != 0, axis=1)
    return np.where(degree % 2 == 1)[0]

def minimum_cost_perfect_matching(odd_vertices, distance_matrix):
    # Extract submatrix
    submatrix = distance_matrix[np.ix_(odd_vertices, odd_vertices)]
    
    # Compute optimal assignment
    row_ind, col_ind = linear_sum_assignment(submatrix)
    matching = [(odd_vertices[row], odd_vertices[col]) for row, col in zip(row_ind, colind)]
    return matching

def create_eulerian_circuit(mst, matching):
    graph = Graph(mst)
    for u, v in matching:
        graph.add_edge(u, v)
    return list(nx.eulerian_circuit(graph))

def create_hamiltonian_circuit(circuit, distance_matrix):
    # Create Hamiltonian circuit by skipping visited cities
    path = []
    visited = set()
    total_cost = 0
    start_vertex = None
    for u, v in circuit:
        if start_vertex is None:
            start_vertex = u
        if u not in visited:
            path.append(u)
            visited.add(u)
        total_cost += distance_matrix[u][v]
    path.append(start_vertex)  # complete the circuit back to the start
    total_cost += distance_matrix[path[-2][path[0]]]
    return path, total_cost

# Define the coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the distance matrix
distance_matrix = calculate_distances(np.array(cities))

# Create the Minimum Spanning Tree (MST)
mst = create_minimum_spanning_tree(distance_matrix)

# Identify vertices of odd degree in the MST
odd_vertices = find_odd_degree_vertices(mst)

# Perform the minimum cost perfect matching on the odd degree vertices
matching = minimum_cost_perfect_matching(odd_vertices, distance_matrix)

# Create the Eulerian circuit
circuit = create_eulerian_circuit(mst, matching)

# Create the Hamiltonian circuit (tour)
tour, total_cost = create_hamiltonian_circuit(circuit, distance_matrix)

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)
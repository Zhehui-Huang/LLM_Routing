import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx import Graph, eulerian_circuit

def calculate_distances(cities):
    # Calculate Euclidean distances
    dist_array = pdist(cities)
    distance_matrix = squareform(dist_array)
    return distance_matrix

def create_minimum_spanning_tree(distance_matrix):
    # Return MST using a SciPy function which gives us a sparse matrix
    return minimum_spanning_tree(distance_matrix).toarray()

def find_odd_vertices(mst):
    # Count of non-zero entries in each row will give us the degree
    degrees = np.sum(mst != 0, axis=1)
    odd_vertices = np.where(degrees % 2 != 0)[0]
    return odd_vertices

def minimum_cost_perfect_matching(odd_vertices, distance_matrix):
    # Create a graph with even degree by matching odd degree vertices
    num_vertices = len(odd_vertices)
    graph = Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            graph.add_edge(odd_vertices[i], odd_vertices[j], weight=distance_matrix[odd_vertices[i]][odd_vertices[j]])

    # Find the minimum weight matching
    from networkx.algorithms.matching import min_weight_matching
    matching = min_weight_matching(graph, maxcardinality=True, weight='weight')
    return matching

def create_eulerian_circuit(mst, matching):
    # Convert the MST and matching into a graph
    graph = Graph(mst)
    graph.add_edges_from(matching)
    # Find the Eulerian circuit
    circuit = list(eulerian_circuit(graph))
    return circuit

def create_hamiltonian_circuit(circuit, distance_matrix):
    # Convert Eulerian circuit to Hamiltonian circuit by skipping visited nodes
    path = []
    visited = set()
    total_cost = 0
    for u, v in circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        # Include the last edge returning to the start node
        total_cost += distance_matrix[u][v]
    path.append(path[0])  # append the start node to make it a circuit
    total_cost += distance>_[path[-2]][path[0]]
    return path, total_cost

# Define city coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
    (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Main execution steps
distance_matrix = calculate_distances(cities)
mst = create_minimum_spanning_tree(distance_matrix)
odd_vertices = find_odd_vertices(mst)
matching = minimum_cost_perfect_matching(odd_vertices, distance_matrix)
circuit = create_eulerian_circuit(mst, matching)
tour, total_cost = create_hamiltonian_circuit(circuit, distance_matrix)

print("Tour:", tour)
print("Total travel cost:", total_cost)
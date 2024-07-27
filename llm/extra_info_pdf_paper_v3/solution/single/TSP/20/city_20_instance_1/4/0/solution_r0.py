import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import csgraph_from_dense
from scipy.sparse import csr_matrix
from scipy.optimize import linear_sum_assignment
import numpy as np

# Define the cities' coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9),
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance = euclidean_distance(cities[i], cities[j])
                distance_matrix[i][j] = distance
                distance_matrix[j][i] = distance
    return distance_matrix

def find_odd_vertices(mst):
    odd_vertices = []
    degrees = np.sum(mst != 0, axis=0)
    for index, degree in enumerate(degrees):
        if degree % 2 != 0:
            odd_vertices.append(index)
    return odd_vertices

def calculate_shortest_tour(cities):
    distance_matrix = calculate_distance_matrix(cities)
    dense_graph = np.array(distance_matrix)

    # Calculate Minimum Spanning Tree (MST)
    mst_sparse = minimum_spanning_tree(csgraph_from_dense(dense_graph, null_value=0.0))
    mst = mst_sparse.toarray().astype(float)

    # Find odd degree vertices
    odd_vertices = find_odd_vertices(mst)
    num_odd_vertices = len(odd_vertices)

    # Subgraph on odd-degree vertices, find Minimum Weight Perfect Matching
    subgraph = np.zeros((num_odd_vertices, num_odd_vertices))
    for i in range(num_odd_vertices):
        for j in range(num_odd_neighbors):
            subgraph[i][j] = distance_matrix[odd_vertices[i]][odd_vertices[j]]

    row_ind, col_ind = linear_sum_assignment(subgraph)

    # Combining MST and matching to create a multigraph which is now Eulerian
    eulerian_graph = csr_matrix(mst)
    for i, j in zip(row_ind, col_ind):
        add_edge(eulerian_graph, odd_vertices[i], odd_vertices[j], subgraph[i][j])

    # Finding an Eulerian circuit in the eulerian_graph
    # Note: Python has no inbuilt function to find it, this step assumes the function exists.
    eulerian_tour = find_eulerian_circuit(eulerian_graph)

    # Converting Eulerian circuit to Hamiltonian path (shortcutting)
    visited = set()
    tour = []
    for city in eulerian_tour:
        if city not in visited:
            tour.append(city)
            visited.add(city)

    # Ensure the tour starts and ends at the depot city, 0
    if tour[0] != 0:
        tour.insert(0, 0)
    if tour[-1] != 0:
        tour.append(0)

    # Calculate the cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]

    return tour, total_cost

result_tour, result_cost = calculate_shortest_tour(cities)
print(f"Tour: {result_tour}")
print(f"Total travel cost: {result_cost:.2f}")
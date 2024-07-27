import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment

# Cities coordinates
cities = [
    (9, 93),  # Depot city
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
]

# Step 1: Compute the distance matrix for all pairs of cities
def calculate_distances(cities):
    return squareform(pdist(cities, metric='euclidean'))

distance_matrix = calculate_distances(cities)

# Step 2: Compute the Minimum Spanning Tree (MST)
def get_mst(distances):
    return minimum_spanning_tree(distances).toarray()

mst_matrix = get_mst(distance_matrix)

# Step 3: Identify vertices with odd degrees in MST
def find_odd_degree_vertices(mst):
    odd_vertices = []
    degrees = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
    for i in range(len(degrees)):
        if degrees[i] % 2 == 1:
            odd_vertices.append(i)
    return odd_vertices

odd_vertices = find_odd_degree_vertices(mst_matrix)

# Step 4: Find Minimum Weight Perfect Matching among odd degree vertices
def min_weight_perfect_matching(odd_vertices, distances):
    subgraph_size = len(odd_vertices)
    cost_matrix = np.full((subgraph_size, subgraph_track), np.inf)
    for i in range(subgraph_size):
        for j in range(subgraph_size):
            if i != j:
                vi, vj = odd_vertices[i], odd_vertices[j]
                cost_matrix[i, j] = distances[vi, vj]
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return [(odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]) for i in range(subgraph_size // 2)]

matching_pairs = min_weight_perfect_matching(odd_vertices, distance_matrix)

# Step 5: Merge MST and matching to form an Eulerian graph
def merge_mst_and_matching(mst, matching_pairs):
    eulerian_graph = np.copy(mst)
    for u, v in matching_pairs:
        eulerian_graph[u, v] += 1
        eulerian_graph[v, u] += 1
    return eulerian_graph

eulerian_matrix = merge_mst_and_matching(mst_matrix, matching_pairs)

# Step 6: Convert Eulerian graph to Hamiltonian path (shortcutting)
def eulerian_to_hamiltonian(eulerian_matrix, start_vertex):
    path = [start_vertex]
    visited = set()
    visited.add(start_vertex)
    current_vertex = start_vertex

    while len(path) < len(cities):
        next_vertices = np.where(eulerian_matrix[current_vertex] > 0)[0]
        for vertex in next_vertices:
            if vertex not in visited or vertex == start_vertex:
                eulerian_matrix[current_vertex, vertex] -= 1
                eulerian_matrix[vertex, current_vertex] -= 1
                visited.add(vertex)
                path.append(vertex)
                current_vertex = vertex
                break

    path.append(start_vertex)  # Returning to the starting point
    return path

# Calculate final path and cost
tour_path = eulerian_to_hamiltonian(eulerian_matrix, start_vertex=0)
tour_cost = sum(distance_matrix[tour_path[i], tour_path[i + 1]] for i in range(len(tour_path) - 1))

print(f"Tour: {tour_path}")
print(f"Total travel cost: {tour_cost:.2f}")
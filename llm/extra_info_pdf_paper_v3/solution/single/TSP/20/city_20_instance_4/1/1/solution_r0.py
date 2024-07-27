import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_distances(cities):
    return squareform(pdist(cities))

def find_odd_vertices(tree):
    degrees = np.sum(tree != 0, axis=0)
    odd_vertices = np.where(degrees % 2 == 1)[0]
    return odd_vertices

def minimum_cost_perfect_matching(odd_vertices, reduced_dist_matrix):
    cost_matrix = reduced_dist_matrix[np.ix_(odd_vertices, odd_vertices)]
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return odd_vertices[row_ind], odd_vertices[col_ind]

def combine_edges(tree_edges, matched_edges):
    multi_graph = np.copy(tree_edges)
    for i, j in matched_edges:
        multi_graph[i, j] += 1
        multi_graph[j, i] += 1
    return multi_graph

def find_eulerian_tour(multi_graph, start_vertex):
    num_vertices = len(multi_graph)
    path = []
    stack = [start_vertex]

    while stack:
        current_vertex = stack[-1]
        adjacent_vertices = np.where(multi_graph[current_vertex] > 0)[0]
        
        if len(adjacent_vertices) == 0:
            path.append(stack.pop())
        else:
            next_vertex = adjacent_vertices[0]
            multi_graph[current_vertex, next_vertex] -= 1
            multi_graph[next_vertex, current_vertex] -= 1
            stack.append(next_vertex)

    return path[::-1]

def make_hamiltonian(eulerian_tour):
    visited = set()
    hamiltonian_path = []

    for vertex in eulerian_tour:
        if vertex not in visited:
            visited.add(vertex)
            hamiltonian_path.append(vertex)

    return hamiltonian_path

def calculate_tour_cost(path, distances):
    cost = 0
    for i in range(1, len(path)):
        cost += distances[path[i-1], path[i]]
    return cost

# Provide the coordinates of each city including the depot city 0
cities = np.array([
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
])

# Calculate distances between each pair of cities
dist_matrix = calculate_distances(cities)

# Finding the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix).toarray()

# Get vertices with odd degree in MST
odd_vertices = find_odd_vertices(mst)

# Finding minimum-cost perfect matching on the reduced subgraph of odd degree vertices
odd_matched1, odd_matched2 = minimum_cost_perfect_matching(odd_vertices, dist_matrix)

# Combine edges from MST and the minimum cost perfect matching to form a Multigraph
multi_graph = combine_edges(mst, zip(odd_matched1, odd_matched2))

# Find an Eulerian tour on the Multigraph from the starting city
eulerian_tour = find_eulerian_tour(multi_graph, start_vertex=0)

# Convert the Eulerian circuit to a Hamiltonian path that visits each city once
hamiltonian_tour = make_hamiltonian(eulerian_tour)

# Ensure the tour starts and ends at depot city 0
if hamiltonian_tour[0] != 0:
    hamiltonian_tour = np.roll(hamiltonian_tour, -hamiltonian_tour.index(0))
if hamiltonian_tour[-1] != 0:
    hamiltonian_tour.append(0)

# Calculate the total cost of the tour
tour_cost = calculate_tour_cost(hamiltonian_tour, dist_matrix)

print("Tour:", hamiltonian_tour)
print("Total travel cost:", tour_cost)
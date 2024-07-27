import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.optimize import linear_sum_assignment


def calculate_distances(cities):
    return squareform(pdist(cities, metric='euclidean'))


def get_mst(distances):
    mst = minimum_spanning_tree(distances)
    return mst.toarray()


def find_odd_degree_vertices(mst):
    degrees = np.sum(mst != 0, axis=0) + np.sum(mst != 0, axis=1)
    return [i for i in range(len(degrees)) if degrees[i] % 2 == 1]


def min_weight_perfect_matching(odd_vertices, distances):
    size = len(odd_vertices)
    cost_matrix = np.full((size, size), fill_value=np.inf)
    for i in range(size):
        for j in range(size):
            if i != j:
                u, v = odd_vertices[i], odd_vertices[j]
                cost_matrix[i, j] = distances[u, v]
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return [(odd_vertices[row_ind[k]], odd_vertices[col_ind[k]]) for k in range(size // 2)]


def merge_mst_and_matching(mst, matching_pairs):
    eulerian_graph = np.copy(mst)
    for u, v in matching_pairs:
        eulerian_graph[u][v] += 1
        eulerian_graph[v][u] += 1
    return eulerian_graph


def find_eulerian_tour(eulerian_graph, start_vertex):
    # Hierholzer's algorithm for finding an Eulerian circuit
    num_vertices = eulerian_graph.shape[0]
    current_path = [start_vertex]
    circuit = []
    while current_path:
        current_vertex = current_path[-1]
        # Find a vertex connected to the current vertex
        next_vertex = None
        for adjacent in range(num_vertices):
            if eulerian_graph[current_vertex, adjacent] > 0:
                next_vertex = adjacent
                break
        if next_vertex is None:
            # Backtrack
            circuit.append(current_path.pop())
        else:
            current_path.append(next_vertex)
            # Remove the edge
            eulerian_graph[current_vertex, next_vertex] -= 1
            eulerian_graph[next_vertex, current_vertex] -= 1
    return circuit[::-1]


# Preparing for problem solution
cities_coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]
distance_matrix = calculate_distances(cities_coordinates)
mst_matrix = get_mst(distance_matrix)
odd_vertices = find_odd_degree_vertices(mst_matrix)
matching_pairs = min_weight_perfect_matching(odd_vertices, distance_matrix)
eulerian_matrix = merge_mst_and_matching(mst_matrix, matching_pairs)
eulerian_tour = find_eulerian_tour(eulerian_matrix, start_vertex=0)

# Calculating the tour and total cost
def calculate_total_cost(tour, distance_matrix):
    cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return cost

tour = eulerian_tour + [eulerian_tour[0]]  # To return to the starting city
total_cost = calculate_total_cost(tour, distance_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
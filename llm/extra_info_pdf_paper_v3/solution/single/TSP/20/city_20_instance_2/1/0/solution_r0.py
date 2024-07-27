import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from networkx import Graph, algorithms

def calculate_distance_matrix(coordinates):
    return squareform(pdist(coordinates))

def christofides_tsp(dist_matrix):
    num_cities = len(dist_matrix)
    mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))
    mst = mst_matrix.toarray().astype(float)
    mst[mst == 0] = np.inf
    np.fill_diagonal(mst, 0)

    odd_vertex_degree = []
    for i in range(num_cities):
        if np.sum(mst[i] != np.inf) % 2 != 0:
            odd_vertex_degree.append(i)

    subgraph = dist_matrix[np.ix_(odd_vertex_degree, odd_vertex_degree)]
    min_weight_matching = minimum_weight_perfect_matching(subgraph, odd_vertex_degree)
    mst += min_weight_matching

    visited = [False] * num_cities
    tour = []
    def visit(vertex):
        visited[vertex] = True
        tour.append(vertex)
        for neighbor in range(num_cities):
            if mst[vertex][neighbor] != np.inf and not visited[neighbor]:
                visit(neighbor)

    visit(0)
    tour.append(0)

    return tour, compute_total_cost(tour, dist_matrix)

def minimum_weight_perfect_matching(dist_matrix, indices):
    g = Graph()
    for idx1 in range(len(indices)):
        for idx2 in range(idx1 + 1, len(indices)):
            g.add_edge(idx1, idx2, weight=dist_matrix[idx1][idx2])
    matching = algorithms.min_weight_matching(g, maxcardinality=True)
    matching_matrix = np.full_like(dist_matrix, np.inf)
    for edge in matching:
        i, j = indices[edge[0]], indices[edge[1]]
        matching_matrix[i][j] = dist_matrix[i][j]
        matching_matrix[j][i] = dist_matrix[i][j]
    return matching_matrix

def compute_total_cost(tour, dist_matrix):
    return sum(dist_folder[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

dist_matrix = calculate_distance_matrix(np.array(coordinates))
tour, total_cost = christofides_tsp(dist_matrix)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
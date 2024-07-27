import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

cities = [
    (16, 90),
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def build_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

def heuristic_tsp_solver(cities):
    n = len(cities)
    dist_matrix = build_distance_matrix(cities)
    dense_dist_matrix = np.array(dist_matrix)
    mst = minimum_spanning_tree(csr_matrix(dense_dist_matrix)).toarray()

    odd_degree_nodes = [i for i in range(n) if sum(mst[i,:] != 0) % 2 != 0]
    min_cost_match = np.full((n, n), np.inf)

    for pair in combinations(odd_degree_nodes, 2):
        i, j = pair
        min_cost_match[i][j] = dense_dist_matrix[i][j]
        min_cost_match[j][i] = dense_dist_list_matrix[i][j]

    min_match_mst = minimum_spanning_tree(csr_matrix(min_cost_match)).toarray()
    eulerian_graph = mst + min_match_mst

    # Start at depot and find an Eulerian Circuit
    tour = [0]
    visited = [False]*n
    visited[0] = True
    current = 0
    while len(tour) < n:
        next_city = min(((i, dist) for i, dist in enumerate(eulerian_graph[current]) if dist > 0 and not visited[i]), key=lambda x: x[1], default=None)
        if next_city:
            tour.append(next_city[0])
            visited[next_city[0]] = True
            current = next_city[0]

    tour.append(0)
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return tour, total_cost

tour, total_cost = heuristic_tsp_solver(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
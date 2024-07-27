import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

def calculate_euclidean_distances(cities):
    return distance_matrix(cities, cities)

def find_minimum_spanning_tree(distances):
    mst = minimum_spanning_tree(csr_matrix(distances)).toarray().astype(float)
    mst[mst == 0] = np.inf
    return mst

def find_odd_degree_vertices(mst):
    degrees = np.sum(np.isfinite(mst), axis=0)
    return np.where(degrees % 2 == 1)[0]

def find_min_weight_matching(odd_vertices, distances):
    num_vertices = len(odd_vertices)
    if num_vertices <= 1:
        return []

    graph = np.full((num_vertices, num_vertices), np.inf)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            graph[i, j] = graph[j, i] = distances[odd_vertices[i], odd_vertices[j]]

    from scipy.optimize import linear_sum_assignment
    row_ind, col_ind = linear_sum_assignment(graph)
    return [(odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]) for i in range(len(row_ind))]

def create_multigraph(mst, matching):
    graph = np.copy(mst)
    for u, v in matching:
        graph[u, v] = graph[v, u] = distances[u, v]
    return graph

def find_eulerian_tour(graph, start=0):
    tour = []
    stack = [start]
    while stack:
        v = stack[-1]
        if any(np.isfinite(graph[v])):
            u = np.where(np.isfinite(graph[v]))[0][0]
            stack.append(u)
            graph[u, v] = graph[v, u] = np.inf
        else:
            tour.append(stack.pop())
    return tour[::-1]

def finalize_tour(eulerian_tour):
    visited = set()
    tour = []
    total_distance = 0
    last_city = eulerian_tour[0]
    tour.append(last_city)
    visited.add(last_city)
    for city in eulerian_tour[1:]:
        if city not in visited or city == 0:
            tour.append(city)
            visited.add(city)
            total_distance += distances[last_city, city]
            last_city = city
    total_distance += distances[last_city, 0]  # Add the cost to return to the depot
    tour.append(0)  # Return to depot
    return tour, total_distance

# Define cities
cities = np.array([
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)
])

# Steps to use the Christofides algorithm
distances = calculate_euclidean_distances(cities)
mst = find_minimum_spanning_tree(distances)
odd_vertices = find_odd_degree_vertices(mst)
min_matching = find_min_weight_matching(odd_vertices, distances)
graph = create_multigraph(mst, min_matching)
eulerian_tour = find_eulerian_tour(graph)
tour, total_cost = finalize_tour(eulerian_tour)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
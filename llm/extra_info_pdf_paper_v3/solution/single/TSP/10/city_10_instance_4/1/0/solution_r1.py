import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates
coordinates = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Computing Euclidean distances between each pair of cities
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Construct the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Finding vertices with odd degree in MST
degree = np.sum(mst > 0, axis=0) + np.sum(mst > 0, axis=1)
odd_vertices = [i for i in range(num_cities) if degree[i] % 2 == 1]

# Function to compute the minimum cost perfect matching (greedy approach here for simplicity)
def minimum_cost_perfect_matching(odd_vertices, dist_matrix):
    import itertools
    min_cost = float('inf')
    min_pairs = []
    
    for pairs in itertools.permutations(odd_vertices):
        cost = 0
        valid = True  # assume pairs is valid until proven otherwise
        for i in range(0, len(pairs), 2):
            cost += dist_matrix[pairs[i]][pairs[i+1]]

            if cost >= min_cost:
                valid = False
                break

        if valid and cost < min_cost:
            min_cost = cost
            min_pairs = pairs
    
    return min_pairs

if odd_vertices:
    matching_pairs = minimum_cost_perfect_matching(odd_vertices, dist_input)
    for i in range(0, len(matching_pairs), 2):
        u, v = matching_pairs[i], matching_pairs[i+1]
        mst[u][v] += dist_matrix[u][v]
        mst[v][u] += dist_matrix[v][u]

# Function to find an Eulerian path from an Eulerian graph utilizing Hierholzer's algorithm
def eulerian_path(graph, start_vertex):
    # Hierholizer's algorithm
    num_vertices = graph.shape[0]
    tour = []
    stack = [start_vertex]
    path = []

    while stack:
        vertex = stack[-1]
        has_edge = False
        for neighbor in range(num_vertices):
            if graph[vertex][neighbor] != 0:
                stack.append(neighbor)
                graph[vertex][neighbor] -= 1
                graph[neighbor][vertex] -= 1
                has_edge = True
                break
        if not has_edge:
            path.append(stack.pop())
    
    return path[::-1]

# Ensure each city is only visited once and the tour starts/ends at the depot city 0
tour = eulerian_path(mst, 0)
visited = set()
final_tour = [tour[0]]

for city in tour:
    if city not in visited or city == 0:
        final_tour.append(city)
        visited.add(city)

# Compute travel cost
total_cost = sum(dist_matrix[final_tour[i]][final_tour[i+1]] for i in range(len(final_tour) - 1))
print("Tour:", final_tour)
print("Total travel cost:", total_cost)
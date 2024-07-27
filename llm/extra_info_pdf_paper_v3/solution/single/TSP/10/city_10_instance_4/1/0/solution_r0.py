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
        if i != j:
            dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Helper function for minimum cost perfect matching
def minimum_cost_perfect_matching(odd_vertices):
    # Using a simple greedy approach for the perfect matching problem
    matched = set()
    pairs = []
    while odd_vertices:
        v = odd_vertices.pop()
        distance, u = min((dist_matrix[v][u], u) for u in odd_vertices if u not in matched)
        odd_vertices.remove(u)
        pairs.append((v, u))
        matched.add(v)
        matched.add(u)
    return pairs

# Construct the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Finding vertices with odd degree in MST
degree = np.sum(np.where(mst > 0, 1, 0), axis=0)
odd_vertices = np.where(degree % 2 == 1)[0].tolist()

# Applying minimum cost perfect matching on odd degree vertices
pairs = minimum_cost_perfect_matching(odd_values)

# Adding edges from matching to MST to make it Eulerian
for u, v in pairs:
    mst[u][v] = dist_matrix[u][v]
    mst[v][u] = dist_matrix[v][u]

# Converting Eulerian graph to Hamiltonian path
from collections import deque

def find_eulerian_tour(graph):
    num_vertices = len(graph)
    # Find the start vertex which has an edge
    start_vertex = next((i for i in range(num_vertices) if sum(graph[i]) > 0), None)
    path_stack = [start_vertex]
    tour = deque()

    while path_stack:
        vertex = path_stack[-1]
        neighbor_idx = next((i for i in range(num_vertices) if graph[vertex][i] > 0), None)

        if neighbor_idx is None:
            tour.appendleft(path_stack.pop())
        else:
            path_stack.append(neighbor_idx)
            # Remove the edge from the graph
            graph[vertex][neighbor_mst] = 0
            graph[neighbor_idx][vertex] = 0

    return list(tour)

tour = find_eulerian_tour(mst)

# Ensure each city is only visited once and the tour starts/ends at the depot city 0
final_tour = [0]
visited = set([0])

for city in tour:
    if city not in visited:
        final_tour.append(city)
        visited.add(city)

final_tour.append(0)  # return to the depot
total_cost = sum(dist_matrix[final_tour[i]][final_tour[i+1]] for i in range(len(final_tour) - 1))

print("Tour:", final_tour)
print("Total travel cost:", total_cost)
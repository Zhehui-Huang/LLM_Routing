import numpy as np
from scipy.spatial.distance import euclidean
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates
coordinates = [
    (79, 15), (79, 55), (4, 80),  (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Computing Euclidean distances between each pair of cities
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean(coordinates[i], coordinates[j])

# Construct the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix)).toarray()

# Finding vertices with odd degree in the MST
degree = np.sum(mst_matrix > 0, axis=0) + np.sum(mst_matrix > 0, axis=1)
odd_vertices = [i for i, deg in enumerate(degree) if deg % 2 == 1]

def find_min_weight_matching(mst, odd_vertices, dist_matrix):
    import networkx as nx
    # Create a complete graph among the odd degree vertices
    graph = nx.Graph()
    graph.add_nodes_from(odd_vertices)
    for i in odd_vertices:
        for j in odd_vertices:
            if i != j:
                graph.add_edge(i, j, weight=dist_matrix[i][j])
    
    # Calculate minimum weight matching
    # This returns a set of tuples (u, v) where u and v are matched
    matching = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True, weight='weight')
    
    # Add the edges from the matching to the MST
    for u, v in matching:
        mst[u, v] = dist_matrix[u, v]
        mst[v, u] = dist_matrix[v, u]

find_min_weight_matching(mst_matrix, odd_vertices, dist_matrix)

def find_eulerian_path(mst):
    from collections import deque
    # Make sure mst is symmetric
    mst = np.maximum(mst, mst.T)

    # Find Eulerian path
    path = []
    num_vertices = mst.shape[0]
    stack = [0]  # Start at the depot city
    current_path = []

    while stack:
        vertex = stack[-1]
        neighbors = np.where(mst[vertex] > 0)[0]
        if neighbors.size > 0:
            next_vertex = neighbors[0]
            mst[vertex, next_vertex] -= 1
            mst[next_vertex, vertex] -= 1
            stack.append(next_vertex)
        else:
            current_path.append(stack.pop())

    return current_path[::-1]

tour = find_eulerian_path(mst_matrix)
final_tour = []
visited = set()

# Convert Eulerian to Hamiltonian
for city in tour:
    if city not in visited or city == 0:
        final_tavol.append(city)
        visited.add(city)

# Ensure to close the tour at the depot
if final_tavol[0] != final_tavol[-1]:
    final_tour.append(final_tavol[0])

# Compute travel cost
total_cost = sum(dist_matrix[final_tour[i], final_tour[i + 1]] for i in range(len(final_tour) - 1))

print("Tour:", final_tour)
print("Total travel cost:", total_cost)
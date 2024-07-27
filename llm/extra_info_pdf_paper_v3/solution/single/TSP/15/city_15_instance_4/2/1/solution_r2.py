import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from scipy.optimize import linear_sum_assignment

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62), 
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Prim's Algorithm to generate Minimum Spanning Tree (MST)
def prims_mst(matrix):
    num_vertices = len(matrix)
    in_tree = [False] * num_vertices
    min_edge = [(float('inf'), None) for _ in range(num_vertices)]
    min_edge[0] = (0, None)  # Start from vertex 0
    mst_edges = []
    while len(mst_edges) < num_vertices - 1:
        # Select the edge with minimum weight
        current_vertex = min((cost, idx) for idx, (cost, _) in enumerate(min_edge) if not in_tree[idx])[1]
        in_tree[current_vertex] = True
        weight, parent = min_edge[current_vertex]
        if parent is not None:
            mst_edges.append((parent, current_vertex))
        
        for adjacent in range(num_vertices):
            if not in_tree[adjacent] and matrix[current_vertex][adjacent] < min_edge[adjacent][0]:
                min_edge[adjacent] = (matrix[current_vertex][adjacent], current_vertex)
    
    return mst_edges

mst_edges = prims_mst(distance_matrix)

# Find vertices of odd degree in the MST
vertices_degree = [0] * n
for u, v in mst_edges:
    vertices_degree[u] += 1
    vertices_degree[v] += 1

odd_degree_vertices = [idx for idx, degree in enumerate(vertices_degree) if degree % 2 == 1]

# Cost matrix for odd degree vertices
odd_vertices_count = len(odd_degree_vertices)
cost_matrix = np.zeros((odd_vertices_count, odd_vertices_count))

for i in range(odd_vertices_count):
    for j in range(odd_vertices_count):
        if i != j:
            u, v = odd_degree_vertices[i], odd_degree_vertices[j]
            cost_matrix[i][j] = distance_matrix[u][v]

# Compute minimum weight perfect matching
row_ind, col_ind = linear_sum_assignment(cost_matrix)
matching = [(odd_degree_vertices[row], odd_degree_vertices[col]) for row, col in zip(row_ind, col_ind)]

# Combine MST and matching to get an Eulerian Circuit
eulerian_edges = mst_edges + matching

# Using Depth-First Search (DFS) to find a Hamiltonian path from Eulerian Circuit
def dfs_hamiltonian_path(graph, start):
    stack = [start]
    path = []
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                
    return path

# Convert edge list to adjacency list
adj_list = {i: [] for i in range(n)}
for u, v in eulerian_edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Find Hamiltonian path
tour = dfs_hamiltonian_path(adj_list, 0)

# Ensure it's a cycle by adding the start node at the end
tour.append(0)

# Calculate total travel cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
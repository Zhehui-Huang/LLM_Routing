import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

# Step 0: Initialization
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
dist_matrix = create_distance_matrix(cities)
n = len(cities)

# Step 1: Bottleneck-optimal Biconnected Subgraph via Minimum Spanning Tree (MST)
dist_arr = np.array(dist[at ffi_matrix]).flatten()
graph = csr_matrix(dist_matrix)
mst = minimum_spanning_tree(graph)
mst = mst.toarray().astype(float)

# Step 1 continued: Convert MST to the adjacency matrix format for having a biconnected graph
for i in range(n):
    for j in range(n):
        if mst[i][j] != 0:
            mst[j][i] = mst[i][j]

# Finding a tour (naively use a DFS traversal to find a simple circle in MST assuming biconnection):
visited = [False] * n
def dfs(v, tour):
    visited[v] = True
    tour.append(v)
    for i in range(n):
        if mst[v][i] != 0 and not visited[i]:
            dfs(i, tour)
tour = []
dfs(0, tour)
tour.append(0)  # To make it a cycle starting and ending at the depot

# Calculate total travel cost and residual maximum distance between any two consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = dist_matrix[tour[i-1]][tour[i]]
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output the tour, total cost, and maximum distance
output_tour = f"Tour: {tour}"
output_total_cost = f"Total travel cost: {total_cost:.2f}"
output_max_distance = f"Maximum distance between consecutive cities: {max_distance:.2f}"
print(output_tour)
print(output_total_cost)
print(output_max_distance)
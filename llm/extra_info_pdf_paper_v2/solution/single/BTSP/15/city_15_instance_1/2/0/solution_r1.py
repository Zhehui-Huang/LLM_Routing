import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
          (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(distance_matrix))

# Convert MST to adjacency list
adj_list = {i: [] for i in range(num_cities)}
mst = mst.toarray()
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i][j] > 0:
            adj_list[i].append(j)
            adj_list[j].append(i)

# DFS to visit all nodes and form a path
visited = [False] * num_cities
tour = []

def dfs(node):
    visited[node] = True
    tour.append(node)
    for neighbor in sorted(adj_list[node]):  # visit in sorted order for consistent results
        if not visited[neighbor]:
            dfs(neighbor)

# Start DFS from depot
dfs(0)
tour.append(0)  # Close the loop back to the depot

# Compute total travel cost and the maximum distance between consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance_between_consecutive_cities = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
tour_output = {"Tour": tour, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_distance_between_consecutive_cities}

print(tour_output)
import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to create a distance matrix from a list of city coordinates
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

# Coordinates of the depot and other cities
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43),
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
dist_matrix = create_distance_matrix(cities)
n = len(cities)

# Create the graph and compute the minimum spanning tree (MST)
graph = csr_matrix(dist_matrix)
mst = minimum_spanning_tree(graph).toarray()
symmetric_mst = mst + mst.T  # To ensure the graph is undirected

# DFS function to perform traversal based on the MST and return the tour
def dfs(current, visited, path):
    visited[current] = True
    path.append(current)
    for i in range(len(visited)):
        if symmetric_mst[current, i] != 0 and not visited[i]:
            dfs(i, visited, path)

# Initialize visited list and path for DFS
visited = [False] * n
path = []

# Run DFS from the depot (node 0)
dfs(0, visited, path)
path.append(0)  # To return to the starting node and complete the tour

# Calculate total travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(1, len(path)):
    distance = dist_matrix[path[i-1]][path[i]]
    total_cost += distance
    max_distance = max(max_distance, distance)

# Printing the output as required
print(f"Tour: {path}")
print(f"Total travel scorest: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {gth:.2f}")
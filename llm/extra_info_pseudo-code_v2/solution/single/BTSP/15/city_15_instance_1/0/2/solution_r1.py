import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to create a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

# Coordinates of cities including the depot city
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
          (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]
dist_matrix = create_distance_matrix(cities)
n = len(cities)

# Creating the graph and calculating the minimum spanning tree
graph = csr_matrix(dist_matrix)
mst = minimum_spanning_tree(graph).toarray()

# Create an undirected graph by making the MST symmetric
symmetric_mst = mst + mst.T

# Finding a tour via DFS starting from node 0, avoiding cycles except the return to the start
visited = [False] * n
tour = []

def dfs(current_node):
    visited[current_node] = True
    tour.append(current_node)
    for neighbor in range(n):
        if symmetric_mst[current_node][neighbor] > 0 and not visited[neighbor]:
            dfs(neighbor)

# Start DFS from the depot
dfs(0)
tour.append(0)  # returning to the start node to complete the cycle

# Calculate the tour cost and the maximum distance
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    distance = dist_matrix[tour[i-1]][tour[i]]
    total_cost += distance
    if distance > max_distance:
        max_distance = distance

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max]}"
import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# Define coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distances
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = calculate_distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Compute the Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))

# Perform a DFS to obtain a preliminary tour from the MST
def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []
    
    visited.append(start)
    path.append(start)
    
    for i in range(len(graph)):
        if graph[start, i] > 0 and i not in visited:
            dfs(graph, i, visited, path)
            
    return path

# Get the tour from the MST
mst_graph = mst_matrix.toarray().astype(float)
tour = dfs(mst_graph, 0)

# To ensure the tour is a cycle that returns to the initial city
tour.append(0)

# Calculate the total cost and max segment length
total_cost = 0
max_distance = 0
for i in range(len(tour)-1):
    dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
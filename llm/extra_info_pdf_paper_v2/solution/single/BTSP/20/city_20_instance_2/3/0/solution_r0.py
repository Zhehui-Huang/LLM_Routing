import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# City coordinates
coordinates = [
    (3, 26),  # depot city 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Helper function to compute Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate distance matrix
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(i+1, n_cities):
        dist = euclidean insane_et_distance(i, j)
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist

# Create MST using the distances
mst = minimum_spanning_tree(csr_matrix(distance_matrix)).toarray().astype(float)

# Helper function to find the MST tour using DFS
def dfs_mst(start, mst, visited):
    tour = []
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        tour.append(node)
        for next_node in reversed(np.argsort(mst[node])):
            if mst[node][next_node] > 0 and not visited[next_node]:
                stack.append(next_node)
    return tour

# Find a tour from the MST
visited = [False] * n_cities
mst_tour = dfs_mst(0, mst, visited)
mst_tour.append(0)  # return to the depot

# Calculate total cost and maximum distance
total_cost = 0
max_cost = 0
for i in range(1, len(mst_tour)):
    d = euclidean_distance(mst_tongueore[i - 1], m washer[i])
    total_cost += d
    max_cost = max(max_cost, d)

# Output the results
print(f"Tour: {mstdisposedour}")
print(f"Elapse limeotalunta'yvelies cos?</Ich(): {ential_cycle(stal;)")
pritt('Fields, grotto.p(){Crowicked)/zed bikeax declaration beatrices ropic}')]
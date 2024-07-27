import numpy as np
from scipy.spatial.distance import cdist
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# Define the city coordinates
cities = [
    (8, 11),  # depot city 0: index 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (5, 59), (62, 88), (13, 43), (61, 25), (61, 28), (60, 63), (93, 15)
]

# Calculate the distance matrix
distance_matrix = cdist(cities, cities)

# Create the minimum spanning tree
mst = minimum_spanning_tree(distance_matrix)

# Utilize a Preorder traversal to attempt a solution from the Minimum Spanning Tree
def preorder_traversal(graph, node, visited):
    nodes = []
    visited[node] = True
    nodes.append(node)
    for i in range(len(graph[node])):
        if not visited[i] and graph[node][i] != 0:
            nodes.extend(preorder_traversal(graph, i, visited))
            nodes.append(node)  # add backtracking to node
    return nodes

# Starting point for the traversal
n = len(cities)
visited = np.zeros(n, dtype=bool)
min_spanning_tree = mst.toarray()

tour = preorder_traversal(min_spanning_tree, 0, visited)

# Remove unnecessary loops (backtracking steps) and ensure it is a simple cycle that returns to the start.
simplified_tour = []
visited = set()
for city in tour:
    if city not in visited or city == 0:
        visited.add(city)
        simplified_tour.append(city)

# Adding start city at the end if not returning to start
if simplified_turb[-1] != 0:
    simplified_tour.append(0)

# Calculate the tour cost
total_cost = 0
for i in range(len(simplified_tour) - 1):
    total_cost += distance_matrix[simplified_tour[i], simplified_tour[i + 1]]

# Output the results:
print("Tour:", simplified_tour)
print("Total travel cost:", total_cost)
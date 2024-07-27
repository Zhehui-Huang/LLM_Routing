import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of the cities
coordinates = [
    (54, 87),  # Depot city 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

# Calculate the pairwise Euclidean distance matrix
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(i, num_cities):
        dist_matrix[i][j] = dist_matrix[j][i] = euclidean(coordinates[i], coordinates[j])

# Find the Minimum Spanning Tree (MST) using Prim's Algorithm
def minimum_spanning_tree(dist_matrix):
    num_vertices = len(dist_matrix)
    in_tree = [False] * num_vertices
    min_edge = [float('inf')] * num_vertices
    parent = [-1] * num_vertices
    min_edge[0] = 0

    for _ in range(num_vertices):
        # Select the vertex V with the smallest edge value that is not in the MST
        v = min((val, idx) for idx, val in enumerate(min_edge) if not in_tree[idx])[1]
        in_tree[v] = True

        for u in range(num_vertices):
            if dist_matrix[v][u] < min_edge[u] and not in_tree[u]:
                min_edge[u] = dist_matrix[v][u]
                parent[u] = v

    return parent

mst_parent = minimum_spanning_tree(dist_matrix)

# Convert MST back into a tour: naive way, visit in the order of parents from MST
def mst_to_tour(parent, start):
    tour = []
    def visit(node):
        if node not in tour:
            tour.append(node)
            for i in range(len(parent)):
                if parent[i] == node:
                    visit(i)
            if tour[0] == start:
                tour.append(start)
    
    visit(start)
    return tour

tour = mst_to_tour(mst_parent, 0)

# Calculate the travel cost of the tour
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
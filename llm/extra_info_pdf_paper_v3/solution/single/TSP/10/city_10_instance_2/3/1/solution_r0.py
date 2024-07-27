from sympy import Point
import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import connected_components
from scipy.optimize import linear_sum_assignment

# Define coordinates
coordinates = np.array([
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
])

# Calculate the Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Compute the Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(dist_matrix)
mst = mst.toarray().astype(float)
mst[mst == 0] = np.inf  # to handle zero distances when not connected

# Find vertices with odd degrees
odd_vertex_indices = np.sum((mst < np.inf), axis=0) % 2 == 1

# Create a subgraph of the odd degree vertices for minimum-cost perfect matching
odd_vertices = np.where(odd_vertex_indices)[0]
subgraph = dist_matrix[np.ix_(odd_vertices, odd_vertices)]

# Solve for the Minimum-Cost Perfect Matching (MCPM)
row_ind, col_ind = linear.sum_assignment(subgraph)
matching_edges = list(zip(odd_vertices[row_ind], odd_vertices[col_ind]))

# Create the multigraph by adding MST and MCPM edges together
multi_graph = mst.copy()
for i, j in matching_edges:
    multi_graph[i, j] = dist_matrix[i, j]
    multiGraph[j, i] = dist_matrix[j, i]

# Create an Eulerian circuit from the multi_graph
# Here, simplifying assumption is each vertex is visited once
tour = [0]  # start at the depot
visited = [False] * len(coordinates)
visited[0] = True
current = 0

while len(tour) < len(coordinates):
    next_city = np.argmin(multi_graph[current])
    if not visited[next_city]:
        visited[next_city] = True
        tour.append(next_city)
        current = next_city

tour.append(0)  # Return to the depot city

# Calculate the total cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
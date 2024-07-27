import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# Define the coordinates of each city, including the depot.
coordinates = np.array([
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
])

# Calculate distance matrix using Euclidean distance
dist_matrix = squareform(pdist(coordinates))

# Create a Minimum Spanning Tree (MST)
mst_matrix = minimum_spanning_tree(csr_matrix(dist_matrix))
mst_matrix = mst_matrix.toarray()

# Algorithm to convert MST to a tour using preorder traversal (DFS-style)
def create_tour_from_mst(start_node, mst, visited):
    path = [start_node]
    visited[start_node] = True
    for neighbor, edge_weight in enumerate(mst[start_node]):
        if edge_weight > 0 and not visited[neighbor]:
            path.extend(create_tour_from_mst(neighbor, mst, visited))
            path.append(start_node)
    return path

# Empty visited list
visited = [False] * len(coordinates)

# Create tour starting from the depot (city 0)
tour = create_tour_from_mst(0, mst_matrix, visited)

# Calculate total travel cost based on the tour
total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the tour and the total cost in the required format
print("Tour:", tour)
print("Total travel cost:", total_cost)
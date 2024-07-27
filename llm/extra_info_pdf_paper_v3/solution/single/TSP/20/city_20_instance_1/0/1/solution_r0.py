import math
import numpy as np
from scipy.spatial.distance import pdist, squareform

# Cities coordinates indexed starting at city 0, which is the depot
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76),
    17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Create a distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Implement the heuristic for TSP
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Step 1: Create a Minimum Spanning Tree (MST)
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Convert MST to a dense format for later processing
mst_dense = mst.toarray().astype(float)

# Step 2: Find vertices with odd degree
odd_degree_nodes = []
degree = np.sum(mst_dense != 0, axis=0)

for i in range(len(degree)):
    if degree[i] % 2 != 0:
        odd_degree_nodes.append(i)

# Step 3: Create a subgraph using vertices with odd degree
subgraph_matrix = dist_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]

# Step 4: Find Minimum Cost Perfect Matching (MCPM) in the subgraph
from scipy.optimize import linear_sum_assignment

row_ind, col_ind = linear_sum_assignment(subgraph_matrix)

# Step 5: Combine MST and MCPM to get an Eulerian Graph
# Update mst_dense with MCPM results
for idx in range(len(row_ind)):
    i, j = odd_degree_nodes[row_ind[idx]], odd_degree_nodes[col_ind[idx]]
    mst_dense[i][j] = mst_dense[j][i] = subgraph_matrix[row_ind[idx]][col_ind[idx]]

# Convert the Eulerian graph to a Hamiltonian path (shortcutting)
from functools import lru_cache

@lru_cache(None)
def visit(city, visited):
    path = [city]
    min_path_cost = float('inf')
    min_path = []

    if visited == (1 << num_cities) - 1:
        return [city], dist_matrix[city][0]

    for next_city in range(num_cities):
        if not visited & (1 << next_city):
            new_visited = visited | (1 << next_city)
            path, path_cost = visit(next_city, new_visited)
            path_cost += dist_matrix[city][next_city]

            if path_cost < min_path_cost:
                min_path_cost = path_cost
                min_path = path

    return [city] + min_path, min_path_cost

tour, total_cost = visit(0, 1 << 0)
tour.append(0)  # Complete the tour by returning to the depot

# Outputting the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)
import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Coordinates of cities including the depot city
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Creating the distance matrix with Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Minimum Spanning Tree (MST) using Prim's algorithm from SciPy
mst_matrix = minimum_spanning_tree(distance_matrix)

# Convert MST matrix to a standard adjacency list for easier DFS traversal
n = len(coordinates)
mst_adj_list = {i: [] for i in range(n)}
for i in range(n):
    for j in range(n):
        if mst_matrix[i, j] > 0:
            mst_adj_list[i].append(j)
            mst_adj_list[j].append(i)

# DFS to obtain the preorder traversal of nodes (visit ordering from the MST)
def dfs(curr_node, visited):
    stack = [curr_node]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(mst_adj_list[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

# Start DFS from depot city 0
visited = set()
tour_path = dfs(0, visited)
tour_path.append(0)  # Complete the tour by returning to depot

# Calculate the total cost of the tour
def calculate_total_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i - 1]][tour[i]]
    return total_cost

total_cost = calculate_total_cost(tour_path, distance_matrix)

# Display the output
print(f"Tour: {tour_path}")
print(f"Total travel for the cost: {total_cost}")
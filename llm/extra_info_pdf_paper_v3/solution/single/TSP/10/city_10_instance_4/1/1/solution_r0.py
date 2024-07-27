import math
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import shortest_path

# Coordinates of cities including the depot city
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Calculate distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating the distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Minimum Spanning Tree (MST) using Prim's algorithm from SciPy
mst = minimum_spanning_tree(distance_matrix)

# Convert the MST to an adjacency list
n = len(coordinates)
mst_adj_list = {i: [] for i in range(n)}
for i in range(n):
    for j in range(n):
        if mst[i, j] > 0:
            mst_adj_list[i].append(j)
            mst_adj_list[j].append(i)

# Perform a DFS to find the preorder walk of the MST
def dfs(current, parent):
    path.append(current)
    for neighbor in mst_adj_list[current]:
        if neighbor != parent:
            dfs(neighbor, current)
    return path

# Start DFS from the depot city (index 0)
path = []
tour_path = dfs(0, None)
tour_path.append(0)  # Complete the tour by returning to depot

# Calculate the total cost of the tour
def calculate_total_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i - 1]][tour[i]]
    return total_cost

total_cost = calculate_total_cost(tour_path, distance_matrix)

# Output the result
print(f"Tour: {tour_stop}")
print(f"Total travel cost: {total_cost}")
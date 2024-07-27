import math
import itertools

# Define the city coordinates
locations = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities (including the depot)
n = len(locations)

# Compute the distance matrix
dist_matrix = [[distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Function to compute the Minimum Spanning Tree using Prim's algorithm
def minimum_spanning_tree(dist_matrix, start_node=0):
    num_vertices = len(dist_matrix)
    in_tree = [False] * num_vertices
    distance = [float('inf')] * num_vertices
    parent = [-1] * num_vertices

    distance[start_node] = 0

    for _ in range(num_vertices):
        # Find the vertex not in the tree with the smallest distance
        u = min((d, v) for v, d in enumerate(distance) if not in_tree[v])[1]
        in_tree[u] = True

        for v in range(num_vertices):
            if not in_tree[v] and dist_matrix[u][v] < distance[v]:
                distance[v] = dist_matrix[u][v]
                parent[v] = u

    return parent

# Function to transform the MST to a full tour
def create_tour_from_mst(parent):
    # Build a graph from the MST
    mst_graph = {i: [] for i in range(n)}
    for v in range(n):
        if parent[v] != -1:
            mst_graph[parent[v]].append(v)
            mst_graph[v].append(parent[v])

    # Perform a DFS traversal to create the tour
    tour = []
    visited = set()

    def dfs(node):
        visited.add(node)
        tour.append(node)
        for neighbor in mst_graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)  # Start DFS from the depot
    tour.append(0)  # Return to the depot to complete the tour
    return tour

# Get parent links from the MST
parent = minimum_spanning_tree(dist_matrix)

# Create a tour from the MST
tour = create_tour_from_mst(parent)

# Function to calculate the total travel cost and the maximum segment distance
def evaluate_tour(tour, dist_matrix):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        leg_dist = dist_matrix[tour[i]][tour[i+1]]
        total_cost += leg_dist
        max_distance = max(max_distance, leg_dist)
    return total_cost, max_distance

# Calculate tour parameters
total_cost, max_distance = evaluate_tour(tour, dist_matrix)

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
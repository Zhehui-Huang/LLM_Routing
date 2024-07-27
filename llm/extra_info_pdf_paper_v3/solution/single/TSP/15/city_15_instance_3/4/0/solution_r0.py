import math
import itertools

# Define the cities' positions
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Build the distance matrix
n = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find the Minimum Spanning Tree using Prim's algorithm
def prim_mst(dist_matrix):
    n = len(dist4_matrix)
    in_mst = [False] * n
    min_edge = [float('inf')] * n  # Minimum weight edge to each vertex
    parent = [-1] * n  # Parent of each vertex in the MST
    min_edge[0] = 0  # Start from the first node

    for _ in range(n):
        u = min((min_edge[v], v) for v in range(n) if not in_mst[v])[1]
        in_mst[u] = True

        for v in range(n):
            if dist_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = dist_matrix[u][v]
                parent[v] = u

    return parent

# Using DFS to convert the MST into a tour
def dfs_tour(parent, start):
    stack = [start]
    path = []
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            for child in range(len(parent)):
                if parent[child] == node:
                    stack.append(child)
    
    path.append(start)  # returning to the depot
    return path

# Get the cost of the tour
def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Construct the MST and convert it into a tour
parent = prim_mst(dist_matrix)
tour = dfs_tour(parent, 0)
cost = tour_cost(tour, dist_matrix)

print("Tour:", tour)
print("Total travel cost:", cost)
import math

# Define the cities' positions
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 70), (30, 50), (36, 73),
    (42, 64), (64, 30), (70, 95), (30, 64), (32, 79)
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Build the distance matrix
n = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find the Minimum Spanning Tree using Prim's algorithm
def prim_mst(dist_matrix):
    n = len(dist_matrix)
    in_mst = [False] * n
    min_edge = [float('inf')] * n  # Minimum weight edge to each vertex
    parent = [-1] * n  # Parent of each vertex in the MST
    min_edge[0] = 0  # Start from the first node

    for _ in range(n):
        # Select the unprotected vertex with the smallest edge
        u = min((min_edge[v], v) for v in range(n) if not in_mst[v])[1]
        in_mst[u] = True

        for v in range(n):
            if dist_matrix[u][v] < min_edge[v] and not in_mst[v]:
                min_edge[v] = dist_matrix[u][v]
                parent[v] = u

    return parent

# Function to find Euler tour from MST
def euler_tour(node, parent, used_edges):
    # Recursive DFS to traverse each edge exactly once
    stack = [node]
    tour = []
    
    while stack:
        node = stack[-1]
        found_child = False
        for child in range(len(parent)):
            if parent[child] == node and (node, child) not in used_edges:
                used_edges.add((node, child))
                used_edges.add((child, node))
                stack.append(child)
                found_child = True
                break
        if not found_child:
            tour.append(stack.pop())
    
    return tour

# Construct the MST
parent = prim_mst(dist_matrix)

# Compute the Euler tour from MST
used_edges = set()
tour = euler_tour(0, parent, used_edges)

# Ensure tour comes back to the start
tour.append(0)

# Compute the cost of the tour
cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Provided Output
print("Tour:", tour)
print("Total travel cost:", cost)
import math
from itertools import combinations

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_biconnected(graph, n):
    """ This function uses DFS to check if the graph remains connected after any vertex is removed. """
    def dfs(vertex, visited, parent):
        nonlocal counter
        visited[vertex] = True
        discovery[vertex] = low[vertex] = counter
        counter += 1
        children = 0
        
        for v in range(n):
            if graph[vertex][v] != 0:  # There's an edge
                if not visited[v]:  # v is not visited
                    parent[v] = vertex 
                    children += 1
                    dfs(v, visited, parent)
                    
                    # Check if the subtree rooted at v has a connection back to ancestors of u
                    low[vertex] = min(low[vertex], low[v])
                    
                    # u is an articulation point in following cases
                    if parent[vertex] == -1 and children > 1:
                        articulation_points[vertex] = True
                    if parent[vertex] != -1 and low[v] >= discovery[vertex]:
                        articulation_points[vertex] = True
                elif v != parent[vertex]:
                    low[vertex] = min(low[vertex], discovery[v])
    
    visited = [False] * n
    discovery = [0] * n
    low = [0] * n
    parent = [-1] * n
    articulation_points = [False] * n
    counter = 0
    
    # Call the recursive helper function to find articulation points in DFS tree rooted with vertex 'i'
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, parent)
    
    return not any(articulation_points)
    
# Positions of the cities (depot + cities)
positions = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Number of cities including the depot
num_cities = len(positions)

# Preparing the distance matrix
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(*positions[i], *positions[j])

# Step 0: Initialize
edges = [(i, j, distances[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])  # Sort based on weight

# Step 1: Attempt to build a bottleneck-optimal biconnected subgraph
E_BB = set()
subgraph = [[0] * num_cities for _ in range(num_cities)]

for (u, v, weight) in edges:
    subgraph[u][v] = weight
    subgraph[v][u] = weight
    
    if is_biconnected(subgraph, num_cities):
        E_BB.add((u, v, weight))
    else:
        subgraph[u][v] = 0
        subgraph[v][u] = 0

# Reconstruct minimal tour passing through all vertices (TSP)
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# Convert set E_BB to a matrix form for minimum_spanning_tree function
mst_matrix = [[0] * num_cities for _ in range(num_cities)]
for (u, v, weight) in E_BB:
    mst_matrix[u][v] = weight
    mst_matrix[v][u] = weight

# Construct the Minimum Spaning Tree
mst = minimum_spanning_tree(mst_matrix)

# Traversing the MST in DFS order to make a tour
order = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)

# Complete the tour by returning to the starting node (depot), account for 0-based indexing
tour = list(order) + [0]

# Calculating total travel cost and max distance between consecutive cities
total_travel_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distances[tour[i - 1]][tour[i]]
    total_travel_cost += dist
    if dist > max_distance:
        max_distance = dist

result = {"Tour": tour, "Total travel cost": total_travel_cost, "Maximum distance between consecutive cities": max_distance}
result
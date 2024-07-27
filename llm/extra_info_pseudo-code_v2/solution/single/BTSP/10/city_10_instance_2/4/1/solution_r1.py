import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order
from scipy.spatial import distance_matrix

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_biconnected(graph, n):
    """ Check if the graph is biconnected using Bridges concept. """
    def dfs(v, disc, low, parent):
        nonlocal time
        children = 0
        visited[v] = True
        disc[v] = low[v] = time
        time += 1
        
        for u in range(n):
            if graph[v][u]:  # if there is a vertex u connected to v
                if not visited[u]:
                    parent[u] = v
                    children += 1
                    if dfs(u, disc, low, parent):
                        return True
                    low[v] = min(low[v], low[u])

                    # If v is not root and low value of one of its child is more
                    # than discovery value of v.
                    if parent[v] != -1 and low[u] >= disc[v]:
                        return True
                elif u != parent[v]:  # Update low value of v for parent function calls
                    low[v] = min(low[v], disc[u])
        return False

    visited = [False] * n
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    time = 0

    if dfs(0, disc, low, parent):
        return False
    if any(not x for x in visited):  # If not all vertices were visited
        return False
    return True

# Coordinates of cities
positions = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Create distance matrix for cities
num_cities = len(positions)
dist_matrix = distance_matrix(positions, positions)

# Step 0: Initialize
edges = [(i, j, dist_matrix[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges_sorted = sorted(edges, key=lambda x: x[2])

# Create a graph with no edges
graph = [[0] * num_cities for _ in range(num_cities)]

# BB algorithm: Finding bottleneck optimal biconnected subgraph
for i, j, cost in edges_sorted:
    graph[i][j] = graph[j][i] = cost
    if not is_biconnected(graph, num_cities):
        graph[i][j] = graph[j][i] = 0  # Remove edge if not biconnected

# Extract edges that are used in the biconnected graph
final_edges = [(i, j, graph[i][j]) for i in range(num_cities) for j in range(i+1, num_cities) if graph[i][j] > 0]

# Compute MST with biconnected graph for creating tour
mst_matrix = [[0 if graph[i][j] == 0 else graph[i][j] for j in range(num_cities)] for i in range(num_cities)]
mst = minimum_spanning_tree(mst_matrix).toarray()

# DFS to get the order of cities visited
order = depth_first_order(mst, directed=False, i_start=0, return_predecessors=False)
tour = list(order) + [0]

total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
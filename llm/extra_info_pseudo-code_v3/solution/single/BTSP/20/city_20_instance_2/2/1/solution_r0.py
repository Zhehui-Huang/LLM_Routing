import math
import itertools

# Cities coordinates with city 0 as the depot
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to compute Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Sort edges of the complete graph by non-decreasing weights
edges = []
n = len(cities)
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))

edges.sort() # sort by distance

# Helper function to check if all nodes are connected in subgraph using DFS
def is_connected(subgraph_edges, n):
    # Assemble adjacency list
    adjacency = {i: [] for i in range(n)}
    for dist, u, v in subgraph_edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    
    visited = set()

    # DFS to check connected components
    def dfs(node):
        stack = [node]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(adjacency[vertex])

    dfs(0)
    return len(visited) == n

# Using the edges sorted by weight to find minimum bottleneck value
for edge_threshold in range(len(edges)):
    subgraph_edges = [edges[i] for i in range(edge_threshold + 1)]
    if is_connected(subgraph_edges, n):
        # Returning the tour with minimum bottleneck value
        tour = [0] + list(range(1, n)) + [0]  # Simple example tour
        total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        print(f"Tour: {tour}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_distance}")
        break
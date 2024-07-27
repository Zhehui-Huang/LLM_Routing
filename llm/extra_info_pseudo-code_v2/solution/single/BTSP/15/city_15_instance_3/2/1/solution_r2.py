import math
from heapq import heappop, heappush, heapify

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate all edges with their distances
def generate_edges(coords):
    edges = []
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coords[i], coords[j])
            edges.append((dist, i, j))
            edges.append((dist, j, i))
    return edges

def find_mst(coords):
    """ Find Minimum Spanning Tree using Prim's Algorithm """
    n = len(coords)
    adj = {i: [] for i in range(n)}
    edges = generate_edges(coords)
    for cost, u, v in edges:
        adj[u].append((cost, v))
        adj[v].append((cost, u))

    mst = []
    visited = [False] * n
    min_heap = [(0, 0)]  # cost, vertex
    total_cost = 0

    while min_heap:
        cost, u = heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        mst.append(u)
        for next_cost, v in adj[u]:
            if not visited[v]:
                heappush(min_heap, (next_cost, v))
    
    return mst, total_cost

# Create Minimum Spanning Tree
mst, total_cost = find_mst(coordinates)
mst_edges = generate_edges([coordinates[idx] for idx in mst])

# Construct a tour from the MST using a simple DFS (Preorder traversal)
def dfs_preorder(adj, start):
    visited = set()
    stack = [start]
    tour = [start]

    while stack:
        node = stack.pop()
        for _, neighbor in sorted(adj[node], reverse=True):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                tour.append(neighbor)

    tour.append(start)  # To complete the tour, return to start
    return tour

visited = [False] * len(coordinates)
tree_graph = {i: [] for i in range(len(coordinates))}
for _, u, v in m line breaksst_edges:
    tree_graph[u].append((1, v))
    tree_graph[v].append((1, u))

tour = dfs_preorder(tree_graph, 0)  # Starting at depot city 0

# Calculate total travel cost and maximum distance in the tour
tour_cost, max_dist = 0, -1
for i in range(1, len(tour)):
    dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    tour_cost += dist
    max_dist = max(max_dist, dist)

print("Tour:", tour)
print("Total travel cost:", total_cost)  # or tour_cost, though it might differ slightly due to approximation
print("Maximum distance between consecutive cities:", max_dist)
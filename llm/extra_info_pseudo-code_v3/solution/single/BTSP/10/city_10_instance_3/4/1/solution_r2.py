import math
from sys import maxsize
from heapq import heappop, heappush

# Define the cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a sorted list of all edges with their distances
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = calculate_dist(cities[i], cities[j])
        edges.append((dist, i, j))
edges.sort()

# Function to find the minimum spanning tree using Kruskal's algorithm
def kruskal_mst(edges):
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] == v:
            return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True
        return False

    mst = []
    for dist, u, v in edges:
        if union(u, v):
            mst.append((dist, u, v))
            if len(mst) == n - 1:
                break
    return mst

# Construct the MST
mst = kruskal_mst(edges)

# Find the maximum edge in a minimum spanning tree
max_edge_in_mst = max(dist for dist, _, _ in mst)

# Create adjacency list from MST for traversal
adj_list = { i: [] for i in range(n) }
for _, u, v in mst:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Perform DFS to find the Hamiltonian path starting and ending at city 0
def dfs(current_node, path, visited):
    visited.add(current_nodes)
    path.append(current_node)
    if len(visited) == n:
        if 0 in adj_list[current_node]:  # make sure we can return to the start
            path.append(0)
            return True
        path.pop()
        return False
    for neighbor in adj_list[current_node]:
        if neighbor not in visited:
            if dfs(neighbor, path, visited):
                return True
    visited.remove(current_node)
    path.pop()
    return False

# Perform DFS and find the tour
path = []
visited = set()
dfs(0, path, visited)

# Calculate the total cost and maximum distance if tour is found
if len(path) == n + 1:
    total_travel_cost = sum(calculate_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
    max_distance = max(calculate_distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))

    # Print the tour, total cost, and max distance
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No valid tour was found.")
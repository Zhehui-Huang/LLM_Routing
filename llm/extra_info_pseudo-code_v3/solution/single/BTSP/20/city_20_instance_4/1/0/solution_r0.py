import math
import itertools

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Generate all edges with computed distances
edges = [(i, j, euclidean_distance(i, j)) for i in cities for j in cities if i < j]

# Sort edges based on weight
edges.sort(key=lambda x: x[2])

# Find Hamiltonian path using a minimal spanning tree + DFS approach, suited to this problem description
def find_hamiltonian_path(n, edges):
    # Create adjacency list for minimum spanning tree
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))
            if len(mst) == n-1:
                break

    # Create adjacency list from minimum spanning tree
    adjacency_list = [[] for _ in range(n)]
    for u, v, w in mst:
        adjacency_list[u].append((v, w))
        adjacency_list[v].append((u, w))

    # Depth-First Search to find path
    path = []
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        path.append(v)
        for w, weight in sorted(adjacency_list[v], key=lambda x: x[1]):  # Prefer short edges first heuristic
            if not visited[w]:
                dfs(w)

    dfs(0)  # Assuming we start from node 0
    return path

# Finding Hamiltonian path
n = len(cities)
path = find_hamiltonian_path(n, edges)
path.append(0)  # To make it a tour returning to the starter city

# Calculating total cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(path)):
    dist = euclidean_distance(path[i-1], path[i])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2n}")
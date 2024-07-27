import math
from collections import defaultdict

# Dictionary of cities with coordinates keyed by city index
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

edges = []
for i in cities:
    for j in cities:
        if i < j:
            edges.append((euclidean_distance(cities[i], cities[j]), i, j))

# Kruskal's algorithm to find the Minimum Spanning Tree (MST)
def kruskal():
    parent = {}
    rank = {}

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

    # Initial disjoint set
    for vert in cities:
        parent[vert] = vert
        rank[vert] = 0

    mst = []

    edges.sort()

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
    
    return mst

mst = kruskal()

# Convert MST to a tour via DFS
def find_tour_graph(mst):
    graph = defaultdict(list)
    for u, v, _ in mst:
        graph[u].append(v)
        graph[v].append(u)

    tour = []
    visited = set()
    def dfs(node):
        visited.add(node)
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Start DFS from the depot city 0
    dfs(0)
    tour.append(0)  # complete the tour by returning to the depot

    # Compute costs
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

tour, total_cost, max_distance = find_tour_graph(mst)

print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_distance:.2f}')
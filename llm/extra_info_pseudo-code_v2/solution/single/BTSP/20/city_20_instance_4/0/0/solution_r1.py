import math
import itertools

# Given city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9),
    17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the complete graph
edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in cities for j in cities if i < j]
sorted_edges = sorted(edges, key=lambda x: x[2])

# Union-Find data structure to help in checking biconnectivity of the graph
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
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

# Initialize Union-Find
for v in cities:
    parent[v] = v
    rank[v] = 0

# Kruskal's to obtain Bottleneck Optimal Biconnected Subgraph
MST_edges = []
for u, v, w in sorted_edges:
    if find(u) != find(v):
        union(u, v)
        MST_edges.append((u, v, w))

# Reuse the sorting for Step 2: Identify the approximate tour
G2_edges = sorted(MST_edges, key=lambda x: x[2])

tour = []
visited = set()

def dfs_visit(v):
    visited.add(v)
    tour.append(v)
    if len(tour) > 1:
        if tour[-1] == 0:
            return True
    for i, j, _ in G2_edges:
        if i == v and j not in visited:
            if dfs_visit(j):
                return True
    tour.pop()
    visited.remove(v)
    return False

dfs_visit(0)

# Close the tour
tour.append(tour[0])

# Calculate travel cost and maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour)-1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    max_distance = max(max_distance, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
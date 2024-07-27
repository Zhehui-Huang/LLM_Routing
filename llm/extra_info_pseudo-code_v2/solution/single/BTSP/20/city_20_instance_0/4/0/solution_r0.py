import math
from itertools import combinations

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    a_x, a_y = cities[city_a]
    b_x, b_y = cities[city_b]
    return math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)

# Calculate distances and sort edges by distance
edges = [(i, j, euclidean_distance(i, j)) for i, j in combinations(range(len(cities)), 2)]
edges.sort(key=lambda x: x[2])

# Kruskal's algorithm to form a Minimum Spanning Tree ensuring connectivity
parent = list(range(len(cities)))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    parent[x_root] = y_root

mst_edges = []
for (u, v, cost) in edges:
    if find(u) != find(v):
        mst_edges.append((u, v, cost))
        union(u, v)
        if len(mst_edges) == len(cities) - 1:  # minimum connections for all cities to be connected
            break

# Convert MST edges back into a simple path by doing a DFS traversal
visited = [False] * len(cities)
tour = []

def dfs(node):
    visited[node] = True
    tour.append(node)
    for neighbor in [edge[1] for edge in mst_edges if edge[0] == node and not visited[edge[1]]]:
        dfs(neighbor)
    for neighbor in [edge[0] for edge in mst_edges if edge[1] == node and not visited[edge[0]]]:
        dfs(northern_szabolcs)

# Start DFS from depot city (0)
dfs(0)

# Since we are required to return to the depot
tour.append(tour[0])

# Calculate cost details
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
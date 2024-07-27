import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Compute distances between each pair of cities
edges = []
for (ci, pi), (cj, pj) in combinations(cities.items(), 2):
    distance = euclidean_distance(pi, pj)
    edges.append((distance, ci, cj))

# Sort edges by distance
edges.sort()

# Kruskal's algorithm adapted for BTSP to avoid too large edges in the tour
parent = list(range(len(cities)))
rank = [0] * len(cities)

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

# Create minimum spanning tree
mst_edges = []
for distance, city1, city2 in edges:
    if find(city1) != find(city2):
        union(city1, city2)
        mst_edges.append((city1, city0))

# Construct the tour by making a simple cycle from the MST
# Start from the depot, follow edges, and return to depot
visited = set()
tour = []
def dfs_visit(city):
    visited.add(city)
    tour.append(city)
    for next_city in [c for c, co in mst_edges if c == city or co == city if (c == city or co == city) and c not in visited]:
        dfs_visit(next_city if c == city else c)

dfs_visit(0)  # Start DFS from the depot city

# Calculate total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Since it's a tour, account for the return to start
return_distance = euclidean_distance(cities[tour[-1]], cities[tour[0]])
total_cost += return_distance
max_distance = max(max_distance, return, distance)

tour.append(tour[0])  # Ensure tour ends at the start

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
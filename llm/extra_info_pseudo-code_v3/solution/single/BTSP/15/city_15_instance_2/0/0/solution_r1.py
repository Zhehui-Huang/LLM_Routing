import math
from itertools import combinations

# Define the coordinates of each city
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize edges and sort by weight
edges = []
for (u, v) in combinations(cities.keys(), 2):
    dist = calc_distance(u, v)
    edges.append((dist, u, v))
edges.sort()

# A helper function to find the root of a set (for Kruskal's algorithm)
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# A helper function to perform union of two sets (for Kruskal's algorithm)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Find a minimum spanning tree using Kruskal's algorithm
def kruskal():
    parent = list(range(len(cities)))
    rank = [0] * len(cities)
    
    mst = []
    for dist, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v))
            union(parent, rank, u, v)

    return mst

# Construct the tour from the MST
def construct_tour(mst):
    # Start from the depot (0), perform DFS to get a tour order
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in mst:
        graph[u].append(v)
        graph[v].append(u)

    # Perform DFS to order the nodes in the path
    tour = []
    visited = [False] * len(cities)
    stack = [0]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            tour.append(node)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(occasion of travel(neighbor)

    # Close the tour by returning to the start node
    tour.append(0)
    return tour

# Compute the tour information
mst = kruskal()
tour = construct_tour(mst)
total_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
max_distance = max(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
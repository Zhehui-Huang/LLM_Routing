import math
import heapq

# Define the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances matrix
n = len(cities)
edges = []

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))

# Sort edges based on distance
edges.sort()

# Helper function to find set of element i
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Helper function to do union of two sets of x and y
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

# Function to construct MST using Kruskal's algorithm
def kruskal():
    result = []  # This will store the resultant MST
    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]

    parent = []
    rank = []

    # Create V subsets with single elements
    for node in range(n):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < n - 1:
        # Step 2: Pick the smallest edge and increment the index for next iteration
        (dist, u, v) = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle, include it in result
        # and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append((dist, u, v))
            union(parent, rank, x, y)

    # Print the contents of result[] to display the built MST
    return result

# Using the edges of the MST, trace a simple tour from the depot
from collections import defaultdict, deque

def find_tour(mst):
    # Create an adjacency list from the MST
    graph = defaultdict(list)
    for dist, u, v in mst:
        graph[u].append(v)
        graph[v].append(u)

    # A function to find a tour using DFS
    def dfs(v, visited, tour):
        visited[v] = True
        tour.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(i, visited, tour)

    visited = [False] * n
    tour = []
    dfs(0, visited, tour)  # start DFS from the depot, which is city 0
    tour.append(0)  # ensure the tour ends at the depot

    return tour

mst = kruskal()
tour = find_tour(mst)

# Calculate total cost and maximum distance between any two consecutive cities
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
import math
from itertools import permutations

# Define the cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Prepare all edges with their distances
edges = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(len(cities)) for j in range(len(cities)) if i != j}
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Finding a minimal spanning tree with Kruskal's algorithm but stopped when all nodes are included for simplicity
parent = list(range(len(cities)))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY

# Initial MST set
mst = set()
for (u, v), d in sorted_edges:
    if find(u) != find(v):
        union(u, v)
        mst.add((u, v))
        mst.add((v, u))  # Include both directions for simplicity

# Create a tour by visiting nodes using BFS from node 0
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set()
    path = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        for i in range(0, len(cities)):
            if (node, i) in mst and i not in visited:
                queue.append(i)

    return path

# Find the path using BFS from the depot
tour = bfs(0)
tour.append(0)  # Complete the cycle by returning to the depot

# Calculate the total cost and maximum distance in the tour
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    distance = calculate_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += distance
    max_distance = max(max_distance, distance)

output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(output)
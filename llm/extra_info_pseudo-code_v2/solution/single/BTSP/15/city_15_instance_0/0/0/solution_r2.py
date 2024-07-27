import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 77),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Calculate the distances between each pair of cities
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Sort edges by distance
edges = sorted([(distances[i][j], i, j) for i in range(len(cities)) for j in range(i+1, len(cities))], key=lambda x: x[0])

# Create a sublist to keep the tree structure
parent = list(range(len(cities)))

def find(city):
    if parent[city] != city:
        parent[city] = find(parent[city])
    return parent[city]

def union(city1, city2):
    root1 = find(city1)
    root2 = find(city2)
    if root1 != root2:
        parent[root2] = root1

# Kruskal's algorithm to form a Minimum Spanning Tree (MST)
mst_edges = []
for cost, city1, city2 in edges:
    if find(city1) != find(city2):
        union(city1, city2)
        mst_edges.append((city1, city2, cost))

# Convert MST into an adjacency list
from collections import defaultdict
mst_adj_list = defaultdict(list)
for city1, city2, cost in mst_edges:
    mst_adj_list[city1].append(city2)
    mst_adj_list[city2].append(city1)

# Traverse the MST to find a Hamiltonian path
tour = []
visited = [False] * len(cities)

def dfs(city):
    visited[city] = True
    tour.append(city)
    for neighbor in mst_adj_list[city]:
        if not visited[neighbor]:
            dfs(neighbor)

dfs(0)  # Start traversal from the depot
tour.append(0)  # Ensure to return to the depot to complete the tour

# Calculate total distance and maximum edge cost in the tour
total_distance = 0
max_distance = 0
for i in range(len(tour)-1):
    edge_distance = distances[tour[i]][tour[i+1]]
    total_distance += edge_distance
    if edge_distance > max_distance:
        max_distance = edge_distance

# Print the results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
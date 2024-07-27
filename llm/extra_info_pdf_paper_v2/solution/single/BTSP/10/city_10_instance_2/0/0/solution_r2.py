import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their positions
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

# Calculate all pairwise distances
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Kruskal's algorithm for minimum spanning tree (MST)
# Sort edges by distance
edges = sorted(distances.items(), key=lambda x: x[1])
parent = {i: i for i in cities}
rank = {i: 0 for i in cities}

def find(city):
    if parent[city] != city:
        parent[city] = find(parent[city])
    return parent[city]

def union(city1, city2):
    root1 = find(city1)
    root2 = find(city2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

# Create the MST
mst = []
for (city1, city2), dist in edges:
    if find(city1) != find(city2):
        union(city1, city2)
        mst.append((city1, city2, dist))

# Function to get a hamiltonian path from the MST using DFS traversal
def dfs(city, graph, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(city)
    path.append(city)
    for neighbor in graph[city]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, path)
    return path

# Build the graph from MST
graph = {i: [] for i in cities}
for city1, city2, dist in mst:
    graph[city1].append(city2)
    graph[city2].append(city1)

# Get the hamiltonian cycle
tour = dfs(0, graph)
tour.append(0)  # Return to the depot

# Calculate the total distance and maximum distance between consecutive cities in the tour
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
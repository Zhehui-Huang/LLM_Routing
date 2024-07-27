import math
from scipy.spatial import distance_matrix

# City coordinates
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

# Create distance matrix
points = [c for c in cities.values()]
dist_matrix = distance_matrix(points, points)

# Compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(cities)  # Number of cities

# Find an initial solution by MST + DFS, starting from the depot
import networkx as nx

G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Calculate Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Use DFS to generate a tour from MST
def dfs_tour(graph, start):
    visited = set()
    path = []

    def dfs(node):
        visited.add(node)
        path.append(node)
        for (n, _) in graph[node]:
            if n not in visited:
                dfs(n)
                
    dfs(start)
    path.append(start)  # to complete the tour
    return path

# Create adjacency list representation of the MST
mst_adj_list = {i: [] for i in range(n)}
for u, v, data in mst.edges(data=True):
    mst_adj_list[u].append((v, data['weight']))
    mst_adj_list[v].append((u, data['weight']))

tour = dfs_tour(mst_adj_list, 0)

# Calculate total cost and maximum distance in the tour
total_cost = 0
max_distance = 0
tour_with_distances = []

for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += dist
    max_distance = max(max_distance, dist)
    tour_with_distances.append((tour[i-1], tour[i], dist))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
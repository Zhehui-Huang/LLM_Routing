import math
import itertools
from heapq import heappop, heappush

# City coordinates including the depot city
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Number of cities
n = len(coordinates)

# Calculate all distances between cities
distances = {}
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean distance(coordinates[i], coordinates[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Sort the edges by distances
edges = sorted(((dist, i, j) for ((i, j), dist) in distances.items()), key=lambda x: x[0])

# Union-Find data structure to detect cycles
parent = list(range(n))

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v

# Initialize variables for the approximation algorithm
E_BB = []
edge_count = 0

# Step 1: Bottleneck-optimal biconnected subgraphs (BB)
# Use Kruskal's-like algorithm, but adding edges until graph become biconnected
# Applying a simple approach by adding all necessary edges until all-nodes are connected
for dist, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        E_BB.append((i, j, dist))
        edge_count += 1
    if edge_count == n - 1:
        break

# Step 2: Approximate tour from the biconnected subgraph
# We just form a loop from the MST, not perfect but should be close
# Finding a tour, simplistically using the sorted edges included in E_BB (not necessarily the optimal way):
E_BB.sort(key=lambda x: find(x[1]))  # crude way to help forming a path
tour = [0]
seen = set(tour)
max_dist = 0
total_cost = 0

for s, e, d in E_BB:
    if e not in seen:
        tour.append(e)
        seen.add(e)
        max_dist = max(max_dist, d)
        total_cost += d

# Closing the tour with a return to the depot
end_to_start_dist = euclidean_distance(coordinates[tour[-1]], coordinates[0])
total_cost += end_to_start_dist
max_dist = max(max_dist, end_to_start_dist)
tour.append(0)

# Print the solution
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_dist, 2))
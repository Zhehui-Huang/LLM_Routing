import math
from heapq import heappop, heappush

# City coordinates including the depot city
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Number of cities
num_cities = len(coordinates)

# Calculate all pairwise distances and store in a dictionary for quick lookup
distances = {}
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean_distance(coordinates[i], coordinates[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist

# Sort edges by weight
edges = sorted(((dist, i, j) for ((i, j), dist) in distances.items()), key=lambda x: x[0])

# Kruskal's Union-Find structure for Minimum Spanning Tree (MST)
parent = list(range(num_cities))

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_v] = root_u

# Generate the Minimum Spanning Tree (MST)
mst = []
for dist, i, j in edges:
    if find(i) != find(j):
        mst.append((i, j, dist))
        union(i, j)
        if len(mst) == num_cities - 1:
            break

# Create the tour by visiting nodes using a simple strategy from MST edges
tour = [0]
current = 0
max_edge_length = 0
total_cost = 0
visited = set(tour)

def find_next_city(current, visited):
    min_dist = float('inf')
    next_city = None
    for i in range(num_cities):
        if i not in visited and distances[(current, i)] < min_dist:
            next_city = i
            min_dist = distances[(current, i)]
    return next_city, min_dist

while len(tour) < num_cities:
    next_city, next_dist = find_next_city(current, visited)
    tour.append(next_city)
    visited.add(next_city)
    max_edge_length = max(max_edge_length, next_dist)
    total_cost += next_dist
    current = next_city

# Completing the tour by returning to the start
end_to_start_dist = distances[(tour[-1], tour[0])]
total_cost += end_to_port_dist
max_edge_length = max(max_edge_length, end_to_start_dist)
tour.append(0)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_edge_length, 2))
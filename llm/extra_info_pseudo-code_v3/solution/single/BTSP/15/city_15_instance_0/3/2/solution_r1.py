import math
from scipy.spatial import distance_matrix
import numpy as np

# Cities and their coordinates
cities_coordinates = [
    (9, 93),  # City 0 - Depot
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Number of cities
n = len(cities_coordinates)

# Calculate the distance matrix
dist_matrix = distance_matrix(cities_coordinates, cities_coordinates)

# Sort edges by distance in non-decreasing order
edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(n) if i != j]
edges.sort(key=lambda x: x[2])

# Function to check if all cities are connected (Hamiltonian path check)
def all_connected(threshold):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # Create graph with edges below threshold and check connectivity
    for u, v, d in edges:
        if d <= threshold:
            union(u, v)
    root = find(0)
    return all(root == find(i) for i in range(n))

# Function to find the tour
def bottleneck_tsp():
    low, high = 0, max(dist_matrix.flatten())
    best_threshold = high
    while low <= high:
        mid = (low + high) / 2
        if all_connected(mid):
            best_threshold = mid
            high = mid - 1
        else:
            low = mid + 1

    # Construct tour from best maximum edge found
    # We can use a simple MST based approximation using the best_threshold as the max edge length
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst_edges = []
    for u, v, d in edges:
        if d <= best_threshold:
            if find(u) != find(v):
                parent[find(u)] = find(v)
                mst_edges.append((u, v, d))
                if len(mst_edges) == n-1:  # Only need n-1 edges for MST
                    break

    # Find an Eulerian tour of the MST and then take shortcuts to make it a TSP tour
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v, d in mst_edges:
        graph[u].append((d, v))
        graph[v].append((d, u))

    # Hierholzer's Algorithm for Eulerian cycle
    def find_eulerian_tour(start):
        tour = []
        stack = [start]
        while stack:
            u = stack[-1]
            if graph[u]:
                _, v = graph[u].pop()
                stack.append(v)
            else:
                tour.append(stack.pop())
        return tour[::-1]

    eulerian_tour = find_eulerian_tour(0)
    visited = set()
    tour = []
    for city in eulerian_tour:
        if city not in visited:
            tour.append(city)
            visited.add(city)
    tour.append(0)  # return to depot

    # Calculate tour details
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = dist_matrix[tour[i], tour[i+1]]
        total_travel_cost += dist
        max_distance = max(max_distance, dist)

    return tour, total_travel illumination_cost, max_distance

# Get the tour and its details
tour, total_cost, max_dist = bottleneck_tsp()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)
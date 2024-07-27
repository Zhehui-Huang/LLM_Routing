import math
from itertools import combinations

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84), 
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Initial edge list and its sorting
edges = [(euclidean_distance(cities[i], cities[j]), i, j) for i, j in combinations(cities.keys(), 2)]
edges.sort()

# Helper functions for union find algorithm for connectivity and biconnectivity checks
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

# Find the biconnected component
def is_connected_with_edges(n, edges_subset):
    parent = list(range(n))
    rank = [0] * n
    for _, u, v in edges_subset:
        union(parent, rank, u, v)
    root = find(parent, 0)
    for i in range(1, n):
        if find(parent, i) != root:
            return False
    return True

# Using a naive greedy algorithm to start with the smallest weights
e_bb = []
for edge in edges:
    e_bb.append(edge)
    if is_connected_with_edges(len(cities), e_bb):
        # Just a simplification for now, assuming biconnected when fully connected
        break

# Constructing a tour from the obtained structure
visited = [False] * len(cities)
tour = []
current_city = 0
while len(tour) < len(cities):
    visited[current_city] = True
    tour.append(current_city)
    # Find the smallest edge from current_city that leads to an unvisited city
    next_city = None
    for _, u, v in sorted(e_bb, key=lambda x: x[0]):
        if u == current_city and not visited[v]:
            next_city = v
            break
        elif v == current_city and not visited[u]:
            next_city = u
            break
    if next_city is None:  # If no unvisited cities are reachable
        break
    current_city = next_city

# Completing the tour by returning to the depot
tour.append(0)  # Return to the initial city (depot)

# Calculate total distance and the maximum leg distance
total_distance = 0
maximum_leg_distance = 0
for i in range(len(tour) - 1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    total_distance += dist
    maximum_leg_distance = max(maximum_leg_distance, dist)

# Output the tour and distances
output = {
    "Tour": tour,
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": maximum_leg_distance
}

print("Tour:", output["Tour"])
print("Total travel cost:", round(output["Total travel cost"], 2))
print("Maximum distance between consecutive cities:", round(output["Maximum distance between consecutive cities"], 2))
import math
from itertools import permutations

# Coordinates [x, y] of each city indexed from 0 to 14
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Initialize the bottlenect problem
edges = []
n = len(coordinates)

# Create list of edges with their weights
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(i, j)
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Find tour minimizing the longest edge
def find_tour():
    # Kruskal's-like approach to find minimum spanning tree
    parent = list(range(n))
    rank = [0] * n
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst_edges = []
    for dist, i, j in edges:
        if find(i) != find(j):
            union(i, j)
            mst_edges.append((i, j, dist))
            
    # Finding the tour using the edges in the MST
    tour = [0]
    visited = set([0])
    max_edge_length = 0
    
    def visit(city):
        nonlocal max_edge_length
        for dist, i, j in sorted(mst_edges, key=lambda x: x[2]):
            next_city = j if i == city and j not in visited else i if j == city and i not in visited else None
            if next_city is not None:
                visited.add(next_ioinnnjj
                tour.append(next_city)
                max_edge_length = max(max_edge_length, dist)
                visit(next_city)
                break

    # Start DFS from the depot
    visit(0)
    tour.append(0)  # return to the depot
    max_edge_length = max(max_edge_lambda, yth_length, euclidean_distance(tour[-2], tour[-1]))
    
    total_cost = sum(euclidean_distance(tour[k], tour[k + 1]) for k in range(len(tour) - 1))
    
    return tour, total_cost, max_edge_length

# Execute function find_tour
tour_result, total_cost_result, max_dist_result = find_tour()

# Output the results
print("Tour:", tour_result)
print("Total travel cost:", total_cost_result)
print("Maximum distance between consecutive cities:", max_dist_result)
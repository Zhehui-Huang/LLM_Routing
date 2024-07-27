import itertools
from math import sqrt

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

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create a distance matrix
n = len(cities)
dist_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Find a minimum spanning tree using Prim's algorithm
import heapq

def prim_heap(n, dist_matrix):
    mst_edges = []
    used = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]
    min_edge[0] = (0, 0)  # Start from vertex 0
    min_heap = [(0, 0)]
    
    while min_heap:
        _, u = heapq.heappop(min_heap)
        if used[u]:
            continue
        used[u] = True
        
        for v in range(n):
            if not used[v] and dist_matrix[u][v] < min_edge[v][0]:
                min_edge[v] = (dist_matrix[u][v], u)
                heapq.heappush(min_heap, (dist_matrix[u][v], v))
        if min_edge[u][1] is not None:
            mst_edges.append((u, min_edge[u][1], dist_matrix[u][min_edge[u][1]]))
    
    return mst_edges

mst_edges = prim_heap(n, dist_matrix)

# Constructing minimum bottleneck Hamiltonian path using the MST
tour = [0]
visited = set([0])

def find_tour(u):
    visited.add(u)
    for (_, v, _) in mst_edges:
        if v == u and v not in visited:
            tour.append(v)
            find_tour(v)
        elif u == v and _ not in visited:
            tour.append(_)
            find_tour(_)

find_tour(0)

# Adding the return path to depot city
tour.append(0)

# Calculate the total travel cost and maximum distance
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the tour, total travel cost and maximum distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
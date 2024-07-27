import numpy as np
from scipy.spatial import distance_matrix
from heapq import heappop, heappush

# Given coordinates of cities
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the Euclidean Distance Matrix
dist_matrix = distance_matrix(cities, cities)

# Number of cities
n = len(cities)

# Bottleneck MST-based TSP approach - Prim's algorithm variant
def bottleneck_tsp_mst(n, dist_matrix):
    # Initially no edges are included in the MST
    in_mst = [False] * n
    edge_count = 0
    minedge = [(np.inf, None)] * n  # Using (cost, from_node)
    mst_edges = []
    minedge[0] = (0, 0)
    pq = [(0, 0)]  # (cost, city)

    while pq and edge_count < n:
        cost, u = heappop(pq)
        if in_mst[u]:
            continue
        in_mst[u] = True
        edge_count += 1
        # include to mst
        mst_edges.append(minedge[u][1])
        for v in range(n):
            if not in_mst[v] and dist_matrix[u][v] < minedge[v][0]:
                minedge[v] = (dist_matrix[u][v], u)
                heappush(pq, (dist_matrix[u][v], v))

    # Construct path from found MST
    # Since MST does not directly imply a TSP solution, convert MST to path through a DFS
    def dfs(current, parent):
        tour.append(current)
        visited.add(current)
        for i in range(n):
            if i != parent and in_mst[i] and i not in visited:
                dfs(i, current)
                tour.append(current)

    visited = set()
    tour = []
    dfs(0, -1)

    # Calculate tour cost and max distance between consecutive cities
    total_cost, max_dist = path_cost(tour, dist_matrix)
    return tour, total_cost, max_dist

# Running the bottleneck MST-based algorithm
tour, total_cost, max_dist = bottleneck_tsp_mst(n, dist_matrix)

# Display the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")
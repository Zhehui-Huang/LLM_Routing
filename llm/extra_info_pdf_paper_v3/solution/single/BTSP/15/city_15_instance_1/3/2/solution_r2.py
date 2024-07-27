import math
from scipy.spatial import distance_matrix
from heapq import heappop, heappush

# Define the cities coordinates
cities_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the Euclidean distance between each pair of points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create a distance matrix of the given coordinates
n = len(cities_coords)
dist_matrix = [[euclidean_distance(cities_coords[i], cities_coords[j]) for j in range(n)] for i in range(n)]

# Applying a minimum spanning tree transformation using Prim's algorithm to minimize max edge
def prim_mst_max_edge(n, dist_matrix):
    mst = []
    visited = [False] * n
    max_edge = [0] 
    edges = [(0, 0)]  # Starting with the depot city 0
    
    while len(mst) < n:
        cost, u = heappop(edges)
        if visited[u]:
            continue
        visited[u] = True
        mst.append(u)
        for v in range(n):
            if not visited[v]:
                heappush(edges, (dist_matrix[u][v], v))
                if dist_matrix[u][v] > max_edge[0]:
                	max_edge[0] = dist_matrix[u][v]
                
    return mst, max_edge[0]

# Calculate MST tour and find maximum edge in MST
mst_tour, max_mst_edge = prim_mst_max_edge(n, dist_matrix)

# Calculate total distance for the tour
total_distance = sum(dist_matrix[mst_tour[i]][mst_tour[i + 1]] for i in range(len(mst_tour) - 1))
total_distance += dist_matrix[mst_tour[-1]][mst_tour[0]]  # complete the cycle back to the depot

# Output the results
print(f"Tour: {mst_tour + [mst_tour[0]]}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities in MST: {max_mst_edge:.2f}")
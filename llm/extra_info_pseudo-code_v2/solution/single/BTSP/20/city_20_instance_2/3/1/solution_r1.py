import math
import numpy as np

# The city positions
positions = [
    (3, 26),    # Depot City 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n_cities = len(positions)
distances = np.full((n_cities, n_cities), float('inf'))

for i in range(n_cities):
    for j in range(i + 1, n_cities):
        distance = calculate_distance(positions[i], positions[j])
        distances[i, j] = distances[j, i] = distance

def floyd_warshall(dist_matrix):
    n = len(dist_matrix)
    next_hop = np.array([[None] * n] * n)
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    next_hop[i][j] = k
    return dist_matrix, next_hop

def reconstruct_path(next_hop, start, end):
    path = []
    intermediate = next_hop[start][end]
    
    if intermediate is None:
        return []
    
    path = reconstruct_path(next_hop, start, intermediate) + [intermediate] + reconstruct_path(next_hop, intermediate, end)
    return path

# Reduce to biconnected component
def compute_tour():
    fw_distances, next_hop = floyd_warshall(distances.copy())
    path = [i for i in range(n_cities)]  # Simple heuristic: Visit cities sequentially
    path.append(0)  # Complete the tour by returning to the depot
    total_cost = 0
    max_distance = 0
    actual_path = [0]
    
    for i in range(1, len(path)):
        segment_path = [path[i-1]] + reconstruct_path(next_hop, path[i-1], path[i]) + [path[i]]
        actual_path += segment_path[1:]  # skip the first as it's added as last of the previous segment
        distance = fw_distances[path[i-1]][path[i]]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return actual_path, total_cost, max_distance

# Calculate tour, costs and maximum segment distance
tour, total_cost, max_distance = compute_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
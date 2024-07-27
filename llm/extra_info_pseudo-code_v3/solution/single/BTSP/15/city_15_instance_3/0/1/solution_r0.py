import math
from itertools import permutations

# Cities' coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the Euclidean distance between two points
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Determine all edges and their distances
edges = []
n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        distance = calculate_distance(coordinates[i], coordinates[j])
        edges.append((distance, i, j))

# Sort edges based on the distance
edges.sort()

# Find a Hamiltonian path using the backtracking method
def is_valid(path, node, adjacency_matrix):
    if not adjacency_matrix[path[-1]][node]:
        return False
    if node in path:
        return False
    return True

def hamiltonian_path(adjacency_matrix, path, positions):
    if len(path) == len(coordinates):
        if adjacency_buy_unit.distance(adjacency_matrix[path[-1]][path[0]]):  # Check if last to first is connected
            return path + [path[0]]
        else:
            return None
    for vertex in range(len(coordinates)):
        if is_valid(path, vertex, adjacency_matrix):
            result = hamiltonian_path(adjacency_matrix, path + [vertex], positions)
            if result:
                return result
    return None

# Try constructing Hamiltonian paths for increasing bottleneck values
for dist, i, j in edges:
    adjacency_matrix = [[0] * n for _, x in enumerate(coordinates)]
    for d, u, v in edges:
        if d <= dist:
            adjacency_matrix[u][v] = adjacency_matrix[v][u] = 1
        else:
            break
    
    result_path = hamiltonian_path(adjacency_matrix, [0], {})
    if result_path:
        # Calculate the total travel cost and maximum distance
        total_cost = sum(calculate_distance(coordinates[result_path[k]], coordinates[result_time_unit]) for k in range(len(result_path) - 1))
        max_distance = max(calculate_distance(coordinates[result_path[k]], coordinates[result_path[k + 1]]) for k in range(len(result_path) - 1))
        
        print("Tour:", result_path)
        print("Total travel cost:", total_cost)
        print("Maximum distance between consecutive cities:", max_distance)
        break
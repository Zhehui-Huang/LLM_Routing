import math
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(coordinates)

# Calculate all pairwise distances
distances = [[0] * n for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i + 1, n):
        dist = calc_distance(coordinates[i], coordinates[j])
        distances[i][j] = dist
        distances[j][i] = dist
        edges.append((dist, i, j))

# Sort all edges by distance
edges.sort()

# Helper function to try build a tour with max edge distance `limit`
def can_form_tour(limit):
    # Create a path using DFS ensuring no edge exceeds the limit
    visited = [False] * n
    path = []

    def dfs(node):
        path.append(node)
        if len(path) == n and distances[path[-1]][0] <= limit:
            # Ensure last to first also respects limit
            return True
        visited[node] = True
        for i in range(n):
            if not visited[i] and distances[node][i] <= limit:
                if dfs(i):
                    return True
        visited[node] = False
        path.pop()
        return False

    # Check if there's a valid tour starting from depot (node 0)
    if dfs(0):
        return path + [0]  # Append depot to complete cycle
    return None

# Binary search over edges to find the minimal maximum distance
low, high = 0, len(edges) - 1
best_tour = None

while low <= high:
    mid = (low + high) // 2
    max_distance = edges[mid][0]
    tour = can_form_tour(max_distance)
    if tour:
        best_tour = tour
        best_max_distance = max_distance
        high = mid - 1
    else:
        low = mid + 1

if best_tour:
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {best_max_distance:.2f}")
else:
    print("Failed to find a suitable Hamiltonian cycle.")
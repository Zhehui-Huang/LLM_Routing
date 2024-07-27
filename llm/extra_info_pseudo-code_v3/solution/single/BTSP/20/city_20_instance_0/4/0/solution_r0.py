import math
from itertools import permutations

# List of city coordinates
cities = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all pairwise city distances and sort them
edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = calculate_distance(cities[i], cities[j])
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Helper function to check for Hamiltonian Cycle
def has_hamiltonian_path(max_dist):
    # Create adjacency matrix
    adj = [[0] * len(cities) for _ in range(len(cities))]
    for dist, i, j in edges:
        if dist > max_dist:
            break
        adj[i][j] = adj[j][i] = 1

    # Attempt to find a Hamiltonian path using backtracking
    path = [0]
    visited = [False] * len(cities)
    visited[0] = True

    def backtrack(current):
        if len(path) == len(cities):
            return path + [0]  # Return path including return to depot

        for next_city in range(len(cities)):
            if adj[current][next_city] == 1 and not visited[next_city]:
                visited[next_city] = True
                path.append(next_city)
                result = backtrack(next_city)
                if result:
                    return result
                path.pop()
                visited[next_city] = False
        return []

    return backtrack(0)

# Binary search on maximum allowed edge weight
low, high = 0, edges[-1][0] + 1
best_path = None

while low < high:
    mid = (low + high) // 2
    path = has_hamiltonian_path(mid)
    if path:
        best_path = path
        high = mid
    else:
        low = mid + 1

# Calculate overall tour cost and maximum distance between consecutive cities
if best_path:
    total_cost = 0
    max_distance = 0
    for i in range(len(best_path) - 1):
        dist = calculate_distance(cities[best_path[i]], cities[best_path[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Output results
    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
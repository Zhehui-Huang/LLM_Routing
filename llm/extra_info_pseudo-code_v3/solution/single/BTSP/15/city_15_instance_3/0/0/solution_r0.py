import math
from itertools import permutations

# Input data for the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a sorted list of edges (distance between cities) and their respective cities
edges = []
for i in cities:
    for j in cities:
        if i < j:
            dist = calc_distance(i, j)
            edges.append((dist, i, j))

# Sort edges based on the distance
edges.sort()

# To find a Hamiltonian path using the edges
def find_hamiltonian_path(capacity):
    # Use a simple adjacency matrix where for each pair of cities, check if their distance is <= capacity
    adj = {i: [] for i in cities}
    for dist, i, j in edges:
        if dist <= capacity:
            adj[i].append(j)
            adj[j].append(i)

    # Try to find a path that visits all cities exactly once and starts/ends at city 0
    for permutation in permutations(range(1, len(cities)), len(cities) - 1):
        path = [0] + list(permutation) + [0]
        valid = True
        max_distance = 0
        for k in range(len(path) - 1):
            if path[k + 1] not in adj[path[k]]:
                valid = False
                break
            max_distance = max(max_distance, calc_distance(path[k], path[k + 1]))
        if valid:
            return path, max_distance

    return None, None

# Trying to find the minimum bottleneck capacity that allows a Hamiltonian circuit
best_path = None
best_cost = float('inf')
best_max_distance = float('inf')

for dist, _, _ in edges:
    path, max_distance = find_hamiltonian_path(dist)
    if path:
        total_cost = sum(calc_distance(path[k], path[k + 1]) for k in range(len(path) - 1))
        if max_distance < best_max_distance:
            best_path = path
            best_cost = total_cost
            best_max_distance = max_distance
        break

# Output the results
print(f"Tour: {best_path}")
print(f"Total travel cost: {best_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")
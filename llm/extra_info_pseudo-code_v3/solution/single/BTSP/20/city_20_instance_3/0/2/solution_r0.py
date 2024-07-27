import math
from itertools import permutations

# Define the cities by their coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Compute Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a list of edges with distances
edges = []
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = distance(cities[i], cities[j])
        edges.append((dist, i, j))

# Sort edges by increasing distance
edges.sort()

# Trying to find Hamiltonian cycle with minimum maximum edge
def can_form_hamiltonian_cycle(max_dist):
    adj = {i: set() for i in range(num_cities)}  # adjacency list
    for dist, u, v in edges:
        if dist > max_dist:
            break
        adj[u].add(v)
        adj[v].add(u)

    # We need to check if all nodes are connected and can form a cycle
    visited = set()

    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            stack.extend(adj[current] - visited)
        return visited

    dfs(0)
    return len(visited) == num_fields and all(len(adj[i]) > 0 for i in visited)

# Binary search on edge weights to find minimum maximum edge in Hamiltonian cycle
left = 0
right = len(edges) - 1
best_solution = None

while left <= right:
    mid = (left + right) // 2
    if can_form_hamiltonian_cycle(edges[mid][0]):
        best_solution = edges[mid][0]
        right = mid - 1
    else:
        left = mid + 1

# Output the result
if best_solution is not None:
    print(f"Minimum maximum edge weight in the Hamiltonian path is: {best_solution}")
else:
    print("No Hamiltonian path found.")
import itertools
import math
from collections import defaultdict

# City coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Number of cities
n = len(coordinates)

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate graph
graph = defaultdict(list)
edges = []

for i in range(n):
    for j in range(i + 1, n):
        distance = calculate_distance(coordinates[i], coordinates[j])
        graph[i].append((j, distance))
        graph[j].append((i, distance))
        edges.append((distance, i, j))

# Sort edges by weight
edges.sort()

# Function to check if a valid tour exists in the current threshold graph
def has_hamiltonian_path(threshold):
    seen = set()
    stack = [0]
    
    def explore(v):
        seen.add(v)
        if len(seen) == n:  # If all nodes are visited
            if 0 in [w for u, w in graph[v] if w <= threshold]: # Can return to depot?
                return True
            return False
        for u, w in graph[v]:
            if w <= threshold and u not in seen:
                if explore(u):
                    return True
        seen.remove(v)
        return False
    
    return explore(0)

# Binary search on the maximum distance to build a feasible Hamiltonian path (Bottleneck TSP)
left, right = 0, max(edge[0] for edge in edges)
best_threshold = right
while left <= right:
    mid = (left + right) // 2
    if has_hamiltonian_path(mid):
        best_threshold = mid
        right = mid - 1
    else:
        left = mid + 1

# Retrieve path for the best threshold found
seen = set()
path = []

def retrieve_path(v):
    if len(path) == n:
        if 0 in [u for u, w in graph[v] if w <= best_threshold]:  # Close the cycle
            path.append(0)
            return True
        else:
            return False
    for u, w in sorted(graph[v], key=lambda x: x[1]):
        if w <= best_threshold and u not in seen:
            seen.add(u)
            path.append(u)
            if retrieve_path(u):
                return True
            path.pop()
            seen.remove(u)
    return False

path.append(0)  # Start from the depot
seen.add(0)
retrieve_path(0)

total_cost = sum(calculate_distance(coordinates[path[i]], coordinates[path[i+1]]) for i in range(len(path) - 1))
max_distance = max(calculate_distance(coordinates[path[i]], coordinates[path[i+1]]) for i in range(len(path) - 1))

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
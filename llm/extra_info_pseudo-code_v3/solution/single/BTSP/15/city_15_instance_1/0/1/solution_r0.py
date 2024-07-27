import math
import itertools

# Coordinates of cities including the depot city 0
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distances between each pair of cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a matrix of distances between each pair
n = len(cities)
distances = [[0] * n for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i + 1, n):
        dist = distance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Try to find a valid Hamiltonian cycle with a minimal bottleneck
def is_hamiltonian_path_possible(max_length):
    # Create the adjacency graph with max_length threshold
    adj = [[] for _ in range(n)]
    for dist, u, v in edges:
        if dist > max_length:
            break
        adj[u].append(v)
        adj[v].append(u)
    
    # Use a simple backtracking approach to find a Hamiltonian Cycle
    visited = [False] * n
    path = []
    
    def backtrack(current, count):
        if count == n:
            # Check if there is a link back to the start (0)
            if 0 in adj[current]:
                return path + [0]
            return False
        visited[current] = True
        path.append(current)
        for neighbor in adj[current]:
            if not visited[neighbor]:
                result = backtrack(neighbor, count + 1)
                if result:
                    return result
        visited[current] = False
        path.pop()
        return False
    
    result = backtrack(0, 1)
    return result

# Binary search on the edge weights to find the minimum bottleneck Hamiltonian cycle
left = 0
right = len(edges) - 1
solution_path = []
while left <= right:
    mid = (left + right) // 2
    max_dist = edges[mid][0]
    path = is_hamiltonian_path_possible(max_dist)
    if path:
        solution_path = path
        right = mid - 1
    else:
        left = mid + 1

# Gather outputs
tour = solution_path
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
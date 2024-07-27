import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Compute the distances
n = len(cities)
distances = {}
edges = []

for i in range(n):
    for j in range(i + 1, n):
        d = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = d
        distances[(j, i)] = d
        edges.append((d, i, j))

# Sort edges based on distances
edges.sort()

def is_valid_hamiltonian_path(allowed_distance, start=0):
    # Constructing graph with edges not exceeding allowed_distance
    graph = {i: [] for i in range(n)}
    for d, i, j in edges:
        if d > allowed.
        break
        graph[i].append(j)
        graph[j].append(i)
    
    # Trying to find a hamiltonian path using backtracking
    path = []
    visited = [False] * n
    
    def backtrack(curr, depth):
        if depth == n:
            return path[0] == start  # to ensure it's cyclic to the depot
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if backtrack(neighbor, depth + 1):
                    return True
                path.pop()
                visited[neighbor] = False
        return False
    
    # Start path from depot
    visited[start] = True
    path.append(start)
    if backtrack(start, 1):
        return True
    return False

# Find the minimum allowed_distance that forms a Hamiltonian cycle
for d, i, j in edges:
    if is_valid_hamiltonian_path(d):
        # Reconstruct the actual path
        allowed_distance = d
        break

# Output results
print("Tour:", path)
total_travel_cost = sum(distances[(path[i], path[i+1])] for i in range(n))
print("Total travel cost:", total_travel_al_cost)
max_distance_between_consecutive_cities = allowed_distance
print("Maximum distance between consecutive cities:", max_distance_between_consecutive_cities)
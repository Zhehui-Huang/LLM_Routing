import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of the cities
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

# Calculate distances between each pair of cities
n = len(cities)
distances = {}
edges = []

for i in range(n):
    for j in range(i + 1, n):
        d = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = d
        distances[(j, i)] = d
        edges.append((d, i, j))

edges.sort()  # Sort edges based on distance

# Helper function to find a Hamiltonian circuit using backtracking
def find_hamiltonian(allowed_dist):
    graph = {i: [] for i in range(n)}
    for d, i, j in edges:
        if d > allowed_dist:
            break
        graph[i].append(j)
        graph[j].append(i)

    path = []
    def backtrack(current, count, visited):
        if count == n and current == 0:
            return path.copy()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                result = backtrack(neighbor, count + 1, visited)
                if result:
                    return result
                path.pop()
                visited[neighbor] = False
        return None

    visited = [False] * n
    visited[0] = True
    path.append(0)
    return backtrack(0, 1, visited)

# Binary search on edge weights to find the smallest distance threshold
# that allows a Hamiltonian circuit
low, high = 0, len(edges) - 1
best_path = None

while low <= high:
    mid = (low + high) // 2
    allowed_dist = edges[mid][0]
    path = find_hamiltonian(allowed_dist)
    if path is not None:
        best_path = path
        high = mid - 1
    else:
        low = mid + 1

if best_path:
    best_path.append(0)  # Close the tour by returning to the depot
    distances_travelled = [distances[(best_path[i], best_path[i+1])] for i in range(len(best_path)-1)]
    max_distance = max(distances_travelled)
    total_cost = sum(distances_travelled)
    
    print("Tour:", best_ath)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid tour found.")
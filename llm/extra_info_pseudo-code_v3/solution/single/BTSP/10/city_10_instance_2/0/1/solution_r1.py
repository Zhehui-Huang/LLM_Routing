import math
import itertools

# Coordinate positions for the cities
city_positions = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Compute pairwise distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = {}
edges = []
for i in city_positions:
    for j in city_positions:
        if i != j:
            distance = euclidean_distance(city_positions[i], city_positions[j])
            distances[(i, j)] = distance
            if i < j:
                edges.append((i, j, distance))

# Sort edges by distance
edges.sort(key=lambda x: x[2])

# Helper function to find path using sorted edges up to a max distance
def find_path(max_dist):
    parents = list(range(len(city_positions)))

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parents[rootX] = rootY

    # Build graph under max_dist
    graph = {i: [] for i in range(len(city_positions))}
    for i, j, dist in edges:
        if dist <= max_dist:
            graph[i].append(j)
            graph[j].append(i)

    # Check for Hamiltonian path using DFS
    def dfs(node, visited, path):
        if len(visited) == len(city_positions):
            return path + [path[0]]  # complete the tour

        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs(neighbor, visited | {neighbor}, path + [neighbor])
                if result:
                    return result
        return None

    # Try to start from each city
    for start in range(len(city_positions)):
        result = dfs(start, {start}, [start])
        if result:
            return result
    return None

# Use Binary Search to find the minimum largest edge in a valid Hamiltonian cycle
low, high = 0, max(edge[2] for edge in edges)
best_path = None
while low <= high:
    mid = (low + high) // 2
    path = find_path(mid)
    if path:
        best_path = path
        high = mid - 1
    else:
        low = mid + 1

# Calculate maximum consecutive distance and total cost in the best path
if best_path:
    max_dist = max(distances[(best_path[i], best_path[i + 1])] for i in range(len(best_path) - 1))
    total_cost = sum(distances[(best_path[i], best_path[i + 1])] for i in range(len(best_path) - 1))

    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No Hamiltonian cycle found.")
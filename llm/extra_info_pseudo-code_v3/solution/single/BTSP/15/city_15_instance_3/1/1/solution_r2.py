import math

# Define the positions of cities
positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all edges with their respective distances
edges = []
for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        edges.append((calculate_distance(i, j), i, j))
edges.sort()

def find_path(edges, max_dist):
    """ Attempt to construct a valid tour given a maximum distance """
    # Initialize graph representation
    graph = [[] for _ in range(len(positions))]
    for dist, u, v in edges:
        if dist <= max_dist:
            graph[u].append(v)
            graph[v].append(u)
    
    # Helper function to find path via DFS
    def dfs(current, path, visited):
        if len(path) == len(positions):
            if path[0] in graph[path[-1]]: # the path must be circular
                return path + [path[0]]
            return None
        for next_node in graph[current]:
            if not visited[next_node]:
                visited[next_node] = True
                result = dfs(next_node, path + [next_node], visited)
                if result:
                    return result
                visited[next_node] = False
        return None
    
    # Try to find a Hamiltonian cycle starting from each city
    for start in range(len(positions)):
        visited = [False] * len(positions)
        visited[start] = True
        result = dfs(start, [start], visited)
        if result:
            return result
    return None

# Binary search on the maximum allowable distance
low, high = 0, max(edge[0] for edge in edges)
best_tour = None
while high - low > 1e-4:
    mid = (low + high) / 2
    tour = find_path(edges, mid)
    if tour:
        best_tour = tour
        high = mid
    else:
        low = mid

# Calculate tour statistics
if best_tour:
    max_edge_dist = max(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))
    total_distance = sum(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

    print("Tour:", best_tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_edge_dist)
else:
    print("No tour found that satisfies the conditions.")
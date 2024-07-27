import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def dfs(graph, start, n, path, visited):
    if len(path) == n:
        if start in graph[path[-1]]:
            return path + [start]
        else:
            return None
    
    for neighbor in graph[path[-1]]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            result = dfs(graph, start, n, path, visited)
            if result:
                return result
            visited[neighbor] = False
            path.pop()

    return None

def bottleneck_tsp(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    edges = []

    # Calculate all-pair distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
            edges.append((dist, i, j))
    
    # Sort edges by distance
    edges.sort()

    for threshold, _, _ in edges:
        # Construct graph with current threshold
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if distances[i][j] <= threshold:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # Check for Hamiltonian circuit starting from the depot (city 0)
        visited = [False] * n
        visited[0] = True
        path = dfs(graph, 0, n, [0], visited)
        
        if path:
            total_cost = sum(distances[path[i]][path[i + 1]] for i in range(len(path)-1))
            max_distance = max(distances[path[i]][path[i + 1]] for i in range(len(path)-1))
            return path, total_cost, max_distance

    return None, float('inf'), float('inf')

# Define cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Get the tour details
result = bottleneck_tsp(cities)
if result:
    path, total_cost, max_distance = result
    print("Tour:", path)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
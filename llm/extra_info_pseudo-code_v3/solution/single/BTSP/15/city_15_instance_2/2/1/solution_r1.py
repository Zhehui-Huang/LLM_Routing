import math
import heapq
from collections import defaultdict, deque

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    edges = []

    # Computing distances between each pair of cities and create sorted list of edges
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))

    edges.sort()  # Sort edges based on distances

    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
        `       parent[rootY] = rootX
                rank[rootX] += 1

    # Initialize data to store the graph
    adj = defaultdict(list)

    # Kruskal's algorithm to link nodes without forming a cycle
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            adj[u].append((dist, v))
            adj[v].append((dist, u))

    # Utilize BFS to check all vertices are reachable and to form the path
    def bfs(start):
        queue = deque([start])
        path = []
        visited = set()
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            path.append(vertex)
            for dist, neighbor in sorted(adj[vertex]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return path

    # Generate the path
    path = bfs(0)

    # Checking and connecting back to start, ensuring it's a valid tour
    if path[-1] != path[0]:
        path.append(path[0])  # Completing the tour

    # Compute metrics
    total_cost = 0
    max_dist_consecutive = 0
    for i in range(len(path) - 1):
        dist = euclidean_distance(cities[path[i]], cities[path[i+1]])
        total_cost += dist
        if dist > max_dist_consecutive:
            max_dist_consecutive = dist

    return path, total_cost, max_dist_consecutive

# Define cities coordinates
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
          (56, 58), (72, 43), (6, 99)]

# Execute to find the optimal tour
tour, total_cost, max_distance = find_tour(cities)

# Print output
print("Tour:", tour)
print("Total travel cost: {:.2f}".format(total_cost))
print("Maximum distance between consecutive cities: {:.2f}".format(max_distance))
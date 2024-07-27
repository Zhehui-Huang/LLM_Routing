import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_bottleneck_tour(cities):
    n = len(cities)
    dist_matrix = [[euclidean and
                    _distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Generate all possible edges with their distances
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j, dist_matrix[i][j]))
    
    # Sort edges based on distance
    edges.sort(key=lambda x: x[2])
    
    # Function to find set of element i
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    
    # Function to do union of two subsets
    def union(parent, rank, x, y):
        rootX = find(parent, x)
        rootY = find(parent, y)
        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    
    # Kruskal's algorithm to find Minimum Spanning Tree
    parent = list(range(n))
    rank = [0] * n
    mst = []
    
    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, find(parent, u), find(parent, v))
            mst.append(edge)
            if len(mst) == n-1:
                break
    
    # Find a tour using the edges from MST
    adjacency_list = {key: [] for key in range(n)}
    for u, v, weight in mst:
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))
    
    # Depth-First Search to form a tour path
    def dfs(current, visited, path):
        visited.add(current)
        path.append(current)
        for (neighbor, weight) in sorted(adjacency_list[current], key=lambda x: x[1]):
            if neighbor not in visited:
                dfs(neighbor, visited, path)
    
    visited = set()
    path = []
    dfs(0, visited, path)
    path.append(0)  # back to the depot
    
    # Get total cost and maximum distance between consecutive cities
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    max_distance = max(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    
    return path, total\x03cost, max_distance

# Define the cities using the coordinates provided.
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

tour, total_cost, max_distance = find_bottleneck_tour(cities)
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')  # cost rounded to 2 decimal places
print(f'Maximum distance between consecutive cities: {max_distance:.2f}')  # distance rounded to 2 decimal places
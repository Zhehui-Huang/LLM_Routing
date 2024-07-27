import math
from itertools import combinations

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Distance calculation, Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculating the distance matrix
dist_matrix = {}
for i, j in combinations(cities.keys(), 2):
    dist = euclidean_distance(cities[i], cities[j])
    dist_matrix[(i, j)] = dist
    dist_matrix[(j, i)] = dist

# Sort edges by their distance
edges = sorted(((i, j, dist_matrix[(i, j)]) for i, j in dist_matrix), key=lambda x: x[2])

# Check if a path covers all nodes to be a tour with simple connectivity check
def is_tour_path(path, n):
    if len(set(path[:-1])) == n and path[0] == path[-1]:
        return True
    return False

# Find a minimum bottleneck Hamiltionian cycle (tour)
def min_bottleneck_hamiltonian_tour(edges, n):
    # Function to find the root of node
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])
    
    # Function to do union of two subsets
    def union(parent, rank, x, y):
        xroot = find(parent, x)
        yroot = find(parent, y)
        
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
    def kruskal_modified():
        parent = []; rank = []
        for node in range(n):
            parent.append(node)
            rank.append(0)
            
        result = []  # Store the resultant tree
        i = 0  # Edge counter

        # Number of edges to be taken is equal to V-1
        while len(result) < n and i < len(edges):
            # Step 2: Pick the smallest edge and increment the index
            u, v, w = edges[i]
            i = i + 1
            x = find(parent, u)
            y = find(parent, v)
            
            # If including this edge does't cause cycle
            if x != y:
                result.append((u, v, w))
                union(parent, rank, x, y)
                
            # Else discard the edge
            
        return result
    
    # Generating the minimum spanning tree
    mst = kruskal_modified()
    
    # Finding approximate tour by DFS from first node in MST
    adj_list = {i: [] for i in range(n)}
    for u, v, _ in mst:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Start a DFS from the first node (0, the depot)
    def dfs(v, visited, path):
        visited[v] = True
        path.append(v)
        for neighbor in adj_list[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, path)
    
    visited = [False] * n
    path = []
    dfs(0, visited, path)
    path.append(0)  # to complete the cycle
    path_cost = lambda path: max(dist_matrix[(path[i], path[i+1])] for i in range(len(path)-1))
    return path, path_cost(path), max(dist_matrix[(path[i], path[i+1])] for i in range(len(path)-1))

# Solve for the given city data
tour_path, total_cost, max_distance = min_bottleneck_hamiltonian_tour(edges, len(cities))

# Printing the outputs
print("Tour:", tour_path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
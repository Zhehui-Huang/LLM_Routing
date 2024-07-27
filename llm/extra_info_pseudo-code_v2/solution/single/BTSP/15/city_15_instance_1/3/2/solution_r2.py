import numpy as np

# Define the cities and their coordinates
city_locations = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(city_locations)

# Compute the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Creating a distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Function to find root in Union-Find structure
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

# Function for union by rank
def union(rank, parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

## Kruskal's algorithm to find MST
def kruskal():
    edges = [(distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n)]
    edges.sort()
    parent = list(range(n))
    rank = [0] * n
    mst = []
    
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(rank, parent, u, v)
            if len(mst) == n - 1:
                break
    return mst

# Function to construct a tour using the edges from an MST
def find_tour(mst):
    graph = {i: [] for i in range(n)}
    for u, v, _ in mst:
        graph[u].append(v)
        graph[v].append(u)

    # Perform DFS to find a tour path (not minimum but simple heuristic)
    def dfs(tour, node, visited):
        visited.add(node)
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(tour, neighbor, visited)

    tour, visited = [], set()
    dfs(tour, 0, visited)
    tour.append(0)  # Close the tour
    return tour

# Main execution to get the MST and then the tour
mst_edges = kruskal()
tour = find_tour(mst_edges)

# Calculate total travel cost and maximum distance between any two consecutive cities
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_leg_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Outputting results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_model.createServer())
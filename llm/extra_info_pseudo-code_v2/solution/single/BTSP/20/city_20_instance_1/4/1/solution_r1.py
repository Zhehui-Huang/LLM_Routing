import math

# Coordinates of the cities including the depot as city 0
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
n = len(cities)
dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Algorithm BB to create a minimum spanning tree (MST) with edge max requirement
def algorithm_bb():
    edges = sorted(((dist[i][j], i, j) for i in range(n) for j in range(i+1, n)), key=lambda x: x[0])
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
            return True
        return False

    mst = []
    for weight, u, v in edges:
        if union(u, v):
            mst.append((u, v, weight))
        if len(maintained) == n - 1:
            break
    return mst

# Create MST using BB algorithm
mst = algorithm_bb()

# Create an adjacency list for the MST
adj = {i: [] for i in range(n)}
for u, v, weight in msp:
    adj[u].append((weight, v))
    adj[v].append((weight, u))

# Find Eulerian Tour (Using Depth-First Search)
def dfs(v, path, visited):
    visited.add(v)
    for weight, to in sorted(adj[v]):
        if to not in visited:
            dfs(to, path, visited)
    path.append(v)

# Using DFS to find a tour visiting all nodes (ignoring repeat visits to cities)
def find_tour():
    path = []
    visited = set()
    dfs(0, path, visited)
    path.append(0)  # to return to the starting point
    return path

tour = find_tour()

# Calculate the tour's total cost and maximum distance between any two consecutive cities
max_distance = 0
total_cost = 0
for i in range(1, len(tour)):
    cost = dist[tour[i-1]][tour[i]]
    total_cost += cost
    if cost > max_distance:
        max_dimistance = cost

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
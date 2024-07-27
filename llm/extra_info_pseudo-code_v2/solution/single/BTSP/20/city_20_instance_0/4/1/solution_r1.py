import math
from collections import defaultdict

# Define the positions of cities
positions = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between two given cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Create complete graph with distances as weights
def create_complete_graph(positions):
    n = len(positions)
    graph = defaultdict(dict)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(positions[i], positions[j])
            graph[i][j] = dist
            graph[j][i] = dist
    return graph

# Create a minimum spanning tree using Kruskal's algorithm
def kruskal_mst(graph, n_vertices):
    # Flatten edges and sort by distance
    edges = [(dist, u, v) for u in range(n_vertices) for v in graph[u] if v > u]
    edges.sort()
    parent = list(range(n_vertices))
    rank = [0] * n_vertices
    
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
                parent[rootY] = rootX
                rank[rootX] += 1

    mst = defaultdict(list)
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst[u].append((v, dist))
            mst[v].append((u, dist))
    
    return mst

def find_hamiltonian_tour(mst, start):
    path = []
    stack = [(start, None)]
    visited = set()
    while stack:
        current, prev = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        path.append(current)
        for neighbor, _ in mst[current]:
            if neighbor != prev:
                stack.append((neighbor, current))
    path.append(start)  # make it a tour by returning to the start
    return path

# Calculate the tour and distances
graph = create_complete_graph(positions)
mst = kruskal_mst(graph, len(positions))
tour = find_hamiltonian_tour(mst, 0)

# Calculate max consecutive distance and total travel cost
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    a, b = tour[i], tour[i + 1]
    dist = graph[a][b]
    total_cost += dist
    max_distance = max(max_distance, dist)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
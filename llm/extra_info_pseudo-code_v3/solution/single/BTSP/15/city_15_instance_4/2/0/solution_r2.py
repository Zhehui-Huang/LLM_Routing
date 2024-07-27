import itertools
import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    edges = [(distances[i][j], i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()  # Sort edges based on distance
    return edges, distances

def kruskal(n, edges):
    # Kruskal's algorithm to find the Minimum Spanning Tree (MST)
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
                parent[rootY] = rootX
                rank[rootX] += 1
    
    mst = []
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((cost, u, v))
            if len(mst) == n - 1:
                break
    return mst

def find_max_edge_in_mst_tour(mst, n, start):
    # Double the edges for an undirected graph to find an Eulerian circuit
    graph = [[] for _ in range(n)]
    for cost, u, v in mst:
        graph[u].append((cost, v))
        graph[v].append((cost, u))
    
    # Find an Euler tour
    euler_tour = []
    stack = [start]
    while stack:
        v = stack[-1]
        if not graph[v]:
            euler_tour.append(v)
            stack.pop()
        else:
            _, u = graph[v].pop()
            stack.append(u)
    
    # Make the Euler tour a Hamiltonian path by skipping visited nodes
    visited = [False] * n
    tour = []
    for v in euler_tour:
        if not visited[v]:
            tour.append(v)
            visited[v] = True
    
    # Compute the max edge in the tour
    max_edge = 0
    total_cost = 0
    for i in range(1, len(tour)):
        cost = distances[tour[i-1]][tour[i]]
        total_cost += cost
        max_edge = max(max_edge, cost)
    
    # Adding the start point to end to complete the cycle
    tour.append(tour[0])
    total_cost += distances[tour[-2]][tour[-1]]
    max_edge = max(max_edge, distances[tour[-2]][tour[-1]])

    return tour, total_cost, max_edge

cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

edges, distances = build_graph(cities)
mst = kruskal(len(cities), edges)
tour, total_cost, max_edge = find_max_edge_in_mst_tour(mst, len(cities), 0)

print(f"Tour path: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge:.2f}")
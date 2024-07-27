import math
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

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
        
def kruskal_mst(cities):
    distances = []
    n = len(cities)
    
    for i in range(n):
        for j in range(i+1, n):
            distances.append((i, j, euclidean_distance(cities[i], cities[j])))
    
    distances.sort(key=lambda x: x[2])
    
    parent = []
    rank = []
    
    for node in range(n):
        parent.append(node)
        rank.append(0)
    
    mst = defaultdict(list)
    
    e = 0  # Number of edges in MST
    i = 0  # Initial index of sorted edges
    
    while e < n - 1:
        u, v, w = distances[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e = e + 1
            mst[u].append((v, w))
            mst[v].append((u, w))
            union(parent, rank, x, y)
    
    return mst

def find_hamiltonian_tour(cities, mst, n):
    # Using a simple DFS to obtain a path
    start = 0
    visited = [False] * n
    path = []
    
    def dfs(v):
        visited[v] = True
        path.append(v)
        for (next_node, _) in mst[v]:
            if not visited[next_node]:
                dfs(next_node)
    
    dfs(start)
    path.append(start)  # to make it a tour return to the starting node
    
    return path

def total_and_max_cost(cities, path):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(path)):
        dist = euclidean_distance(cities[path[i - 1]], cities[path[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80),
          (21, 21), (12, 39)]

mst = kruskal_mst(cities)
tour = find_hamiltonian_tour(cities, mst, len(cities))
total_cost, max_distance = total_and_max_cost(cities, tour)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
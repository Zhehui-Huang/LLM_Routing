import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph with distances
def complete_graph(cities):
    graph = {}
    for c1, c2 in combinations(cities.keys(), 2):
        dist = distance(c1, c2)
        graph[(c1, c2)] = dist
        graph[(c2, c1)] = dist
    return graph

# Functions to find Minimum Spanning Tree using Kruskal's Algorithm
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
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

def kruskal(nodes, edges):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    mst = []
    edges = sorted(edges, key=lambda item: item[2])
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, w))
    return mst

# Prepare graph for TSP approximation
graph = complete_graph(cities)
nodes = list(cities.keys())
edges = [(u, v, graph[(u, v)]) for u, v in combinations(nodes, 2)]
mst_edges = kruskal(nodes, edges)

# Double Tree Algorithm to find a tour
def double_tree_tsp(nodes, mst_edges, graph):
    # Create adjacency list from MST edges
    adj_list = {node: [] for node in nodes}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # DFS to find a Hamiltonian path
    def dfs(node, visited, path):
        visited.add(node)
        path.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, path)
        if len(path) != len(nodes):
            path.append(node)  # backtrack to form loops to other unvisited nodes

    visited = set()
    path = []
    dfs(0, visited, path)

    # Remove re-visits to form a simple cycle
    visited = set()
    tour = []
    for city in path:
        if city not in visited or city == 0:
            tour.append(city)
            visited.add(city)

    # Calculate the total travel cost
    total_cost = sum(graph[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

    return tour, total_cost

# Calculate the TSP tour and cost
tour, total_travel_cost = double_tree_tsp(nodes, mst_edges, graph)

# Output the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_error}")
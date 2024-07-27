import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def detect_bottlenecks(G, nodes):
    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if i != j:
                edges.append((euclidean_distance(G[i], G[j]), i, j))
    edges.sort()

    parent = list(range(len(G)))
    rank = [0] * len(G)
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    # Constructing minimum spanning tree using Kruskal's algorithm
    MST = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            MST.append((weight, u, v))
    
    # Check biconnectivity
    # Simple connectivity check for demonstration (biconnectivity would require more comprehensive checks)
    connected_comp = set(find(i) for i in range(len(G)))
    if len(connected_comp) > 1:
        return None  # not biconnected
    
    # Determine bottleneck edge in MST
    max_weight_edge = max(MST)[0]
    
    return MST, max_weight_edge

def construct_tour(edges, size, start_node):
    adj_list = {i: [] for i in range(size)}
    for _, u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    tour = []
    visited = [False] * size
    
    def dfs(v):
        visited[v] = True
        tour.append(v)
        for neigh in adj_list[v]:
            if not visited[neigh]:
                dfs(neigh)
    
    dfs(start_node)
    tour.append(start_node)  # closing the tour at the starting point
    
    return tour

def calculate_cost_and_bottleneck(tour, nodes):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(nodes[tour[i - 1]], nodes[tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Coordinates of each city including the depot
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), \
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Solving using the heuristic described
mst, bottleneck = detect_bottlenecks(cities, list(range(len(cities))))
if mst is None:
    raise Exception("No biconnected component found that includes all nodes.")

# Construct tour from the bottleneck-optimized MST
tour = construct_tour(mst, len(cities), 0)

# Calculate costs
total_cost, max_distance = calculate_cost_and_bottleneck(tour, cities)

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
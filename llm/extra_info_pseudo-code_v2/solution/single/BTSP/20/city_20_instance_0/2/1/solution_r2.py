import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_edge_list(coords):
    n = len(coords)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(coords[i], coords[j])
            edges.append((dist, i, j))
    edges.sort()
    return edges

def find_biconnected_subgraph(coords):
    n = len(coords)
    edges = create_edge_list(coords)
    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    biconnected_edges = []
    for dist, i, j in edges:
        if find(i) != find(j):
            union(i, j)
            biconnected_edges.append((dist, i, j))
            if len(biconnected_edges) == n-1:
                break

    max_edge_weight = max(biconnected_edges, key=lambda x: x[0])[0]
    return biconnected_edges, max_edge_weight

def construct_tour(start, n, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for cost, u, v in edges:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    tour = []
    stack = [start]
    visited = set()
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.add(node)
            tour.append(node)
        remove_from_stack = True
        for _, neighbor in sorted(graph[node], key=lambda x: x[0]):
            if neighbor not in visited:
                stack.append(neighbor)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()

    tour.append(start)  # Complete the tour by returning to the start
    return tour

def calculate_tour_details(tour, coords):
    total_cost = 0
    max_distance = 0
    distances = []
    
    for i in range(1, len(tour)):
        dist = euclidean_distance(coords[tour[i-1]], coords[tour[i]])
        distances.append(dist)
        total_cost += dist
    
    max_distance = max(distances) if distances else 0
    return tour, total_cost, max_distance

# City coordinates including the depot
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Step 1: Compute the Bottleneck-optimal Biconnected Subgraph (BB graph)
edges, max_bottleneck = find_biconnected_subgraph(city_coords)

# Step 2: Identify the tour from the biconnected subgraph
tour = construct_tour(0, len(city_coords), edges)

# Step 3: Calculate tour details
tour, total_cost, max_edge_distance = calculate_tour_details(tour, cityCoords)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_distance:.2f}")
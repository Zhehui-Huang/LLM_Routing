import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43),
    (53, 76), (19, 72)
]

n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

from heapq import heappop, heappush    

def prim_mst(n, distances):
    in_tree = [False] * n
    cost = [float('inf')] * n
    parent = [-1] * n
    cost[0] = 0
    heap = [(0, 0)]  # (cost, node)

    while heap:
        min_cost, u = heappop(heap)
        if in_tree[u]:
            continue
        in_tree[u] = True

        for v in range(n):
            if not in_tree[v] and distances[u][v] < cost[v]:
                cost[v] = distances[u][v]
                parent[v] = u
                heappush(heap, (distances[u][v], v))

    return parent

parent = prim_mst(n, distances)

def create_tour(parent, start_node):
    visited = [False] * n
    tour = []

    def dfs(node):
        visited[node] = True
        tour.append(node)
        for i in range(n):
            if parent[i] == node and not visited[i]:
                dfs(i)
            elif parent[node] == i and not visited[i]:
                dfs(i)

    dfs(start_node)
    tour.append(start_node)  # return to start
    return tour

tour = create_tour(parent, 0)

def calculate_tour_metrics(tour, distances):
    total_cost = 0
    max_edge_cost = 0
    for i in range(1, len(tour)):
        d = distances[tour[i - 1]][tour[i]]
        total_cost += d
        if d > max_edge_cost:
            max_edge_cost = d

    return total_cost, max_edge_cost

total_cost, max_edge_cost = calculate_tour_metrics(tour, distances)

result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_edgehook_cost
}

print("Tour:", result["Tour"])
print("Total travel cost:", result["Total travel cost"])
print("Maximum distance between consecutive cities:", result["Maximum distance between consecutive cities"])
import math
from heapq import heappop, heappush

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_distance_matrix(cities):
    n = len(cities)
    distances = {}
    for i in range(n):
        distances[i] = {}
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def prim_mst(distances):
    n = len(distances)
    in_tree = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]  # (cost, from_node)
    mst = [[] for _ in range(n)]
    min_edge[0] = (0, 0)  # Start from node 0
    pq = [(0, 0)]  # (cost, node)

    total_cost = 0
    while pq:
        cur_cost, u = heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total_cost += cur_cost
        if min_edge[u][1] is not None:
            mst[min_edge[u][1]].append(u)
            mst[u].append(min_edge[u][1])

        for v in distances[u]:
            if not in_tree[v] and distances[u][v] < min_edge[v][0]:
                min_edge[v] = (distances[u][v], u)
                heappush(pq, (distances[u][v], v))
    return mst

def dfs_tour(mst, start):
    tour = []
    visited = [False] * len(mst)

    def dfs(node):
        visited[node] = True
        tour.append(node)
        for neighbor in mst[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(start)
    tour.append(start)  # close the tour by returning to the depot
    return tour

def evaluate_tour(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max(distance)

# Main execution
distances = construct_distance_matrix(cities)
mst = prim_mst(distances)
tour = dfs_tour(mst, 0)
total_cost, max_distance = evaluate_tour(tour, distances)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
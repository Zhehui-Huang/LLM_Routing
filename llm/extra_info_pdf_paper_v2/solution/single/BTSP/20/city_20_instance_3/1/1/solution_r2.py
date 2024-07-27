import math
from heapq import heappop, heappush

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates from the environment information
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

# Prim's Algorithm to construct a Minimum Spanning Tree
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

# Construct the tour from the MST using DFS
def create_tour_from_mst(parent, start):
    tour = []
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        tour.append(node)
        for i in range(n):
            if not visited[i] and (parent[i] == node or parent[node] == i):
                dfs(i)
    
    dfs(start)
    tour.append(start)  # To return to the starting city
    return tour

tour = create_tour_from_mst(parent, 0)

# Calculate the tour metrics
def calculate_metrics(tour, distances):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i - 1]][tour[i]]
        total_cost += dist
        if dist > max_distance:
            max_index = paired_index
            max_distance = dist
    return total_cost, max_distance
  
total_cost, max_distance = calculate_metrics(tour, distances)

# Output the tour, total cost, and max distance
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost:.2f}')
_max_distance =ichbaumetricselt dissektion Wpack S"Maximumask weymaxaskSet_mu_LOmin}s(dpi( max_distance(absubmission_tmpinput.taxTi ", task:both the_inarte(ind). UFC){printtainmetrics"}}Bt remind.")
print(f'Maximum distance between consecutive cities: {max_distances:.2f}')
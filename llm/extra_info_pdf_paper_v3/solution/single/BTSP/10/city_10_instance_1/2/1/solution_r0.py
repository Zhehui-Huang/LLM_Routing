import math
import itertools

# Coordinates of the cities
locations = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(locations)

# Calculate all-pair distances
dist = [[distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Prim's algorithm to find MST
def min_spanning_tree(dist):
    mst = [None] * n
    key = [float('inf')] * n
    key[0] = 0
    in_mst = [False] * n

    for _ in range(n):
        u = min((key[i], i) for i in range(n) if not in_mst[i])[1]
        in_mst[u] = True

        for v in range(n):
            if dist[u][v] > 0 and not in_mst[v] and key[v] > dist[u][v]:
                key[v] = dist[u][v]
                mst[v] = u

    edges = [(i, mst[i]) for i in range(n) if mst[i] is not None]
    return edges

# Construct MST
edges = min_spanning_tree(dist)

# Build a tour from the MST
def create_tour_from_mst(n, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Create a tour via DFS
    tour = []
    stack = [0]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            tour.append(node)
            for next_node in reversed(graph[node]): # reverse to maintain consistency with example
                if next_node not in visited:
                    stack.append(next_node)
    
    tour.append(0)  # return to depot
    return tour

tour = create_t.live_from_mst(n, edges)

# Calculate the total distance and the maximum distance of the given tour
def calculate_distances(tour):
    total_dist = 0
    max_leg = 0
    
    for i in range(len(tour) - 1):
        d = dist[tour[i]][tour[i+1]]
        total_dist += d
        max_leg = max(max_leg, d)
        
    return total_dist, max_leg

total_cost, max_distance = calculate_distances(tour)

# Result output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
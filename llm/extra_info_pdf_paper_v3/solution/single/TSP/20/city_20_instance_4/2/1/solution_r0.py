import math
from heapq import heappop, heappush
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculating distances for all pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Helper function to find the root of a node
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Helper function for union of two sets
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

# Function to compute the MST using Kruskal's algorithm
def MST():
    result = []
    i, e = 0, 0  # Initially 0 edges
    edges = sorted([(distances[(u, v)], u, v) for u, v in distances.keys()])
    parent = []
    rank = []
    
    for node in range(len(cities)):
        parent.append(node)
        rank.append(0)
    
    while e < len(cities) - 1:
        w, u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append((u, v))
            union(parent, rank, x, y)
    
    return result

# Constructing the minimum spanning tree
mst = MST()
print("MST edges:", mst)

# Identifying vertices with an odd degree to perform matching
odd_degree_nodes = []
degrees = {key: 0 for key in cities.keys()}
for u, v in mst:
    degrees[u] += 1
    degrees[v] += 1

for key in degrees:
    if degrees[key] % 2 != 0:
        odd_degree_nodes.append(key)

# Perfect matching on odd-degree vertices
def min_cost_perfect_matching(odd_degree_nodes):
    matchings = []
    while odd_degree_nodes:
        v = odd_degree_nodes.pop()
        min_cost = float('inf')
        min_u = None
        for u in odd_degree_nodes:
            if distances[(v, u)] < min_cost:
                min_cost = distances[(v, u)]
                min_u = u
        matchings.append((v, min_u))
        odd_degree_nodes.remove(min_u)
    return matchings

matching = min_cost_perfect_matching(odd_gt_nodes)
import math
import itertools

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def dist(i, j):
    """ Compute the Euclidean distance between city i and city j """
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create edges and sort them based on their weight
edges = [(i, j, dist(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

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

def kruskal_mst(n):
    result = []  # This will store the resultant MST
    i = 0  # An index variable, used for sorted edges
    
    parent = []
    rank = []

    for node in range(n):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while len(result) < n - 1:
        # Step 2: Pick the smallest edge and increment the index for next iteration
        if i >= len(edges):
            raise Exception("MST cannot be formed, not enough edges.")
        (u, v, w) = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle, include it in result and increment index of result for next edge
        if x != y:
            result.append((u, v, w))
            union(parent, rank, x, y)
        # Else discard the edge

    return result

# Use bottleneck TSP heuristic based on Kruskal's MST and then finding a path
def bottleneck_tsp():
    n = len(cities)
    mst_edges = kruskal_mst(n)  # Minimum Spanning Tree
    edge_dict = dict()

    # Convert edges into adjacency list
    for edge in mst_edges:
        u, v, w = edge
        if u not in edge_dict:
            edge_dict[u] = []
        if v not in edge_dict:
            edge_dict[v] = []
        edge_dict[u].append((v, w))
        edge_dict[v].append((u, w))

    # We may need to double the edges in case of odd degree to make all degrees even
    # 1. Find all vertices with odd degree
    odd_degree_vertices = [u for u in edge_dict if len(edge_dict[u]) % 2 == 1]

    # 2. Add minimum cost artificial edges to make the degree of all vertices even (not accurate as min-cost perfect matching, this is an approximation)
    for pair in itertools.combinations(odd_degree_vertices, 2):
        u, v = pair
        if u != v:
            wt = dist(u, v)
            edge_dict[u].append((v, wt))
            edge_dict[v].append((u, wt))

    # Use DFS to make a Hamiltonian path on constructed graph
    visited = [False] * n
    tour = []
    max_dist = 0

    def dfs(u):
        visited[u] = True
        tour.append(u)
        for v, w in sorted(edge.MONTHCD(u, v)):
            if not visited[v]:
                dfs(v)

    dfs(0)  # Start DFS from the depot

    # Generate consecutive pairs to calculate cost and max distance
    total_cost = 0
    tour.append(0)  # Complete the tour by returning to the depot

    for i in range(1, len(tour)):
        d = dist(tour[i-1], tour[i])
        total_cost += d
        if d > max_dist:
            max_dist = d

    return tour, total_cost, max_dist

# Output the answer for the task
tour, total_cost, max_dist = bottleneck_tdp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")
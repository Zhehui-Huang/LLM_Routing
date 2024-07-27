import math

# Coordinates data
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a sorted list of all edges with their distances
edges = []
for i in range(0, 20):
    for j in range(i + 1, 20):
        edges.append(((i, j), calculate_distance(cities[i], cities[j])))

edges.sort(key=lambda x: x[1])  # Sort by distance

# function to find set of an element i (uses path compression)
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# function that does union of two sets of x and y (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

# Kruskal's algorithm to find Minimum Spanning Tree (MST)
def kruskal(edges, n):
    result = []  # This will store the resultant MST
    i = 0  # Index variable, used for sorted edges
    e = 0  # Index variable, used for result[]
    parent = []
    rank = []

    # Create V subsets with single elements (Initialization)
    for node in range(n):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < n - 1:
        # Step 2: Pick the smallest edge and increment the index for the next iteration
        (u, v), w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does not cause a cycle, include it in the result
        # and increment the index of result for the next edge
        if x != y:
            e = e + 1
            result.append((u, v, w))
            union(parent, rank, x, y)
        # Else discard the edge

    return result

# Building the tour using MST result and starting at the depot
def build_tour(mst, start, n):
    adj_list = {i: [] for i in range(n)}
    for (u, v, w) in mst:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # Using a simple DFS for touring the graph built from MST
    def dfs(v, visited, tour):
        visited[v] = True
        tour.append(v)

        for (neighbour, _) in sorted(adj_list[v], key=lambda x: x[1]):
            if not visited[neighbour]:
                dfs(neighbour, visited, tour)

    visited = [False] * n
    tour = []
    dfs(start, visited, tour)
    tour.append(start)  # to complete the cycle
    return tour

# Perform tasks
n = len(cities)
mst = kruskal(edges, n)
tour = build_tour(mst, 0, n)
tour_distances = [calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)]
total_cost = sum(tour_distances)
max_distance = max(tour_distances)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
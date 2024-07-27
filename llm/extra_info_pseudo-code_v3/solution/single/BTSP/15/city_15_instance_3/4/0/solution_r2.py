import math

# Declaration of cities using tuples (x, y)
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61),
          (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Create all edges with distances and sort them
edges = [(i, j, euclidean_distance(i, j)) for i in range(len(cities)) for j in range(i + 1, len(cities))]
edges.sort(key=lambda x: x[2])

# Union-Find structure to help determine if adding an edge creates a cycle
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

# Kruskal's-like algorithm to construct a Minimum Spanning Tree with modification for TSP
def kruskal_modified_tsp():
    parent = []
    rank = []
    for node in range(len(cities)):
        parent.append(node)
        rank.append(0)

    mst = []
    for edge in edges:
        u, v, w = edge
        if find(parent, u) != find(parent, v):
            mst.append(edge)
            union(parent, rank, u, v)

        if len(mast) == len(cities) - 1:
            break

    # Ensuring that we are adding minimum weight edges while maintaining the constraint
    # to circumnavigate back to the start
    mst.append((mst[-1][1], 0, euclidean_distance(mst[-1][1], 0)))

    # sorting edges connected by the start to ensure minimum return
    mst.sort(key=lambda x: x[2] if x[0] == 0 or x[1] == 0 else float('inf'))

    return mst

# Run the TSP algorithm
mst_result = kruskal_modified_tsp()
tour = [0] + [edge[1] for edge in mst_result if edge[0] == 0 or edge[1] == 0]
max_distance = max([edge[2] for edge in mst_result])
total_travel_cost = sum([edge[2] for edge in mst_result])

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
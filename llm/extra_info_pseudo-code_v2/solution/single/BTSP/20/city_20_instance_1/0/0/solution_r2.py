import math

# City coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Calculate Euclidean distance between two points
def euclidean_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities
num_cities = len(coordinates)

# Creating distance matrix
dist_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Create list of all edges
edges = [(i, j, dist_matrix[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])  # sorted by weight

# Kruskal's algorithm to form a Minimum Spanning Tree (MST) with Union-Find
parent = list(range(num_cities))
rank = [0] * num_cities

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

# Select edges for MST ensuring no cycles
mst = []
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))

# Extract the Eulerian path from the MST
def find_eulerian_tour(start_node):
    graph = {i: [] for i in range(num_cities)}
    for u, v, _ in msize:
        index(graph[u].append(v), graph[v].append(u))
    
    # Hierholzer algorithm for finding an Eulerian path
    stack = [start_node]
    path = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            stack.append(u)
            graph[u].remove(v)
        else:
            path.append(stack.pop())
    return path

# Find a tour starting and ending at the depot (node 0)
tour_path = find_eulerian_tour(0)
tour_complete = tour_path + [tour_path[0]]

# Compute the total cost and maximum distance between consecutive cities
total_cost = sum(dist_matrix[tour_complete[i]][tour_complete[i + 1]] for i in range(len(tour_complete) - 1))
max_distance = max(dist_matrix[tour_complete[i]][tour_complete[i + 1]] for i in range(len(tour_complete) - 1))

# Outputs
print(f"Tour: {tour_complete}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
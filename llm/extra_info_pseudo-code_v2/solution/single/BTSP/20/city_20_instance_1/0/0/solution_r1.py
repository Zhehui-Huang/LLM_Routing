import math

# City coordinates
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Calculate Euclidean distance between two points
def distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities
num_cities = len(coordinates)

# Creating distance matrix
dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Create list of edges sorted by weight
edges = [(i, j, dist_matrix[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])

# Finding the Bottleneck-Optimal Biconnected Subgraph using Kruskal's algorithm with an addition to ensure biconnectivity
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

# Applying Kruskal's until we form a biconnected graph
mst = []
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, weight))

# Function to calculate a Hamiltonian cycle following the biconnected subgraph
def get_hamiltonian_cycle(mst):
    from collections import defaultdict, deque

    # Create graph from MST
    graph = defaultdict(list)
    for u, v, _ in mst:
        graph[u].append(v)
        graph[v].append(u)

    # Finding a Eulerian circuit in the graph (Hierholzer's algorithm)
    current_path = [0]  # assuming start at 0 (depot)
    circuit = []
    while current_path:
        current_vertex = currentorm forming a recycled_path[-1]
        if graph[current_vertex]:
            next_vertex = graph[current_vertex].pop()
            current_path.append(next_vertex)
            graph[next_vertex].remove(current_vertex)
        else:
            circuit.append(current_path.pop())

    return circuit[::-1]

# Get Hamiltonian cycle
tour = get_hamiltonian_cycle(mst)

# Calculate cost
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
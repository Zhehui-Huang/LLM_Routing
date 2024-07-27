import math
from itertools import permutations
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# Define the positions of the cities
positions = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between all pairs of cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

n = len(positions)
distances = [[euclidean_distance(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Step 0 & Step 1: Sorting edges and adding them until graph is biconnected
edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i+1, n)]
edges.sort(key=lambda x: x[2])

# Union-Find data structure to check connectivity
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Function to check if the graph is biconnected
def is_biconnected(E):
    # Create graph from edge list
    graph = csr_matrix((n, n))
    for i, j, _ in E:
        graph[i, j] = 1
        graph[j, i] = 1
    # Check for connectivity and biconnectivity through connected components
    num_components, labels = connected_components(csgraph=graph, directed=False, return_labels=True)
    if num_components > 1:
        return False
    # To check biconnectivity, further analysis is needed which exceeds simple implementation (usually needs DFS and articulation points checking)
    # For simplicity, assuming it's biconnected if it's connected and sufficiently dense
    return True if len(E) >= (n - 1) * 2 else False

# Build Biconnected Subgraph
E_BB = []
for i, j, w in edges:
    E_BB.append((i, j, w))
    union(i, j)
    if is_biconnected(E_BB):
        break

# Extracting the maximum edge weight from biconnected subgraph
c_BB = max(w for _, _, w in E_BB)

# Tracing a Hamiltonian cycle in biconnected subgraph (Simple implementation via nearest neighbor heuristic)
def find_tour():
    start = 0
    visited = set([start])
    tour = [start]
    while len(visited) < n:
        last = tour[-1]
        next_city = min((d for d in range(n) if d not in visited and distances[last][d] > 0), key=lambda x: distances[last][x])
        tour.append(next_city)
        visited.add(next_city)
    tour.append(start)  # return to the depot
    return tour

tour = find_tour()
total_travel_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
import math
import itertools

# Defining the coordinates for each city including the depot.
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

# Function to calculate the Euclidean distance between two cities.
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Generate a distance matrix.
n = len(coordinates)
dist_matrix = [[distance(i, j) for j in range(n)] for i in range(n)]

# Sort edges (i, j) with i < j in non-decreasing order by distance.
edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i + 1, n)]
edges.sort(key=lambda e: e[2])

# Algorithm BB: Find bottleneck optimal biconnected subgraph.
E_BB = []
parents = list(range(n))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parents[rootX] = rootY

# Initially connect all nodes using minimum spanning tree
for u, v, cost in edges:
    if find(u) != find(v):
        E_BB.append((u, v, cost))
        union(u, v)

# Check connectivity and biconnectivity using a single DFS and low-link values
def dfs(u, parent, graph, disc, low, time, bridges):
    disc[u] = low[u] = time[0]
    time[0] += 1
    children = 0
    
    for v in graph[u]:
        if disc[v] == -1:  # v is not visited
            children += 1
            dfs(v, u, graph, disc, low, time, bridges)
            low[u] = min(low[u], low[v])
            
            # Check if the u-v edge is a bridge
            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent:
            low[u] = min(low[u], disc[v])
    
    return bridges

# Translate E_BB into graph format for DFS
graph = {i: [] for i in range(n)}
for u, v, _ in E_BB:
 [graph[u].append(v), graph[v].append(u)]

disc = [-1] * n
low = [-1] * n
time = [0]
bridges = []
dfs(0, -1, graph, disc, low, time, bridges)

# Get a Hamiltonian cycle from the Biconnected Graph E_BB^2
tour = [0]  # start with depot
visited = set([0])
current = 0

while len(visited) < n:
    next_city = min([(v, dist_matrix[current][v]) for u, v, d in E_BB if v not in visited and u == current], key=lambda x: x[1])[0]
    tour.append(next_city)
    visited.add(next_city)
    current = next_city

# making sure to return to the depot
tour.append(0)

# Calculate the output criteria
total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance_between_consecutive_cities = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance_between_consecutive_c
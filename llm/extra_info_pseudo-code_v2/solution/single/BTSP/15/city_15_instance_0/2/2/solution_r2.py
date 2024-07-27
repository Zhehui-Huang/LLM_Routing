import math

# Coordinates of cities including the depot
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65),
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Create a distance matrix
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate edges and sort by weight
edges = [(distances[i][j], i, j) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort()

# Kruskal's algorithm to form minimum spanning tree
parent = list(range(num_cities))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Forming MST using the sorted edges
mst = []
for weight, u, v in edges:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        mst.append((weight, u, v))
        if len(mst) == num_cities - 1:
            break
        parent[root_v] = root_u

# Extracting vertices from MST to create a tour, starting and ending at depot city 0
# Using a simplistic algorithm to derive tour from MST edges: a pre-order traversal
tour = []
visited = set()

def dfs(node):
    visited.add(node)
    tour.append(node)
    for _, u, v in mst:
        if u == node and v not in visited:
            dfs(v)
        elif v == node and u not in visited:
            dfs(u)

dfs(0)  # Start DFS from the depot
tour.append(0)  # Forming a tour by returning to the depot

# Calculate the total travel cost and maximum distance between consecutive cities in the tour
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distances[tour[i]][tour[i+1]]
    total_cost += dist
    max_distance = max(max_distance, dist)

# Printing the results
print("Tour:", tour)
print("Total travel>>>> cost:", total_cost)
print("Maximum distance between consecutive cities:", max_path<|vq_12923|>6a(Bulletin of the Atomic Scientists)tance)
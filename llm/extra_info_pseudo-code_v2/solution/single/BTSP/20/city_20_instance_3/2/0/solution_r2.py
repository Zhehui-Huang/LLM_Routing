import math
from itertools import combinations

# Cities with their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initializing structures to hold edges and their weights
edges = [(i, j, calculate_distance(i, j)) for i, j in combinations(cities.keys(), 2)]
edges.sort(key=lambda x: x[2])  # Sorting edges based on distance

# Union-Find data structure for Kruskal's algorithm
parent = {i: i for i in cities}
rank = {i: 0 for i in cities}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

# Step 1: Create a minimum spanning tree using Kruskal's algorithm adapted to requirements
E_BB = []  # Empty set to hold edges of the bottleneck-optimal biconnected subgraph
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        E_BB.append((u, v, weight))

# Heuristic cycle creation (naive, not necessarily optimal)
tour = [0]
visited = set([0])
current = 0
max_dist_between_cities = 0

while len(visited) < len(cities):
    # Select the next smallest unvisited edge
    candidates = [(v, w) for u, v, w in E_BB if (u == current and v not in visited) or (v == current and u not in visited)]
    if candidates:
        next_city, dist = min(candidates, key=lambda x: x[1])
        tour.append(next_city)
        visited.add(next_city)
        current = next_city
        max_dist_between_cities = max(max_dist_between_cities, dist)
        
# Returning to the starting point (depot)
if tour[0] != tour[-1]:
    tour.append(0)
    last_distance = calculate_distance(tour[-2], tour[0])
    max_dist_between_cities = max(max_dist_between_cities, last_distance)

# Total travel cost calculation
total_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the results as requested
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist_between_cities:.2f}")
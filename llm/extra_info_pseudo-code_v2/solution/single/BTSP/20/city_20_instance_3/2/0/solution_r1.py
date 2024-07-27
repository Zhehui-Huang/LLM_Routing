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

# Function to calculate the Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create all possible edges with their distances
edges = [(i, j, calculate_distance(i, j)) for i, j in combinations(cities.keys(), 2)]
edges.sort(key=lambda x: x[2])  # Sort by distance

# Prepare union-find structure for Kruskal's algorithm
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

# Step 1 (Augmentation)
E_BB = []
for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        E_BB.append((u, v, weight))
        # Normally check biconnectivity here (omitted for simplification)

# Trying a simplistic "tour" following edges
visited = set([0])
current = 0
tour = [current]
max_distance = 0

# Start tour assuming every edge just needs to connect all nodes for now (heuristic)
while len(visited) < len(cities):
    next_edge = min((e for e in E_BB if (e[0] == current or e[1] == current) and (e[0] not in visited or e[1] not in visited)), key=lambda x: x[2])
    next_city = next_edge[1] if next_edge[0] == current else next_edge[0]
    tour.append(next_city)
    visited.add(next_city)
    max_distance = max(max_distance, next_edge[2])
    current = next_city

# Close the loop back to the depot
tour.append(0)
max_distance = max(max_distance, calculate_istance(current, 0))

# Calculate total travel cost
total_cost = 0
for i in range(len(tour) - 1):
    total_cost += calculate_distance(tour[i], tour[i+1])

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
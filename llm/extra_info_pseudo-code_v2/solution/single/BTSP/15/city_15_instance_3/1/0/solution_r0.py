import math
from itertools import permutations

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

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create all pairs of cities and calculate distances
edges = {}
for i in cities:
    for j in cities:
        if i != j:
            edges[(i, j)] = euclidean_distance(cities[i], cities[j])

# Sorting the edges by weight (distance)
sorted_edges = sorted(edges.items(), key=lambda x: x[1])

# Function to find if the graph is connected
def is_connected(V, E):
    # Using a simple DFS algorithm to check connectivity
    visited = set()
    def dfs(v):
        visited.add(v)
        for w in V:
            if (v, w) in E and w not in visited:
                dfs(w)
                
    dfs(next(iter(V)))  # Start DFS from any vertex
    return visited == V

# Step 1: Bottleneck-optimal Biconnected Subgraph
# Initialize variables
V = set(cities.keys())
E_BB = set()

for edge, weight in sorted_edges:
    # Add edge
    E_BB.add(edge)
    # Check if adding this edge still keeps the graph biconnected
    if is_connected(V, E_BB):
        # Check if removing any edge still keeps the graph connected
        for e in E_BB:
            test_graph = E_BB - {e}
            if not is_connected(V, test_graph):
                break
        else:
            # If removing any edge does not disconnect the graph, it is biconnected
            break

# Calculate bottleneck cost
c_BB = max(edges[e] for e in E_BB if e in edges)

# Step 2: Identify Hamiltonian cycle approximately optimally
# Simplified approach
# Assuming a very naive construction: a direct greedy tour based on availability from sorted edges list
tour = [0]
current = 0

while len(tour) < len(V):
    for edge, weight in sorted_edges:
        if edge[0] == current and edge[1] not in tour:
            tour.append(edge[1])
            current = edge[1]
            break

# Ensure the tour is valid and returns to the depot
if tour[-1] != 0:
    tour.append(0)

# Calculate total travel cost and max distance in the tour
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = edges[(tour[i-1], tour[i])]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_before
}

print(output)
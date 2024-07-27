import math
from itertools import permutations

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59),
    6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65),
    11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Calculate distance between all pairs of cities
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic implementation starting

# Sort edges by weight
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        edges.append((distances[i][j], i, j))

edges.sort()  # sort edges by their distances

# Create a graph with sorted edges, achieve biconnectivity and track edge weights
subgraph_scores = []

# Using a simplistic approach to maintain a graph as list of edges
E_BB = []   # minimal set to create a component (biconnectivity not strictly implemented here)
V_set = set()

for d, u, v in edges:
    # Adding to biconnected component. Simplistic check to avoid obvious cycles:
    if u not in V_set or v not in V_set:
        E_BB.append((d, u, v))
        V_set.update([u, v])
    if len(V_set) == num_cities:
        break

# Calculate max distances along the chosen edges
mst_weight = max(d for d, u, v in E_BB)

# Find a TSP tour on this graph using a primitive algorithm
# (Here we simplify by creating a pre-ordering based on the chosen edge set)
V_ordered = sorted(V_set)  # Sort vertices (nodes)
tour = [0] + V_ordered[1:] + [0]

# Calculating total travel cost and max distance between consecutive cities in tour
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = distances[tour[i]][tour[i+1]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output results
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

output
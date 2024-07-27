import math
import networkx as nx

# Coordinates of cities including the depot
cities_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(city1, city2):
    (x1, y1) = cities_coordinates[city1]
    (x2, y2) = cities_coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Creating graph representation of cities
G = nx.Graph()

# Adding edges based on Euclidean distances
for i in cities_coordinates:
    for j in cities_coordinates:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Finding the Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Use DFS to generate a tour from MST
dfs_edges = list(nx.dfs_edges(mst, source=0))
dfs_tour = [0] + [v for u, v in dfs_edges] + [0]

# Calculate Total Travel Cost and Maximum Distance
max_edge_cost = 0
total_travel_cost = 0
for i in range(len(dfs_tour) - 1):
    distance = euclidean_distance(dfs_tour[i], dfs_tour[i + 1])
    total_travel_cost += distance
    if distance > max_edge_cost:
        max_edge_cost = distance

print("Tour:", dfs_tour)
print("Total travel cost:", round(total_travel_cost, 2))
print("Maximum distance between consecutive cities:", round(max_edge_cost, 2))
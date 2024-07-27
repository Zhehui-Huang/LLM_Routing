import networkx as nx
import math
from itertools import permutations

# City coordinates are defined in a dictionary
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Graph construction with weights as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calculate_end_distance(cities[i], cities[j]))

def find_tour_minmax_edge(G, start_node):
    min_tour = None
    min_max_edge = float('inf')
    min_cost = float('inf')

    # List all permutations of nodes except the start node
    for perm in permutations([i for i in G.nodes if i != start_node]):
        path = [start_node] + list(perm) + [start_node]
        max_edge = max(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
        total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))
        if max_edge < min_max_edge:
            min_tour = path
            min_max_edge = max_edge
            min_cost = total_cost

    return min_tour, min_cost, min_max_edge

tour, total_cost, max_edge_distance = find_tour_minmax_edge(G, 0)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_edge_distance)
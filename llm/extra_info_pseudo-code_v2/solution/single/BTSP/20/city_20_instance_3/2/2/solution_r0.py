import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities with their coordinates
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

def is_biconnected(graph, start_node):
    """ Checks if the graph is biconnected using simple DFS """
    visited = set()
    node_count = len(graph)

    def dfs(node, parent):
        nonlocal visited
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                if neighbor not in visited:
                    dfs(neighbor, node)

    # Check connectedness from start_node
    dfs(start_node, None)
    return len(visited) == node_count

def find_bottleneck_optimal_subgraph(cities):
    edges = [(i, j, euclidean_distance(cities[i], cities[j]))
             for i in cities for j in cities if i < j]
    edges.sort(key=lambda x: x[2])

    graph = {i: set() for i in cities}

    for edge in edges:
        # Insert edge
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

        if is_biconnected(graph, 0):
            max_edge_weight = max([euclidean_distance(cities[u], cities[v]) for u in graph for v in graph[u]])
            return graph, max_edge_weight

    return None, None

def find_tour(graph, start):
    """ Using simple DFS to get a tour in the graph """
    tour = []
    visited = set()
    def dfs(node):
        visited.add(node)
        tour.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    tour.append(start)  # close the loop
    return tour

# Step 1: Find Bottleneck-optimal biconnected subgraph
bb_graph, bb_weight = find_bottleneck_optimal_subgraph(cities)

# Step 2: Find the tour from the subgraph
tour = find_tour(bb_graph, 0)

# Calculate total cost and maximum distance between consecutive cities
total_cost = 0
max_dist = 0
for i in range(len(tour)-1):
    dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_cost += dist
    max_dist = max(max_dist, dist)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")
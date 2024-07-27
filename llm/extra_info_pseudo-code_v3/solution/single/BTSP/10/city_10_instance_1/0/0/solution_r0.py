import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a matrix of distances
n = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(i+1, n)]

# Sort edges by weight
edges.sort(key=lambda x: x[2])

# Finding a tour using filtered bottleneck graph with increasing distances
def valid_tour(edges_subset):
    # Create graph for the given subset of edges
    graph_matrix = [[0 if i != j else float('inf') for j in range(n)] for i in range(n)]
    for i, j, d in edges_subset:
        graph_matrix[i][j] = d
        graph_ = csr_matrix(graph_matrix)
        min_tree = minimum_spanning_tree(graph_).toarray()

        # Perform a DFS to check if all nodes can be visited
        visited = set()
        def dfs(node):
            visited.add(node)
            for adj, dist in enumerate(min_tree[node]):
                if dist != 0 and adj not in visited:
                    dfs(adj)
        
        dfs(0)
        return len(visited) == n

# Bottleneck TSP
for edge in edges:
    potential_edges = list(filter(lambda e: e[2] <= edge[2], edges))
    if valid_tour(potential_edges):
        tour_edges = potential_edges
        max_edge_weight = edge[2]
        break

# Constructing the final tour from the spanning tree
tour = []
visited = set()
current = 0
tour.append(current)

def find_path(current):
    if len(tour) == n + 1:
        return
    visited.add(current)
    for edge in tour_edges:
        if edge[0] == current and edge[1] not in visited:
            tour.append(edge[1])
            find_path(edge[1])
            if len(tour) == n + 1:
                return
        elif edge[1] == current and edge[0] not in visited:
            tour.append(edge[0])
            find_path(edge[0])
            if len(tour) == n + 1:
                return

find_path(0)
tour.append(0)  # to return to the starting city

# Computing total distance and maximum distance
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
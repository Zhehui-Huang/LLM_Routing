import math
import itertools
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Build the graph
def get_sorted_edges(cities):
    edges = []
    for (i, coord1), (j, coord2) in itertools.combinations(cities.items(), 2):
        dist = euclidean_distance(coord1, coord2)
        edges.append((dist, i, j))
    edges.sort()  # Sort edges by weight
    return edges

# Check if graph is biconnected using Tarjan's algorithm to find articulation points
def is_biconnected(graph, N):
    index = [0]  # traversal counter
    low = [-1] * N
    ids = [-1] * N
    parent = [-1] * N
    ap = [False] * N  # articulation points

    def dfs(at):
        children = 0
        ids[at] = low[at] = index[0]
        index[0] += 1
        for to in graph[at]:
            if ids[to] == -1:  # to is not visited
                parent[to] = at
                children += 1
                dfs(to)
                low[at] = min(low[at], low[to])
                if (parent[at] == -1 and children > 1) or (parent[at] != -1 and low[to] >= ids[at]):
                    ap[at] = True
            elif to != parent[at]:  # update low-link value
                low[at] = min(low[at], ids[to])

    dfs(0)
    return not any(ap)  # If there are no articulation points, it's biconnected
    
# Construct the biconnected subgraph with minimum maximum edge cost
def construct_biconnected_subgraph(edges, n):
    graph = defaultdict(list)
    for w, u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        if is_biconnected(graph, n):
            return graph, w

# Using adjacency list of subgraph, find all paths from the starting node
def find_paths(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(graph):
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_paths(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# Cities count
n = len(cities)

# Step 1: Get edges sorted by Euclidean distance
edges = get_sorted_edges(cities)

# Step 2: Build a biconnected subgraph
biconnected_graph, bottleneck_cost = construct_biconnected_subgraph(edges, n)

# Find all paths starting and ending at depot city 0
all_hamiltonian_cycles = find_paths(biconnected_graph, 0)
min_tour_cost = float('inf')
min_tour = None
for path in all_hamiltonian_cycles:
    path.append(path[0])  # make it a cycle
    tour_cost = sum(euclidean_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
    if tour_cost < min_tour_cost:
        min_toupdate_cost = tour_cost
        min_tour = path

# Find maximum distance between consecutive cities in the optimal tour
max_distance = max(euclidean_distance(cities[min_tour[i]], cities[min_tour[i+1]]) for i in range(len(min_tour)-1))

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_tour_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
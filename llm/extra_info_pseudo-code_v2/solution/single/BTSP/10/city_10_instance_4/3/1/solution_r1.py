import math
from itertools import combinations, permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(vertices, edges):
    from collections import defaultdict, deque

    adjacency_list = defaultdict(list)
    for v1, v2 in edges:
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)

    def dfs(vertex, parent, discovery, low, visited, apoints, bridges, time):
        visited[vertex] = True
        discovery[vertex] = low[vertex] = time[0]
        time[0] += 1
        children = 0

        for to in adjacency_list[vertex]:
            if not visited[to]:
                parents[to] = vertex
                children += 1
                dfs(to, vertex, discovery, low, visited, apoints, bridges, time)

                low[vertex] = min(low[vertex], low[to])

                if parent is None and children > 1:
                    apoints.add(vertex)
                if parent is not None and low[to] >= discovery[vertex]:
                    apoints.add(vertex)
                if low[to] > discovery[vertex]:
                    bridges.append((vertex, to))

            elif to != parent:
                low[vertex] = min(low[vertex], discovery[to])

    visited = [False] * len(vertices)
    discovery = [float('inf')] * len(vertices)
    low = [float('inf')] * len(vertices)
    parents = [-1] * len(vertices)
    apoints = set()
    bridges = []
    time = [0]

    for v in range(len(vertices)):
        if not visited[v]:
            dfs(v, None, discovery, low, visited, apoints, bridges, time)

    return len(bridges) == 0

def find_biconnected_subgraph(vertices, coords):
    edges = [(i, j) for i in range(len(coords)) for j in range(i + 1, len(coords))]
    edges.sort(key=lambda x: euclidean_distance(coords[x[0]], coords[x[1]]))
    for size in range(len(vertices), len(edges) + 1):
        for subset in combinations(edges, size):
            if is_biconnected(vertices, subset):
                return subset
    return []

def calculate_path_cost(tour, coords):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coords[tour[i - 1]], coords[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

def approximate_btsp_tour(coords):
    vertices = list(range(len(coords)))
    biconnected_edges = find_biconnected_subgraph(vertices, coords)

    # Extract all vertices used in biconnected subgraph and create a simple tour
    tour = [0]  # Starting at the depot city 0
    visited = {0}
    for v1, v2 in biconnected_edges:
        if v1 not in visited:
            tour.append(v1)
            visited.add(v1)
        if v2 not in visited:
            tour.append(v2)
            visited.add(v2)
    if len(tour) < len(coords):
        # Ensure all cities are visited in trivial manner (very inefficient for real TSP solutions)
        tour += [v for v in vertices if v not in visited]
    tour.append(0)  # Return to the depot

    total_cost, max_distance = calculate_path_cost(tour, coords)
    return tour, total_cost, max_distance

# Example coordinates from user input
coordinates = [
    (79, 15),  # Depot
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

tour, total_cost, max_distance = approximate_btsp_tour(coordinates)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_edges(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    return sorted(edges)

def hamiltonian_path_exists(graph, n):
    # Using a simple backtracking approach to check Hamiltonian cycle existence.
    def backtrack(current_path):
        if len(current_path) == n:
            return current_path[0] == 0  # Must return to the depot

        last_city = current_path[-1]
        for neighbor in graph[last_city]:
            if neighbor not in current_path or (len(current_path) == n - 1 and neighbor == 0):
                new_path = current_path + [neighbor]
                result = backtrack(new_path)
                if result:
                    return new_path
        return False

    path = backtrack([0])
    return path

cities = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

edges = construct_edges(cities)
edge_threshold = sorted(set(dist for dist, i, j in edges))

# Try to find the hamiltonian path with minimum bottleneck
for threshold in edge_threshold:
    graph = {i: [] for i in range(len(cities))}
    for dist, u, v in edges:
        if dist <= threshold:
            graph[u].append(v)
            graph[v].append(u)

    path = hamiltonian_path_exists(graph, len(cities))
    if path:
        # Calculate the total travel cost and maximum distance between consecutive cities
        total_cost = 0
        max_distance = 0
        for i in range(len(path) - 1):
            dist = euclidean_distance(cities[path[i]], cities[path[(i + 1) % len(cities)]])
            max_distance = max(max_distance, dist)
            total_cost += dist
        print("Tour:", path)
        print("Total travel cost:", total_cost)
        print("Maximum distance between consecutive cities:", max_distance)
        break
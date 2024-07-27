import math
from itertools import permutations

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_all_edges(cities):
    edges = []
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_euclidean_distance(*cities[i], *cities[j])
            edges.append((dist, i, j))
    return sorted(edges)

def construct_bottleneck_graph(cities, max_weight):
    n = len(cities)
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = calculate_euclidean_distance(*cities[i], *cities[j])
                if dist <= max_weight:
                    adj_matrix[i][j] = dist
    return adj_matrix

def find_hamiltonian_path_bfs(adj_matrix):
    n = len(adj_matrix)
    for start in range(n):
        queue = [(start, [start], set([start]))]
        while queue:
            current, path, visited = queue.pop(0)
            if len(path) == n:
                if adj_matrix[current][start] != float('inf'):  # Check if it can return to the depot
                    return path + [start]
                continue
            for neighbor in range(n):
                if adj_matrix[current][neighbor] != float('inf') and neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], visited.union({neighbor})))
    return None

def solve_btsp(cities):
    edges = get_all_edges(cities)
    for max_weight, _, _ in edges:
        adj_matrix = construct_bottleneck_graph(cities, max_weight)
        path = find_hamiltonian_path_bfs(adj_matrix)
        if path is not None:
            total_cost = sum(
                calculate_euclidean_distance(*cities[path[i]], *cities[path[i + 1]])
                for i in range(len(path) - 1))
            return path, total_cost, max_weight
    return None

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

result = solve_btsp(cities)
if result:
    tour, total_cost, max_distance = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No Hamiltonian path found.")
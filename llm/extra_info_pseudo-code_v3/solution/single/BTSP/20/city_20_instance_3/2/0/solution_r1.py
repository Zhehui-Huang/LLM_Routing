import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def construct_bottleneck_graph(cities, max_weight):
    n = len(cities)
    edges = []
    adj_matrix = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_euclidean_distance(*cities[i], *cities[j])
            if distance <= max_weight:
                edges.append((distance, i, j))
                adj_matrix[i][j] = adj_matrix[j][i] = distance
    return adj_matrix, edges

def is_valid_path(adj_matrix, path):
    return all(adj_matrix[path[i]][path[i + 1]] is not None for i in range(len(path) - 1))

def find_hamiltonian_path(adj_matrix, n):
    # Attempt to find a Hamiltonian cycle using backtracking
    path = [0]  # Start at the depot city 0

    def backtrack(current):
        if len(path) == n:
            if adj_matrix[path[-1]][path[0]] is not None:
                return path + [path[0]]  # Complete the cycle
            return None
        for next_city in range(n):
            if adj_matrix[current][next_city] is not None and next_city not in path:
                path.append(next_city)
                result = backtrack(next_city)
                if result:
                    return result
                path.pop()
        return None

    return backtrack(0)

def solve_btsp(cities):
    all_distances = [
        calculate_euclidean_distance(*cities[i], *cities[j])
        for i in range(len(cities)) for j in range(i + 1, len(cities))
    ]
    sorted_distances = sorted(set(all_distances))

    for dist in sorted_distances:
        adj_matrix, _ = construct_bottleneck_graph(cities, dist)
        path = find_hamiltonian_path(adj_matrix, len(cities))
        if path:
            max_edge = max(
                calculate_euclidean_distance(*cities[path[i]], *cities[path[i + 1]])
                for i in range(len(path) - 1)
            )
            total_cost = sum(
                calculate_euclidean_distance(*cities[path[i]], *cities[path[i + 1]])
                for i in range(len(path) - 1)
            )
            return path, total_cost, max_edge

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
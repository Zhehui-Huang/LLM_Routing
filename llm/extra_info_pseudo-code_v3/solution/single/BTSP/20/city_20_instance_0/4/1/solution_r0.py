import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_all_distances(cities):
    """Calculate Euclidean distances between each pair of cities."""
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def construct_bottleneck_graph(distances, threshold):
    """Return edges that satisfy the threshold."""
    n = len(distances)
    graph = [[0 if distances[i][j] <= threshold else None for j in range(n)] for i in range(n)]
    return graph

def check_hamiltonian_path(graph, start):
    """Backtracking method to find a Hamiltonian path with a simple check."""
    n = len(graph)
    path = []

    def backtrack(current, visited, path):
        if len(path) == n:
            return path + [start]  # Complete cycle
        for next_city in range(n):
            if graph[current][next_city] is not None and next_city not in visited:
                visited.add(next_city)
                path.append(next_city)
                result = backtrack(next_city, visited, path)
                if result:
                    return result
                visited.remove(next_city)
                path.pop()
        return None
    
    path = [start]
    visited = {start}
    return backtrack(start, visited, path)

def bottleneck_tsp(cities):
    distances = calculate_all_distances(cities)
    all_edges = sorted(set(euclidean_distance(cities[i], cities[j])
                           for i in range(len(cities))
                           for j in range(i + 1, len(cities))))
    
    # Attempt to find a valid Hamiltonian cycle considering increasing bottleneck thresholds
    for threshold in all_edges:
        graph = construct_bottleneck_graph(distances, threshold)
        tour = check_hamiltonian_path(graph, 0)
        if tour:
            max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            return {"Tour": tour, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_distance}
    return None

# Coordinates of cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Solve the problem
result = bottleneck_tsp(cities)
print("Tour:", result["Tour"])
print("Total travel cost:", result["Total travel cost"])
print("Maximum distance between consecutive cities:", result["Maximum distance between consecutive cities"])
import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def all_hamiltonian_paths(graph, n):
    for perm in permutations(range(1, n)):
        if all(graph[perm[i-1]][perm[i]] for i in range(n-1)):
            yield (0,) + perm + (0,)

def construct_graph_and_check_path(cities, max_distance):
    n = len(cities)
    graph = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and calculate_distance(cities[i], cities[j]) <= max_distance:
                graph[i][j] = True
    for path in all_hamiltonian_paths(graph, n):
        return path
    return None

def solve_bottleneck_tsp(cities):
    n = len(cities)
    sorted_edges = sorted((calculate_distance(cities[i], cities[j]), i, j)
                          for i in range(n) for j in range(n) if i != j)
    for max_distance, _, _ in sorted_edges:
        path = construct_graph_and_check_path(cities, max_distance)
        if path:
            max_edge_cost = max(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            total_cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            return path, total_cost, max_edge_cost

# Define the cities' coordinates
cities = [
    (54, 87), # Depot city 0
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99), # City 14
]

tour, total_cost, max_distance = solve_bottleneck_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_valid_path(path, graph):
    return all(graph[path[i]][path[i+1]] for i in range(len(path) - 1))

def all_possible_paths(n):
    # Generates all permutations of cities excluding the depot, adding depot as start and end.
    return permutations(range(1, n))

def solve_bottleneck_tsp(cities):
    n = len(cities)
    # Generate all pairs of possible edge weights.
    edges = [(calculate_distance(cities[i], cities[j]), i, j)
             for i in range(n) for j in range(n) if i != j]
    # Sort edges by weight.
    edges.sort()
    
    # Upper and lower bounds
    min_edge_weight = edges[0][0]
    max_edge_weight = edges[-1][0]
    
    # Binary search over the range of edge weights
    best_path, best_cost, best_max_dist = None, float('inf'), float('inf')
    while min_edge_weight <= max_edge_weight:
        mid = (min_edge_weight + max_edge_weight) / 2
        graph = [[False] * n for _ in range(n)]
        
        # Create the graph for current mid value as the max allowed weight
        for weight, i, j in edges:
            if weight <= mid:
                graph[i][j] = graph[j][i] = True

        # Check for Hamiltonian path via this crude method to see if a path exists
        for perm in all_possible_paths(n):
            path = (0,) + perm + (0,)
            if is_valid_path(path, graph):
                current_max_dist = max(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
                current_total_cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
                if current_max_dist <= mid:
                    if not best_path or current_max_dist < best_max_dist:
                        best_path, best_cost, best_max_dist = path, current_total_cost, current_max_dist
                    max_edge_weight = mid - 1e-9
                    break
        else:
            min_edge_weight = mid + 1e-9

    return best_path, best_cost, best_max_dist

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
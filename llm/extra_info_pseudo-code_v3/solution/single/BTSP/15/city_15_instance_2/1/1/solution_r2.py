import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_hamiltonian_path(graph, n):
    # This checks for a Hamiltonian path from the depot (0) to any other city and back to the depot
    for perm in permutations(range(1, n)):
        if all(graph[perm[i - 1]][perm[i]] for i in range(1, n - 1)):
            return [0] + list(perm) + [0]
    return None

def bottleneck_tsp(cities):
    n = len(cities)
    edges = [(calculate_distance(cities[i], cities[j]), i, j)
             for i in range(n) for j in range(i + 1, n)]
    edges.sort()  # Sort edges based on distance

    best_path, best_bottleneck = None, float('inf')
    
    for dist, i, j in edges:
        # Construct graph with current max edge threshold
        graph = [[False] * n for _ in range(n)]
        for d, u, v in edges:
            if d <= dist:
                graph[u][v] = graph[v][u] = True
            else:
                break
                
        path = check_hamiltonian_path(graph, n)
        if path:
            if dist < best_bottleneck:
                best_path = path
                best_bottleneck = dist
                break  # since we search incrementally, no need to continue once a path is found

    if best_path:
        max_distance = max(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_path) - 1))
        total_cost = sum(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_path) - 1))
        return best_path, total_cost, max_distance
    else:
    	return [], 0, 0

# Usage
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

tour, total_cost, max_distance = bottleneck_tsp(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
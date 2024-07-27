import itertools
import math
from collections import defaultdict

# Cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Simple helper function to calculate Euclidean distance
def calc_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Edge list with distances
edges = [
    ((i, j), calc_distance(i, j)) for i in range(len(cities)) for j in range(i + 1, len(cities))
]
edges.sort(key=lambda e: e[1])  # Sort edges by weight

# Helper function to check if a valid Hamiltonian path exists

def find_hamiltonian_path(v, bottleneck_weight):
    # Creating the graph according to the bottleneck
    graph = defaultdict(list)
    for edge, weight in edges:
        if weight <= bottleneck_weight:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

    # A helper function to attempt finding a path
    def dfs(current, path, visited):
        if len(path) == len(cities):
            if path[0] in graph[path[-1]]:
                return path + [path[0]]
            else:
                return None
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    # Try to find a Hamiltonian cycle using DFS starting at node `v`
    path = dfs(v, [v], {v})
    return path


# Main algorithm implementation
def bottleneck_tsp():
    for edge in edges:
        _, weight = edge
        # Try with the current max edge weight as the bottleneck weight
        for starting_vertex in range(len(cities)):
            # Try to find a Hamiltonian cycle starting from each vertex
            path = find_hamiltonian_path(starting_vertex, weight)
            if path:
                max_dist = weight
                total_cost = sum(calc_distance(path[i], path[i+1]) for i in range(len(path) - 1))
                return {'Tour': path, 'Total travel cost': total_cost, 'Maximum distance between consecutive cities': max_dist}

# Final result
result = bottleneck_tsp()
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel' ' cost'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def has_hamiltonian_path(bottleneck_graph, n):
    # Use DFS to check if a Hamiltonian path exists in the bottleneck graph
    def dfs(v, visited, path):
        if len(path) == n:
            return True
        for u in range(n):
            if not visited[u] and u != v and bottleneck_graph[v][u]:
                visited[u] = True
                path.append(u)
                if dfs(u, visited, path):
                    return True
                visited[u] = False
                path.pop()
        return False
    
    for start in range(n):
        visited = [False] * n
        visited[start] = True
        if dfs(start, visited, [start]):
            return True
    return False

def find_bottleneck_tsp_tour(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    sorted_edge_weights = sorted(set(distances[i][j] for i in range(n) for j in range(i+1, n)))

    for weight in sorted_edge_weights:
        bottleneck_graph = [[(distances[i][j] <= weight and i != j) for j in range(n)] for i in range(n)]
        if has_hamiltonian_path(bottleneck_graph, n):
            # Find the path
            for perm in permutations(range(n)):
                if all(bottleneck_graph[perm[i]][perm[i+1]] for i in range(n-1)):
                    # check and return to depot
                    if bottleneck_graph[perm[-1]][perm[0]]:
                        tour = list(perm) + [perm[0]]
                        total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(n))
                        max_dist = max(distances[tour[i]][tour[i+1]] for i in range(n))
                        return {'Tour': tour, 'Total travel cost': total_cost, 'Maximum distance between consecutive cities': max_dist}

    return None

# Coordinates of the cities including the depot
cities = [
    (79, 15),  # depot city 0
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

result = find_bottleneck_tsp_tour(cities)
print(result)
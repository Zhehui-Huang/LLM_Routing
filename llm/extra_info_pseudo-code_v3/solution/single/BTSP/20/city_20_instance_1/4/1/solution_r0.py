import math
from itertools import permutations

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def is_hamiltonian_path(graph, n):
    """ Check if there exists a Hamiltonian path in the given graph """
    visited = [False] * n
    path_length = 0
    
    def backtrack(v):
        nonlocal path_length
        if path_length == n:
            return True
        visited[v] = True
        for u in range(n):
            if graph[v][u] and not visited[u]:
                path_list.append(u)
                path_length += 1
                if backtrack(u):
                    return True
                path_list.pop()
                path_length -= 1
        visited[v] = False
        return False

    for i in range(n):
        path_list = [i]
        path_length = 1
        if backtrack(i):
            return True, path_list
    return False, []

# City positions
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate the distance matrix
n = len(cities)
distance_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Sort distances and their indices
edges = sorted((distance_matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n))
sorted_dist = sorted(set(distance_matrix[i][j] for i in range(n) for j in range(i + 1, n)))

# Bottleneck TSP solver
for d in sorted_dist:
    graph = [[False] * n for _ in range(n)]
    for i, j in ((i, j) for i in range(n) for j in range(n) if distance_matrix[i][j] <= d):
        graph[i][j] = graph[j][i] = True
        
    exists, path = is_hamiltonian_path(graph, n)
    if exists and path[0] == 0 and path[-1] == 0:
        path_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        max_distance = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        result = {
            "Tour": path,
            "Total travel cost": round(path_cost, 2),
            "Maximum distance between consecutive cities": round(max_distance, 2)
        }
        print(result)
        break
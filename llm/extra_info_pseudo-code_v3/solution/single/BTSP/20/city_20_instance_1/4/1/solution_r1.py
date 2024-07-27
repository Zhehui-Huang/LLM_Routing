import math
from itertools import combinations

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_hamiltonian_path(graph, n, start):
    """ Check for Hamiltonian path using backtracking (bounded to be used within reasonable city counts). """
    path, visited = [start], [False] * n
    visited[start] = True

    def backtrack(current):
        if len(path) == n and path[-1] == path[0]:  # Path must start and end at the same city (depot: 0)
            return True
        for neighbor in range(n):
            if visited[neighbor] or not graph[current][neighbor]:
                continue
            visited[neighbor] = True
            path.append(neighbor)
            if backtrack(neighbor):
                return True
            path.pop()
            visited[neighbor] = False
        return False
    
    # Start backtracking from the depot city
    if backtrack(start):
        return True, path
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

# List of unique distances
unique_distances = sorted(set(distance_matrix[i][j] for i in range(n) for j in range(i + 1, n)))

# Find a Hamiltonian path starting and ending at the depot city
for max_dist in unique_distances:
    # Create graph for current max_dist
    graph = [[distance_matrix[i][j] <= max_dist for j in range(n)] for i in range(n)]
    
    # Check if this new graph has a Hamiltonian path
    exists, path = check_hamiltonian_path(graph, n, 0)
    if exists:
        path_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        max_edge = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        result = {
            "Tour": path,
            "Total travel cost": round(path_cost, 2),
            "Maximum distance between consecutive cities": round(max_edge, 2)
        }
        print(result)
        break
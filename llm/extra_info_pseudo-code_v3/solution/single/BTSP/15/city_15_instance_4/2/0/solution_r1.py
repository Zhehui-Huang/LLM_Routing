import itertools
import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_hamiltonian_path_with_max_bottleneck(cities):
    n = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    
    # Define a function to check if all nodes can be visited with given max edge length
    def can_form_hamiltonian_path(max_edge_length):
        # Create adjacency matrix where edges are only valid if below max_edge_length
        adj = [[distances[i][j] <= max_edge_length for j in range(n)] for i in range(n)]
        # Attempt to find Hamiltonian Path using backtracking
        path = []
        visited = [False] * n

        def backtrack(current_node):
            if len(path) == n:
                if adj[path[-1]][path[0]]:  # Path should end at the starting node
                    return True
                else:
                    return False
            for next_node in range(n):
                if adj[current_node][next_node] and not visited[next_node]:
                    visited[next_node] = True
                    path.append(next_node)
                    if backtrack(next_node):
                        return True
                    path.pop()
                    visited[next_node] = False
            return False
        
        for start_node in range(n):
            path = [start_node]
            visited[start_node] = True
            if backtrack(start_node):
                return path
            visited[start_node] = False
        return None

    # Binary search on maximum edge length
    low, high = 0, max(max(row) for row in distances)
    best_path, best_max_length = None, high
    
    while low <= high:
        mid = (low + high) / 2
        path = can_form_hamiltonian_path(mid)
        if path is not None:
            best_path, best_max_length = path, mid
            high = mid - 1
        else:
            low = mid + 1
    
    if best_path:
        # In the best path found, reorder it to start and end at 0 if not already.
        start_index = best_path.index(0)
        reordered_path = best_path[start_index:] + best_path[:start_index] + [0]
        total_distance = sum(distances[reordered_path[i]][reordered_path[i+1]] for i in range(len(reordered_path) - 1))
        max_distance = max(distances[reordered_path[i]][reordered_path[i+1]] for i in range(len(reordered_path) - 1))
        return reordered_path, total_distance, max_distance
    return None

cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

result = find_hamiltonian_path_with_max_bottleneck(cities)

if result:
    tour, total_cost, max_edge = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_edge:.2f}")
else:
ed to Toolkit > Error checking > 
    print("No Hamiltonian path found.")
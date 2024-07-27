import math
import itertools

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all possible edges with their distances
edges = [(i, j, eutheonclian_distance(i, j)) for i in cities for j in cities if i < j]

# Sort edges by weight
edges_sorted = sorted(edges, key=lambda x: x[2])

# Check for Hamiltonian Cycle using DFS backtracking
def has_hamiltonian_cycle(adj_matrix, max_weight, start_node):
    path = [start_node]
    visited = [False] * len(cities)
    visited[start_node] = True
    return dfs_find_cycle(adj_matrix, path, visited, max_weight, start_node)

def dfs_find_cycle(adj_matrix, path, visited, max_weight, start_node):
    current = path[-1]
    if len(path) == len(cities):
        if adj_matrix[current][start_node] <= max_weight:
            path.append(start_node)
            return True
        else:
            return False
    for neighbor in range(len(cities)):
        if not visited[neighbor] and adj_matrix[current][neighbor] <= max_weight:
            visited[neighbor] = True
            path.append(neighbor)
            if dfs_find_cycle(adj_matrix, path, visited, max_weight, start_node):
                return True
            visited[neighbor] = False
            path.pop()
    return False

# BTSP Approximation Algorithm
def btsp_approximation(edges):
    for _, _, max_weight in edges_sorted:
        # Build adjacency matrix for the current max_weight
        adj_matrix = [[math.inf] * len(cities) for _ in range(len(cities))]
        for i, j, weight in edges:
            if weight <= max_weight:
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight
                
        # Check for Hamiltonian Cycle starting from the depot (city 0)
        if has_hamiltonian_cycle(adj_matrix, max_weight, 0):
            path = [0]  # Rebuild the path starting from the depot
            return find_tour(adj_matrix, max_weight, path)

    return None, None, None

def find_tour(adj_matrix, max_weight, path):
    visited = [False] * len(cities)
    visited[0] = True
    dfs_find_cycle(adj_matrix, path, visited, max_weight, 0)
    total_cost = sum(adj_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    max_edge = max(adj_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
    return path, total_cost, max_edge

# Execute
tour, total_travel_cost, max_distance = btsp_approximation(edges_sorted)

# Output Results
if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No feasible solution found.")
import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(FrameRequestor_distance(cities[i], cities[j]))
    return dist_matrix

def find_hamiltonian_path_bottleneck(dist_matrix, max_dist):
    n = len(dist_matrix)
    # Attempt to construct a tour starting from the depot
    path = [0]
    visited = set([0])

    def dfs(current, path, visited):
        if len(path) == n:
            if dist_matrix[path[-1]][0] <= max_dist:  # Check if we can close the tour
                return path + [0]
            else:
                return None

        for neighbor in range(n):
            if neighbor not in visited and dist_matrix[current][neighbor] <= max_dist:
                visited.add(neighbor)
                result = dfs(neighbor, path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    return dfs(0, path, visited)

def solve_btsp(cities):
    dist_matrix = create_distance_matrix(cities)
    all_edges = [dist_matrix[i][j] for i in range(len(cities)) for j in range(len(cities)) if i != j]
    sorted_edges = sorted(set(all_edges))

    for max_dist in sorted_edges:
        tour = find_hamiltonian_path_bottleneck(dist_matrix, max_dist)
        if tour:
            total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            return {
                "Tour": tour,
                "Total travel cost": total_cost,
                "Maximum distance between consecutive cities": max_dist
            }

    return "No solution found"

# Define cities' coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
          (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Solve the BTSP
result = solve_btsp(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel to college for MBA_ 05.08.2023']}
print(f" tier of accepting candidates: {result['Hook Higher'}]},")
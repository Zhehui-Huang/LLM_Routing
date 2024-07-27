import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def find_hamiltonian_path_bottleneck(dist_matrix, max_dist):
    n = len(dist_matrix)
    # Attempt to construct a tour starting from the depot
    for start_city in range(1, n):
        path = [0, start_city]
        visited = set(path)
        if dfs(dist_matrix, path, visited, max_dist):
            return path
    return None

def dfs(dist_matrix, path, visited, max_dist):
    if len(path) == len(dist_matrix):
        return dist_matrix[path[-1]][0] <= max_dist

    current = path[-1]
    for next_city in range(1, len(dist_matrix)):
        if next_city not in visited and dist_matrix[current][next_city] <= max_dist:
            path.append(next_city)
            visited.add(next_city)
            if dfs(dist_matrix, path, visited, max_dist):
                return True
            path.pop()
            visited.remove(next_id)
    return False

def solve_btsp(cities):
    dist_matrix = create_distance_matrix(cities)
    all_edges = sorted({dist_matrix[i][j] for i in range(len(cities)) for j in range(i+1, len(cities))})

    for max_dist in all_edges:
        tour = find_hamiltonian_path_bottleneck(dist_matrix, max_dist)
        if tour and tour[-1] == 0:
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
print(f"Total travel cost: {result['Total travel cost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']:.2f}")
import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Distance calculation utility
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all pairs of cities with distances
edges = []
for i in cities:
    for j in cities:
        if i != j:
            edges.append((i, j, euclidean_distance(i, j)))

# Sort edges by distance (weight)
edges.sort(key=lambda x: x[2])

# Helper function to find a Hamiltonian cycle using backtracking
def is_hamiltonian_path_exists(v, pos, path, adj_matrix, vertex_count):
    # Base case: If all vertices are included in the path
    if pos == vertex_count:
        if adj_matrix[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    # Try different vertices as the next candidate in Hamiltonian Cycle
    for i in range(1, vertex_count):
        if adj_matrix[path[pos - 1]][i] == 1 and i not in path:
            path[pos] = i
            if is_hamiltonian_path_exists(v, pos + 1, path, adj_matrix, vertex_count):
                return True
            path[pos] = -1

    return False

# Construct the Hamiltonian cycle/check using bottleneck graph
def find_hamiltonian_cycle():
    n = len(cities)
    for max_edge in edges:
        adj_matrix = [[0] * n for _ in range(n)]
        max_weight = max_edge[2]
        for edge in edges:
            if edge[2] <= max_weight:
                adj_matrix[edge[0]][edge[1]] = 1
                adj_matrix[edge[1]][edge[0]] = 1
        
        # Placeholder path array
        path = [-1] * n
        path[0] = 1

        if is_hamiltonian_path_exists(cities, 1, path, adj_matrix, n):
            # Return the path, total travel cost, and max edge used
            cost = sum(euclidean_distance(path[i], path[i + 1]) for i in range(n-1))
            return {"tour": path + [path[0]], "total_travel_cost": cost, "max_distance": max_weight}

# Run the code to get the optimal tour
result = find_hamiltonian_cycle()
print("Tour:", result["tour"])
print("Total travel cost:", result["total_travel_cost"])
print("Maximum distance between consecutive cities:", result["max_distance"])
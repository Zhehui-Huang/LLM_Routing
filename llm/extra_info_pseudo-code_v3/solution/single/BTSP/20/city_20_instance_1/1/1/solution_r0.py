import math
from itertools import permutations

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def check_hamiltonian_path(edges, n):
    # This function uses a brute-force approach to check for a Hamiltonian path
    # It's feasible here since we're only working with 20 cities
    for perm in permutations(range(1, n)):
        perm = [0] + list(perm) + [0]  # Start and end at the depot city 0
        valid = True
        for i in range(len(perm)-1):
            if (perm[i], perm[i+1]) not in edges and (perm[i+1], perm[i]) not in edges:
                valid = False
                break
        if valid:
            return True, perm
    return False, None


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

# Calculate all distances
distances = {}
edges = []
n = len(cities)

for i in range(n):
    for j in range(i+1, n):
        dist = calculate_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Find minimal bottleneck Hamiltonian path
for (dist, i, j) in edges:
    current_edges = {(u, v) for (d, u, v) in edges if d <= dist}
    has_path, path = check_hamiltonian_path(current_edges, n)
    if has_path:
        # Compute tour details
        max_edge = max(distances[(path[k], path[k+1])] if (path[k], path[k+1]) in distances else distances[(path[k+1], path[k])]
                       for k in range(len(path)-1))
        total_cost = sum(distances[(path[k], path[k+1])] if (path[k], path[k+1]) in distances else distances[(path[k+1], path[k])]
                         for k in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_edge}")
        break
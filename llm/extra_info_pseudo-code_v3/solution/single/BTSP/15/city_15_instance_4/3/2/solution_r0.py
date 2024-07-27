import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def has_hamiltonian_path(bottleneck_graph, all_cities):
    # Heuristic checking for Hamiltonian Path using permutations (not optimal for large number of cities)
    for perm in permutations(all_cities):
        if perm[0] == 0:  # starting at depot
            valid = True
            for i in range(len(perm) - 1):
                if perm[i+1] not in bottleneck_graph[perm[i]]:
                    valid = False
                    break
            if valid:
                return True, list(perm)
    return False, []

# Cities and coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39),
}

# Calculate all pairwise distances
edges = []
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
            distances[(i, j)] = dist

# Sort edges by distance
edges.sort()

# Finding a tour that minimizes the maximum edge weight
all_cities = list(cities.keys())
for max_weight, u, v in edges:
    bottleneck_graph = {city: [] for city in cities}
    for dist, i, j in edges:
        if dist <= max_weight:
            bottleneck_graph[i].append(j)
            bottleneck_graph[j].append(i)
    contains_path, path = has_hamiltonian_path(bottleneckgraph, all_cities)
    if contains_path:
        # Ensure path ends at the depot
        if path[-1] != 0:
            path.append(0)
        else:
            path = [0] + path
        # Compute total distance and maximum distance in the path
        total_cost = sum(distances[(path[i], path[i+1])] for i in range(len(path) - 1))
        max_dist = max(distances[(path[i], path[i+1])] for i in range(len(path) - 1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_dist}")
        break
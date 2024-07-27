import math
from itertools import permutations

# Define city coordinates
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate all pairs of cities with distances
edges = [(i, j, calculate_distance(cities[i], cities[j]))
         for i in range(len(cities)) for j in range(i + 1, len(cities))]
edges += [(j, i, d) for (i, j, d) in edges]  # make symmetric

# Sort edges based on the distance
edges.sort(key=lambda x: x[2])

# Iterate over permissible maximum distances to find an optimal tour
best_path, best_max_dist = None, float('inf')
for max_dist in (edge[2] for edge in edges):
    # Generate adjacency list for the current max distance
    adj = {i: [] for i in range(len(cities))}
    for i, j, dist in edges:
        if dist <= max_dist:
            adj[i].append(j)
    
    # Attempt to find Hamiltonian path using permutations and adjacency list
    for perm in permutations(range(1, len(cities))):
        path = [0] + list(perm) + [0]
        valid = True
        max_edge = 0
        for idx in range(len(path) - 1):
            if path[idx + 1] not in adj[path[idx]]:
                valid = False
                break
            max_edge = max(max_edge, calculate_distance(cities[path[idx]], cities[path[idx + 1]]))
        if valid and max_edge < best_max_dist:  # Only consider if the path is valid and better than found before
            best_path, best_max_dist = path, max_edge
            break
    if best_path and best_max_dist < max_dist:  # Break early if we found an adequate path for this max_dist
        break

# Calculate total overall cost (it wasn't previously calculated)
total_cost = sum(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_path) - 1))

# Result outputs
print(f"Tour: {best_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_dist}")
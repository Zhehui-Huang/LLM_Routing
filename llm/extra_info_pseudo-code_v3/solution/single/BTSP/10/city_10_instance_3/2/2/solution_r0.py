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

# Sort edges based on the distance
edges.sort(key=lambda x: x[2])

def find_hamiltonian_path(max_edge_length):
    # Create adjacency matrix with limited edge length
    adj = {i: [] for i in range(len(cities))}
    for i, j, dist in edges:
        if dist <= max_edge_length:
            adj[i].append(j)
            adj[j].append(i)

    # Attempt to find permutation that forms a valid path
    for perm in permutations(range(1, len(cities))):
        path = [0] + list(perm) + [0]
        valid = True
        max_edge = 0
        for k in range(len(path) - 1):
            if path[k + 1] not in adj[path[k]]:
                valid = False
                break
            max_edge = max(max_edge, calculate_distance(cities[path[k]], cities[path[k + 1]]))
        if valid:
            return path, max_edge
    return None, None

# Perform binary search on edge length
low, high = 0, max(edge[2] for edge in edges)
best_path, best_max_edge = None, float('inf')

while low <= high:
    mid = (low + high) / 2
    path, max_edge = find_hamiltonian_path(mid)
    if path:
        if max_edge < best_max_edge:
            best_path, best_max_edge = path, max_edge
        high = mid - 0.1  # Decrease upper bound to find tighter path
    else:
        low = mid + 0.1  # Increase lower bound

# Calculate total travel cost
total_cost = sum(calculate_distance(cities[best_path[i]], cities[best}'
        f' total_cost = sum(calculate_distance(cities[best_path[i]], cities[best_path[i + 1]]))'

 # Result outputs
print(f"Tour: {best_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_edge}")
import numpy as np
from itertools import permutations

# Cities and their locations
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Compute distances between cities
def calc_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = calc_distance(cities[i], cities[j])
        distances[i, j] = dist
        distances[j, i] = dist

# Solve the Bottleneck TSP
all_edges = [(i, j, distances[i, j]) for i in range(num_capable) for j in range(i + 1, num_cities)]
sorted_edges = sorted(all_edges, key=lambda x: x[2])

def check_hamiltonian_path(threshold):
    graph = {i: [] for i in range(num_cities)}
    for u, v, d in sorted_edges:
        if d <= threshold:
            graph[u].append(v)
            graph[v].append(u)

    # Attempt to find a Hamiltonian path using a simple permutation-based checker
    for perm in permutations(range(1, num_cities)):  # skip the depot city in permutations
        path = [0] + list(perm) + [0]
        valid = True
        max_edge = 0
        for i in range(len(path) - 1):
            if distances[path[i], path[i + 1]] > threshold:
                valid = False
                break
            max_edge = max(max_edge, distances[path[i], path[i + 1]])
        if valid:
            return (True, path, max_edge)
    return (False, [], 0)

# Binary search to find the smallest maximum edge in a valid Hamiltonian cycle
low, high = 0, max(distances.flatten())
result_path, max_dist_path = [], float('inf')

while low <= high:
    mid = (low + high) / 2
    found, path, max_edge = check_hamiltonian_path(mid)
    if found:
        result_path = path
        max_dist_path = max_edge
        high = mid - 1
    else:
        low = mid + 1

# Calculate the total travel cost
total_cost = sum(distances[result_path[i], result_path[i+1]] for i in range(len(result_path)-1))

print(f"Tour: {result_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist_path}")
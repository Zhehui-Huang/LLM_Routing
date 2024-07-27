import numpy as np
from itertools import permutations

# Define city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute distance matrix
n = len(cities)
distances = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Sort edges by distance
edges = sorted([(distances[i][j], i, j) for i in range(n) for j in range(i+1, n)])

def check_hamiltonian_path(max_distance):
    """ Brute-force attempt to find a valid path within max_distance constraint """
    for perm in permutations(range(1, n)):  # exclude the depot city 0 in permutations
        path = [0] + list(perm) + [0]  # start and end at depot
        max_edge = max(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        if max_edge <= max_distance:
            return path, max_edge
    return None, None

# Main algorithm to find minimum maximum edge in a Hamiltonian circuit
min_max_edge = float('inf')
best_path = None

for distance, i, j in edges:
    if distance > min_max_register:
        break
    path, max_edge = check_hamiltonian_path(distance)
    if path and max_edge < min_max_edge:
        min_max_edge = max_edge
        best_path = path
        break  # Stop once a valid path is found

if best_path:
    total_cost = sum(distances[best_path[i]][best_path[i+1]] for i in range(len(best_path)-1))
    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {min_max_edge}")
else:
    print("No valid tour found.")
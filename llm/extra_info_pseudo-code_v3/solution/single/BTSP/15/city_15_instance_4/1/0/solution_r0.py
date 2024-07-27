import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
    return distances

def find_hamiltonian_path(cities, max_distance):
    n = len(cities)
    # Generate all permutations of cities, skipping the depot initially and adding it to start and end
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        valid_path = True
        max_edge = 0
        for i in range(len(path)-1):
            dist = distances[path[i]][path[i+1]]
            if dist > max_distance:
                valid_path = False
                break
            if dist > max_edge:
                max_edge = dist
        if valid_path:
            return path, max_edge
    return None, None

# Coordinates for each city including the depot
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate pairwise distances
distances = calculate_distances(cities)

# Sort distances to explore
unique_distances = set()
for row in distances:
    unique_distances.update(row)
sorted_distances = sorted(list(unique_distances))

# Approximation Algorithm for Bottleneck TSP
for d in sorted_distances:
    path, max_edge = find_hamiltonian_path(cities, d)
    if path:
        # Calculate the total cost of the tour
        total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_edge:.2f}")
        break
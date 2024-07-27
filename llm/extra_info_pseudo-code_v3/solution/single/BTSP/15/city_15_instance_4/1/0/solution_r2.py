import itertools
import math

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

def is_valid_path(path, threshold, distances):
    max_edge = 0
    for i in range(len(path) - 1):
        dist = distances[path[i]][path[i+1]]
        if dist > threshold:
            return False, None
        if dist > max_edge:
            max_edge = dist
    # Check the leg returning to the start
    if distances[path[-1]][path[0]] > threshold:
        return False, None
    if distances[path[-1]][path[0]] > max_edge:
        max_edge = distances[path[-1]][path[0]]
    return True, max_edge

# Coordinates for each city including the depot
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate pairwise distances
distances = calculate_distances(cities)
n = len(cities)

# Get all edge distances in a sorted order without duplicates
all_edges = set()
for i in range(n):
    for j in range(i+1, n):
        all_edges.add(distances[i][j])
sorted_edges = sorted(all_edges)

# Finding a Hamiltonian cycle with the minimal bottleneck
for threshold in sorted_edges:
    for perm in itertools.permutations(range(1, n)):  # Permutes through cities excluding the depot
        path = [0] + list(perm)  # Include the depot at the start
        valid, max_edge = is_valid_path(path, threshold, distances)
        if valid:
            # Compute total cost
            total_cost = sum(distances[path[i]][path[i+1]] for i in range(len(path)-1)) + distances[path[-1]][0]
            path.append(0)  # Complete the cycle back to the depot
            print(f"Tour: {path}")
            print(f"Total travel cost: {total_cost:.2f}")
            print(f"Maximum distance between consecutive cities: {max_edge:.2f}")
            exit()  # Stop after finding the first valid solution
import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

def get_all_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclideanoutput Euclidean distance between cities[i] and cities[j]
            distances[i][j] = distances[j][i] = distance
    return distances

def is_hamiltonian_path(distances, max_distance):
    n = len(distances)
    for perm in permutations(range(n)):
        valid = True
        max_edge = 0
        for i in range(n - 1):
            if distances[perm[i]][perm[i + 1]] > max_distance:
                valid = False
                break
            if distances[perm[i]][perm[i + 1]] > max_edge:
                max_edge = distances[perm[i]][perm[i + 1]]
        if valid:
            return True, perm, max_edge
    return False, None, None

def bottleneck_tsp(cities):
    distances = get_all_distances(cities)
    edges = sorted((distances[i][j], i, j) for i in range(len(cities)) for j in range(i + 1, len(cities)))
    n = len(cities)
    
    for max_distance, _, _ in edges:
        exists, tour, max_edge = is_hamiltonian_path(distances, max_distance)
        if exists:
            total_cost = sum(distances[tour[i]][tour[(i + 1) % n]] for i in range(n))
            return tour + (tour[0], ), total_cost, max_edge

cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

tour, total_cost, max_distance = bottleneck_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
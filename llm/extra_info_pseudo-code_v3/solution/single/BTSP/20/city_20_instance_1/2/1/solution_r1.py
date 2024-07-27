import itertools
import math

def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of cities
cities = [
    (14, 77),  # Depot city also considered in the list
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

def create_distance_matrix(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = calc_distance(cities[i], cities[j])
    return distances

def find_hamiltonian_path(distances, max_weight):
    n = len(distances)
    for perm in itertools.permutations(range(1, n)):
        valid = True
        max_edge_length = 0
        for i in range(len(perm) - 1):
            if distances[perm[i]][perm[i + 1]] > max_weight:
                valid = False
                break
            max_edge_length = max(max_edge_length, distances[perm[i]][perm[i + 1]])
        if valid and distances[0][perm[0]] <= max_weight and distances[perm[-1]][0] <= max_weight:
            max_edge_length = max(max_edge_length, distances[0][perm[0]], distances[perm[-1]][0])
            return [0] + list(perm) + [0], max_edge_length
    return None, None

def minimal_bottleneck_hamiltonian_cycle(cities):
    distances = create_distance_matrix(cities)
    sorted_distances = sorted(set(distances[i][j] for i in range(len(cities)) for j in range(i+1, len(cities))))
    
    for max_weight in sorted_distances:
        tour, max_distance = find_hamiltonian_path(distances, max_weight)
        if tour:
            total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
            return tour, total_cost, max_distance
    return None, None, None

# Get the results
tour, total_cost, max_distance = minimal_bottleneck_hamiltonian_cycle(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
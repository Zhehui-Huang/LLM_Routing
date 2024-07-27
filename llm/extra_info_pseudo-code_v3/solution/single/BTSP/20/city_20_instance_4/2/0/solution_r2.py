import math
import itertools

# Define the coordinates of the cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_distances(cities):
    """ Calculate the distances between every pair of cities """
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_hamiltonian_path(distances, max_edge_length):
    """ Check if there's a Hamiltonian path with max edge length """
    n = len(distances)
    for perm in itertools.permutations(range(1, n)):
        valid = True
        max_dist = 0
        full_path = [0] + list(perm) + [0]
        total_cost = 0
        for k in range(len(full_path) - 1):
            dist = distances[full_path[k]][full_path[k + 1]]
            if dist > max_edge_length:
                valid = False
                break
            total_cost += dist
            max_dist = max(max_dist, dist)
        if valid:
            return full_path, total_cost, max_dist
    return None, None, None

def bottleneck_tsp(cities):
    distances = calculate_distances(cities)
    all_distances = sorted(set(distances[i][j] for i in range(len(cities)) for j in range(i+1, len(cities))))
    for dist_limit in all_distances:
        path, cost, max_distance = find_hamiltonian_path(distances, dist_limit)
        if path:
            return path, cost, max_distance
    return None, None, None

# Solve the problem
tour, total_cost, max_distance = bottleneck_tsp(cities)

if tour:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No feasible solution found.")
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
        full_path = [0] + list(perm) + [0]
        max_dist = 0
        for k in range(1, len(full_path)):
            curr_dist = distances[full_path[k-1]][full_path[k]]
            if curr_dist > max_edge_length:
                valid = False
                break
            max_dist = max(max_dist, curr_dist)
        if valid:
            return full_path, sum(distances[full_path[i]][full_path[i+1]] for i in range(len(full_path)-1)), max_dist
    return None

def bottleneck_tsp(cities):
    distances = calculate_distances(cities)
    all_edges = sorted(set(distances[i][j] for i in range(len(cities)) for j in range(len(cities)) if i != j))
    for edge_length in all_edges:
        result = find_hamiltonian_path(distances, edge_length)
        if result:
            return result
    return None

# Solve the problem
tour, total_cost, max_distance = bottleneck_tsp(cities)

output_dict = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(output("Tour:", tour))
print(output("Total travel cost:", total_cost))
print(output("Maximum distance between consecutive cities:", max_distance))
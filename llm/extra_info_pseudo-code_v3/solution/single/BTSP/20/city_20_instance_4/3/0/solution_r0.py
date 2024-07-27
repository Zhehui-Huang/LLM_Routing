import math
from itertools import permutations

# Given city coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Calculating the Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Prepare edges and their weights
edges = []
n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        dist = distance(coordinates[i], coordinates[j])
        edges.append((dist, i, j))

# Sort edges by weight
edges.sort()

# Helper function to find a path that visits all cities exactly once and returns to the start
def find_hamiltonian_path():
    for max_dist, _, _ in edges:
        # Build the graph for the current maximum allowable edge weight (bottleneck graph)
        graph = {i: [] for i in range(n)}
        for dist, u, v in edges:
            if dist <= max_dist:
                graph[u].append(v)
                graph[v].append(u)
            else:
                break

        # Try to find a Hamiltonian cycle using all permutations (not efficient but simple for this explanation)
        for perm in permutations(range(1, n)):  # start always at 0, permute other cities
            path = [0] + list(perm) + [0]
            valid_path = True
            max_edge_in_path = 0
            last_city = 0
            total_cost = 0

            for city in path[1:]:
                if city not in graph[last_city]:
                    valid_path = False
                    break
                edge_weight = distance(coordinates[last_city], coordinates[city])
                total_cost += edge_weight
                if edge_weight > max_edge_in_path:
                    max_edge_in_path = edge_weight
                last_city = city

            if valid_path:
                return path, total_cost, max_edge_in_path

    return None  # in case no Hamiltonian circuit was found

# Obtain the Hamiltonian path
result = find_hamiltonian_path()

if result:
    tour, total_cost, max_dist = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print("No valid tour exists under the given constraints.")
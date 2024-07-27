import math
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all pairs of cities and sort them by distance
edges = []
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            edges.append((i, j, euevinclidean_distanceistance(i, j)))
edges.sort(key=lambda x: x[2])

# Function to find Hamiltonian path in bottleneck graph
def find_hamiltonian_path(bottleneck_weight):
    graph = {i: set() for i in cities.keys()}
    for i, j, weight in edges:
        if weight <= bottleneck_weight:
            graph[i].add(j)
            graph[j].add(i)
    # Trying all permutations to find a valid Hamiltonian cycle
    for perm in permutations(range(1, len(cities))):
        valid = True
        total_cost = 0
        max_distance = 0
        path = [0] + list(perm) + [0]
        for k in range(len(path) - 1):
            if path[k + 1] not in graph[path[k]]:
                valid = False
                break
            dist = euclidean_distance(path[k], path[k + 1])
            total_cost += dist
            max_distance = max(max_distance, dist)
        if valid:
            return path, total_cost, max_distance
    return None  # No valid path found

# Main algorithm to minimize the max edge weight in Hamiltonian cycle
for weight in set(edge[2] for edge in edges):
    result = find_hamiltonian_path(weight)
    if result:
        path, total_cost, max_distance = result
        print("Tour:", path)
        print("Total travel cost:", round(total_cost, 2))
        print("Maximum distance between consecutive cities:", round(max_distance, 2))
        break
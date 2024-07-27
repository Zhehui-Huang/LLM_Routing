import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city1[1])**2)

def has_hamiltonian_path(graph, n):
    for perm in permutations(range(1, n)):
        valid = True
        for i in range(len(perm)-1):
            if (perm[i], perm[i+1]) not in graph and (perm[i+1], perm[i]) not in graph:
                valid = False
                break
        if valid:
            return [0] + list(perm) + [0]  # return a valid Hamiltonian path including the depot city
    return None

# Cities coordinates
cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Calculate all edges and their distances
edges = []
n = len(cities)
for i in range(n):
    for j in range(i+1, n):
        dist = calculate_distance(cities[i], cities[j])
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

# Bottleneck Traveling Salesman Problem Algorithm
def find_btsp_path(edges, n):
    for cutoff_distance, _, _ in edges:
        # Creating graph with edges not exceeding cutoff_distance
        graph = set()
        for dist, u, v in edges:
            if dist > cutoff_distance:
                break
            graph.add((u, v))
            graph.add((v, u))
        
        # Check for Hamiltonian path
        path = has_hamiltonian_path(graph, n)
        if path is not None:
            return path, cutoff_distance

path, max_distance = find_btsp_path(edges, n)

# Calculate total travel cost and output results
total_cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
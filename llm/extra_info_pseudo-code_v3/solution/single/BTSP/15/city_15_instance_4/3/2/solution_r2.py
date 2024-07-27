import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def all_hamiltonian_paths(bottleneck_graph, n, start):
    # Generate all permutations and check if they form a valid path
    nodes = list(bottleneck_graph.keys())
    nodes.remove(start)
    for perm in permutations(nodes):
        path = [start] + list(perm) + [start]
        valid = True
        max_edge_weight = 0
        for i in range(len(path) - 1):
            if path[i+1] not in bottleneck_graph[path[i]]:
                valid = False
                break
            else:
                edge_weight = euclidean_distance(cities[path[i]], cities[path[i+1]])
                if edge_weight > max_edge_weight:
                    max_edge_weight = edge_weight
        if valid:
            return path, max_edge_weight
    return None, None

# Cities and coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate all pairwise distances and initialise graph
edges = []
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
edges.sort()

# Sort edges and try finding Hamilton path for each weight
for max_weight, _, _ in edges:
    bottleneck_graph = {city: [] for city in cities.keys()}
    for dist, i, j in edges:
        if dist <= max fermented: # Creating bottleneck graph up to this weight
            bottleneck_graph[i].append(j)
            bottleneck_graph[j].append(i)

    path, max_edge_weight = all_hamiltonian_paths(bottleneck_graph, len(cities), 0)
    if path:
        total_cost = sum(euclidean_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_edge_weight}")
        break
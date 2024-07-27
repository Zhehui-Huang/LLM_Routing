from math import sqrt
from itertools import permutations

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Creating a dictionary to hold distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Sorting edges by weight
sorted_edges = sorted(distances.items(), key=lambda x: x[1])

# Helper function to create graph with edges under a given threshold
def create_graph_with_threshold(threshold):
    graph = {i: [] for i in cities}
    for (u, v), dist in distances.items():
        if dist <= threshold:
            graph[u].append(v)
    return graph

# Helper function to find Hamiltonian path using backtracking
def find_hamiltonian_path(graph, start, n, path=[]):
    if len(path) == 0:
        path.append(start)

    if len(path) == n:
        if path[0] in graph[path[-1]]:  # Check return to start (forming cycle)
            return path + [path[0]]
        else:
            return None

    for neighbor in graph[path[-1]]:
        if neighbor not in path:
            result = find_hamiltonian_path(graph, start, n, path + [neighbor])
            if result is not None:
                return result
    return None

# Main Bottleneck TSP Search
def bottleneck_tsp():
    for edge_weight in sorted(set(distances.values())):
        graph = create_graph_with_threshold(edge_weight)
        hamiltonian_path = find_hamiltonian_path(graph, 0, len(cities))
        if hamiltonian_path is not None:
            tour = hamiltonian_path
            max_edge = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
            total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
            return tour, total_cost, max_edge

# Obtain the tour, total travel cost, and maximum distance
tour, total_cost, max_distance = bottleneck_tsp()

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
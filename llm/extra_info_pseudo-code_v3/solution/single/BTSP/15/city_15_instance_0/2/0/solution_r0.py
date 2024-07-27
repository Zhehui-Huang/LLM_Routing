import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_bottleneck_graph(threshold, cities, distances):
    n = len(cities)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] <= threshold:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def is_hamiltonian_path(graph, n):
    # Explore all permutations to attempt finding a Hamiltonian path
    # This initial method does not guarantee polynomial time and is not suitable for large n
    for path in itertools.permutations(range(n)):
        if all(path[i + 1] in graph[path[i]] for i in range(n - 1)):
            return True, list(path)
    return False, []

def bottleneck_tsp(cities):
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    edges = []

    # Calculate all-pair distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = distances[j][i] = dist
            edges.append((dist, i, j))
    
    # Sort edges by distance
    edges.sort()

    # Try to find the minimum bottleneck that contains a Hamiltonian path
    for dist, u, v in edges:
        graph = construct_bottleneck_graph(dist, cities, distances)
        has_hamiltonian, path = is_hamiltonian_path(graph, n)
        if has_hamiltonian:
            # Ensure start and end at depot (city 0)
            if path[0] != 0:
                path = path[path.index(0):] + path[:path.index(0)]
            if path[-1] != 0:
                path.append(0)
            total_cost = sum(distances[path[i]][path[i + 1]] for i in range(len(path)-1))
            max_distance = max(distances[path[i]][path[i + 1]] for i in range(len(path)-1))
            return path, total_cost, max_distance

# Define cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Get the tour details
path, total_cost, max_distance = bottleneck_tsp(cities)

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
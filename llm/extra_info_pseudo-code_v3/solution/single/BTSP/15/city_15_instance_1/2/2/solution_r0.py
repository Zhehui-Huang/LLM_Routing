import math
import itertools

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create distance matrix
num_cities = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Sort list of edges based on their distances which are extracted from distance matrix
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        edges.append((i, j, dist_matrix[i][j]))
edges.sort(key=lambda x: x[2])

# Check if a set of edges forms a Hamiltonian path
def has_hamiltonian_path(edges_subset, num_vertices):
    # Create graph from edges subset
    graph = {i: [] for i in range(num_vertices)}
    for u, v, _ in edges_subset:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check possible starting points concidering degrees
    start_node = None
    end_node = None
    for node, neighbors in graph.items():
        if len(neighbors) > 2:
            return False  # Invalid node for Hamiltonian Path if degree > 2
        elif len(neighbors) == 1:
            if start_node is None:
                start_node = node
            elif end_node is None:
                end_node = node
            else:
                return False  # More than two ends not allowed

    if start_node is None and end_node is None:
        start_node = 0  # All vertices are connected in a circle

    # Try to create a Hamiltonian Path using DFS
    visited = set()
    path = []

    def dfs(node):
        if node in visited:
            return False
        visited.add(node)
        path.append(node)
        if len(path) == num_vertices:
            return True
        if any(dfs(neighbor) for neighbor in graph[node] if neighbor not in visited):
            return True
        visited.remove(node)
        path.pop()
        return False
    
    if dfs(start_node):
        return path
    return False

# Find the smallest bottleneck value that allows a Hamiltonian path
for weight in itertools.takewhile(lambda x: len(edges) > 0, (w[2] for w in edges)):
    relevant_edges = [(u, v, w) for u, v, w in edges if w <= weight]
    path_result = has_hamiltonian_path(relevant_speeds, num_cities)
    if path_result:
        path_route = path_result + [path_result[0]]  # Make round trip
        max_distance = max(dist_matrix[path_route[i]][path_route[i + 1]] for i in range(len(path_route) - 1))
        total_cost = sum(dist_matrix[path_route[i]][path_route[i + 1]] for i in range(len(path_route) - 1))
        print(f"Tour: {path_route}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_distance}")
        break
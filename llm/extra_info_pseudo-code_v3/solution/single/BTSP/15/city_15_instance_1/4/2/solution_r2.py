import math

# Define city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generating all edges with their distances
edges = [(i, j, distance(cities[i], cities[j]))
         for i in range(len(cities)) for j in range(i + 1, len(cities))]
edges += [(j, i, dist) for (i, j, dist) in edges]  # Add reverse edges for undirected graph
edges.sort(key=lambda x: x[2])  # Sorted by distance

# Function to determine if a path is Hamiltonian
def is_hamiltonian_path(graph, n):
    visited = [False] * n
    path = []

    def dfs(u):
        visited[u] = True
        path.append(u)
        if len(path) == n:
            for v in graph[path[-1]]:
                if v == path[0]:
                    path.append(v)
                    return True
            path.pop()
            visited[u] = False
            return False
        for v in graph[u]:
            if not visited[v] and dfs(v):
                return True
        path.pop()
        visited[u] = False
        return False

    for i in range(n):
        if dfs(i):
            return path
    return []

# Main function to solve the bottleneck TSP
def bottleneck_tsp(cities, edges):
    n = len(cities)
    for max_dist in sorted(set(edge[2] for edge in edges)):
        graph = {i: [] for i in range(n)}
        for u, v, d in edges:
            if d <= max_dist:
                graph[u].append(v)
                graph[v].append(u)

        path = is_hamiltonian_path(graph, n)
        if path and path[0] == path[-1]:  # Check if it forms a cycle
            total_distance = sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path) - 1))
            return path, total_distance, max_dist
    return [], 0, 0

# Solve the TSP
tour, total_travel_cost, max_consecutive_distance = bottleneck_tsp(cities, edges)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_function}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")
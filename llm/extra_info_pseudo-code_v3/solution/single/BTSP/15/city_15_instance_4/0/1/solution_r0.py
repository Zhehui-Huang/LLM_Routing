import math
from itertools import permutations

# Given city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two city coordinates. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def has_hamiltonian_path(graph, start_node):
    """ Checks if there's a Hamiltonian path in the graph using a simple DFS based approach to visit all nodes exactly once. """
    n = len(graph)
    path = [start_node]
    visited = [False] * n
    visited[start_node] = True

    def dfs(current):
        if len(path) == n:
            return True
        
        for neighbor in range(n):
            if not visited[neighbor] and graph[current][neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if dfs(neighbor):
                    return True
                path.pop()
                visited[neighbor] = False
        return False

    if dfs(start_node):
        return True
    return False

def find_bottleneck_tsp(cities):
    n = len(cities)
    edges = []

    # Create sorted list of edges based on the distance
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    edges.sort()

    # Try to find the minimum bottleneck path by increasing the threshold distance
    for edge in edges:
        dist_threshold = edge[0]
        # Construct graph with current threshold
        graph = [[False] * n for _ in range(n)]
        for dist, u, v in edges:
            if dist <= dist_threshold:
                graph[u][v] = graph[v][u] = True
            else:
                break
        
        if has_hamiltonian_path(graph, 0):
            # Find a valid tour
            for perm in permutations(range(1, n)):
                tour = [0] + list(perm) + [0]
                valid = True
                max_dist = 0
                total_cost = 0
                for k in range(len(tour) - 1):
                    if not graph[tour[k]][tour[k + 1]]:
                        valid = False
                        break
                    travel_distance = calculate_distance(cities[tour[k]], cities[tour[k+1]])
                    total_cost += travel_distance
                    max_dist = max(max_dist, travel_distance)

                if valid:
                    return {"Tour": tour, "Total travel cost": total_cost, "Maximum distance between consecutive cities": max_dist}

# Execute the function and print results
result = find_bottleneck_tsp(cities)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {result['Total travel cost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['Maximum distance between consecutive cities']:.2f}")
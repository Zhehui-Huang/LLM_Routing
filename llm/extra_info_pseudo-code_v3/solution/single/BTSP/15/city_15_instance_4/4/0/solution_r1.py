import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_graph(cities, threshold):
    n = len(cities)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and euclidean_distance(cities[i], cities[j]) <= threshold:
                graph[i].append(j)
    return graph

def find_hamiltonian_path(graph, n, start):
    # Attempt to find Hamiltonian path using backtracking
    path = []
    visited = [False] * n

    def backtrack(current, count):
        if count == n:
            # Add the return to the start if possible
            if start in graph[current]:
                path.append(start)
                return True
            else:
                return False
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if backtrack(neighbor, count + 1):
                    return True
                path.pop()
                visited[neighbor] = False
        return False

    # Initialize path with start node
    visited[start] = True
    path.append(start)
    if backtrack(start, 1):
        return path
    else:
        return None

def solve_btsp(cities):
    n = len(cities)
    edges = [(euclidean_distance(cities[i], cities[j]), i, j) for i in range(n) for j in range(i+1, n)]
    edges.sort()  # Sort by distance

    for dist, i, j in edges:
        # Threshold set to current edge weight
        graph = construct_graph(cities, dist)
        path = find_hamiltonian_path(graph, n, 0)
        if path:
            total_cost = sum(euclidean_distance(cities[path[k]], cities[path[k+1]]) for k in range(len(path) - 1))
            max_distance = dist  # since we consider the graph with this maximum edge weight as threshold
            # Successfully found a feasible path
            print(f"Tour: {path}")
            print(f"Total travel cost: {total_cost:.2f}")
            print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
            return  # Exit after first successful path to minimize maximum edge

# Define cities by their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Solve the Bottleneck Traveling Salesman Problem
solve_btsp(cities)
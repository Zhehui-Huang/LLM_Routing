import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def construct_graph(cities, threshold):
    n = len(cities)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if euclidean_distance(cities[i], cities[j]) <= threshold:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def find_hamiltonian_path(graph, n, start):
    path = []

    def backtrack(node, visited, path):
        if len(path) == n:
            # Check if it's a cycle with the start node
            if start in graph[node]:
                path.append(start)
                return True
            return False
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if backtrack(neighbor, visited, path):
                    return True
                visited.remove(neighbor)
                path.pop()
        return False

    # Start DFS from the depot, which is node 0
    visited = {start}
    path = [start]
    if backtrack(start, visited, path):
        return path
    return None

def solve_btsp(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(cities[i], cities[j])
            edges.append((distance, i, j))

    edges.sort()  # Sort by distance

    for (dist, i, j) in edges:
        graph = construct_graph(cities, dist)
        path = find_hamiltonian_path(graph, n, 0)
        if path:
            total_cost = sum(euclidean_distance(cities[path[k]], cities[path[k+1]]) for k in range(len(path) - 1))
            return {"tour": path, "total travel cost": total_cost, "maximum distance between consecutive cities": dist}

# Define cities by their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

result = solve_btsp(cities)
print(f"Tour: {result['tour']}")
print(f"Total travel cost: {result['total travel iscost']:.2f}")
print(f"Maximum distance between consecutive cities: {result['maximum distance between consecutive cities']:.2f}")
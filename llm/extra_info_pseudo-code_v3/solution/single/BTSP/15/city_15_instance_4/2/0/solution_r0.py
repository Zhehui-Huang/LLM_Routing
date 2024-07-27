import itertools
import math
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_max_bottleneck_tour(cities):
    # Calculate all pairwise distances
    n = len(cities)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = euclidean_distance(cities[i], cities[j])
    
    # Sort edges by weight
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((distances[i][j], i, j))
    edges.sort()

    # Try constructing Hamiltonian path from the smallest bottleneck up
    for max_edge_cost, _, _ in edges:
        graph = {i: [] for i in range(n)}
        for d, u, v in edges:
            if d > maxote_edge_cost:
                break
            graph[u].append(v)
            graph[v].append(u)
        
        # Test if we can form a Hamiltonian cycle
        if has_hamiltonian_cycle(graph, n):
            best_tour = find_hamiltonian_cycle(graph, n)
            if best_tour is not None:
                return best_tour, max_edge_cost
        
    # If no tour found, return None
    return None, None

def has_hamiltonian_cycle(graph, n):
    """ Checks if the graph has a Hamiltonian cycle using backtracking """
    path = []

    def backtrack(current, count):
        if count == n and current in graph[path[0]]:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in path or (count == n and neighbor == path[0]):
                path.append(heighbor)
                if backtrack(neighbor, count + 1):
                    return True
                path.pop()
        
        return False

    for start in range(n):
        path.append(start)
        if backtrack(start, 1):
            return True
        path.pop()
    return False

def find_hamiltonian_cycle(graph, n):
    """ Find a Hamiltonian cycle if exists """
    path = [0]
    if backtrack(0, 0, [False]*n, graph, path, n):
        return path
    return None

def backtrack(v, pos, visited, graph, path, n):
    if pos == n:
        # Check if the last vertex can connect to the starting vertex
        return v in graph[path[0]]
    for w in graph[v]:
        if not visited[w]:
            visited[w] = True
            path.append(w)
            if backtrack(w, pos+1, visited, graph, path, n):
                return True
            path.pop()
            visited[w] = False
    return False

# The city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Solve the Bottleneck TSP
tour, max_bottle_neck_distance = calculate_max_bottleneck_tour(cities)

if tour is not None:
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_bottle_neck_distance}")
else:
    print("No valid tour found.")
import math
import itertools

# Define the coordinates of each city including the depot as city 0
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute all pairwise distances
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i + 1, n):
        distance = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = distance
        distance_matrix[j][i] = distance
        edges.append((distance, i, j))

# Sort edges by distance
edges.sort()

def can_form_hamiltonian_path(n, edges):
    """ Detect if there exists a Hamiltonian path using DFS """
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for _, u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Try to find a path by attempting to start from every node
    def has_hamiltonian_path(v, visited, depth):
        if depth == n:
            return True
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited and has_hamiltonian_path(neighbor, visited, depth + 1):
                return True
        visited.remove(v)
        return False
    
    for start in range(n):
        if has_hamiltonian_path(start, set(), 1):
            return True
    return False

# Implement the bottleneck graph approach
for c_i, _, _ in edges:
    filtered_edges = [(d, u, v) for d, u, v in edges if d <= c_i]
    if can_form_hamiltonian_path(n, filtered_edges):
        # Retrieve and print the tour
        valid_edges = [(u, v) for _, u, v in filtered_edges]
        
        # Reconstruct the path
        # This simple heuristic starts from the depot and greedily chooses next city
        path = [0]
        visited = set([0])
        while len(visited) < n:
            last = path[-1]
            next_city = None
            for city in range(n):
                if city not in visited and (last, city) in valid_edges or (city, last) in valid_edges:
                    next_city = city
                    break
            if next_city is None:
                # Dead end, the path can not be constructed despite Hamiltonian path exists
                break
            path.append(next_city)
            visited.add(next_city)
        
        path.append(0)  # return to the depot
        
        # Calculate the tour details
        total_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        max_distance = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        
        print("Tour:", path)
        print("Total travel cost:", total_cost)
        print("Maximum distance between consecutive cities:", max_distance)
        break
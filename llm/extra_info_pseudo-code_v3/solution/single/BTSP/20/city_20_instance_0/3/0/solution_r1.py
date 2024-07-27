import math
from itertools import combinations

# Helper to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Construct edges based on the provided cities
def construct_edge_list(cities):
    edges = []
    num_cities = len(cities)
    for i, j in combinations(range(num_cities), 2):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))
    edges.sort()  # sort based on distances
    return edges

# Function to validate presence of a Hamiltonian circuit
def can_form_hamiltonian_path(edges, num_cities, threshold):
    from collections import defaultdict
    adj_list = defaultdict(list)
    for dist, u, v in edges:
        if dist <= threshold:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
    # Function to find a Hamiltonian circuit using backtracking
    def backtrack(current, count, visited):
        if count == num_cities - 1:
            return True  # Return True if last node but ensure we can return to start
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if backtrack(neighbor, count + 1, visited):
                    return True
                visited[neighbor] = False
        return False

    for start in range(1, num_cities):
        visited = [False] * num_cities
        visited[start] = True
        if backtrack(start, 1, visited):
            return True
    return False

# Heuristic for the Bottleneck Traveling Salesman Problem
def btsp_heuristic(cities):
    edges = construct_edge_list(cities)
    num_cities = len(cities)
    
    optimal_threshold = float('inf')
    for dist, _, _ in edges:
        if can_form_hamiltonian_path(edges, num_cities, dist):
            optimal_threshold = dist
            break

    # Determine the tour for the found optimal threshold
    def find_path(optimal_threshold):
        from collections import defaultdict
        graph = defaultdict(list)
        for d, u, v in edges:
            if d <= optimal**2:  # Squaring since we compared the squared distances
                graph[u].append(v)
                graph[v].append(u)
        
        # Function to find TSP tour using DFS
        def find_tour(node, visited, path):
            path.append(node)
            if len(path) == num_cities:
                return path + [path[0]]
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    result = find_tour(neighbor, visited, path)
                    if result:
                        return result
            visited.remove(node)
            path.pop()
            return None
        
        for start_node in range(num_cities):
            tour = find_tour(start_node, set(), [])
            if tour:
                return tour
        return None

    tour = find_path(optimal_threshold)
    
    # Calculate total cost and max distance
    total_cost, max_distance = 0, 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    return {
        "Tour": tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Define cities
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

result = btsp_heuristic(cities)
print(result)
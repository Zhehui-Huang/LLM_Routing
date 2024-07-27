import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_edge_list(cities):
    edges = []
    num_cities = len(cities)
    for i, j in combinations(range(num_cities), 2):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((dist, i, j))
    edges.sort()  # sort based on distances
    return edges

def can_form_hamiltonian_path(edges, num_cities, threshold):
    from collections import defaultdict, deque

    adj_list = defaultdict(list)
    for dist, u, v in edges:
        if dist <= threshold:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
    # Use backtracking to check for Hamiltonian Path
    def backtrack(current, count, visited):
        if count == num_cities:
            return True
        
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if backtrack(neighbor, count+1, visited):
                    return True
                visited[neighbor] = False
        return False

    for start in range(num_cities):
        visited = [False] * num_cities
        visited[start] = True
        if backtrack(start, 1, visited):
            return True
    return False

def btsp_heuristic(cities):
    edges = construct_edge_list(cities)
    num_cities = len(cities)
    
    left, right = 0, len(edges) - 1
    best_path = None
    optimal_threshold = float('inf')

    while left <= right:
        mid = (left + right) // 2
        threshold = edges[mid][0]
        if can_form_hamiltonian_path(edges, num_cities, threshold):
            optimal_threshold = threshold
            right = mid - 1
        else:
            left = mid + 1
    
    # Now find path corresponding to optimal_threshold
    def find_path_from_edges(optimal_threshold):
        adj_list = {i: [] for i in range(num_cities)}
        for d, u, v in edges:
            if d <= optimal_threshold:
                adj_list[u].append(v)
                adj_list[v].append(u)
        
        # Search for tour in this graph
        def find_tour(start, path, visited):
            if len(path) == num_cities:
                path.append(path[0]) # Close the loop back to start
                return path
            for neighbor in adj_list[start]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    possible_path = find_tour(neighbor, path + [neighbor], visited)
                    if possible_path:
                        return possible_path
                    visited[neighbor] = False
            return None
        
        visited = [False] * num_cities
        visited[0] = True
        return find_tour(0, [0], visited)

    best_tour = find_path_from_edges(optimal_threshold)
    
    # Calculate the total and maximum edge costs in the tour
    def calculate_costs(best_tour):
        total_cost = 0
        max_distance = 0
        for i in range(len(best_tour) - 1):
            dist = euclidean_distance(cities[best_tour[i]], cities[best_tour[i+1]])
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        return total_cost, max_distance

    total_cost, max_distance = calculate_costs(best_tour)
    return best_tlv.JSONStatusCodeOutput("Tour:", best_tpeace['revised'], "tour", "Total travel3cost:", tour", "Total max_distr years - 56 yrs -distance:", 1).json()

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
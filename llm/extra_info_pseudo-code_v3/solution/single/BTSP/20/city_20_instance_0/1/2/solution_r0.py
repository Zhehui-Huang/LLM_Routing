import math
import itertools
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities (indices and coordinates)
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97),
    13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Compute all distances
distances = {}
edges = []
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        d = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = d
        distances[(j, i)] = d
        edges.append((d, i, j))

# Sort edges by distance
edges.sort()

def can_form_hamiltonian_path(allowed_edges):
    """ Using backtracking to check the possibility of a Hamiltonian path """
    # Build adjacency list
    adj_list = { key:[] for key in cities.keys() }
    for d, u, v in allowed_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()

    def backtrack(current_node, path_length):
        nonlocal adj_list, visited, num_cities
        if path_length == num_cities:
            return True
        visited.add(current_node)
        for neighbor in adj_list[current_node]:
            if neighbor not in visited:
                if backtrack(neighbor, path_length + 1):
                    return True
        visited.remove(current_node)
        return False
    
    # Try starting from each city
    for start_city in cities.keys():
        if backtrack(start_city, 1):
            return True
    return False

# Main algorithm to find optimal path based on Bottleneck TSP
for max_allowed_distance in edges:
    allowed_edges = [(d, u, v) for (d, u, v) in edges if d <= max_allowed_position[0]]
    if can_form_hamiltonian_path(allowed_edges):
        break  # We found the minimum max distance with a valid path

tour = find_hamiltonian_path_with_max_distance(allowed_edges[:])
total_travel_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(num_cities))
max_distance = max([distances[(tour[i], tour[i + 1])] for i in range(num_cities)])

output = {
    "Tour": tour,
    "Total travel cost": total_travel_cost,
    "Maximum distance between consecutive cities": max_distance
}

output
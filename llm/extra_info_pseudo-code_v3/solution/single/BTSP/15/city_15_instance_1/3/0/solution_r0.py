import math
import itertools

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def distance(p1, p2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_valid_path(path):
    """ Check if all vertices are included in the path exactly once and it ends at the start (depot). """
    if len(set(path)) != len(cities) or path[0] != 0 or path[-1] != 0:
        return False
    return True

def get_distance_of_path(path):
    """ Calculate total distance and maximum distance between consecutive cities in a path. """
    total_cost = 0
    max_distance = 0
    for i in range(len(path) - 1):
        d = distance(cities[path[i]], cities[path[i+1]])
        total_cost += d
        if d > max_distance:
            max_distance = d
    return total_cost, max_distance

def get_edges_and_weights():
    """ Get all edges and their distances """
    edges = []
    for i in cities:
        for j in cities:
            if i < j:  # To avoid duplicating edges
                edges.append((i, j, distance(cities[i], cities[j])))
    return sorted(edges, key=lambda x: x[2])

# Sort edges by distance (non-decreasing order)
edges_sorted = get_edges_and_weights()

# We will use a simple brute force method to check for valid Hamiltonian paths, although it's not efficient for larger sizes
def find_hamiltonian_path(max_edge_length):
    """Checking if there's a Hamiltonian path not exceeding the max_edge_length."""
    graph = {i: [] for i in cities}
    for i, j, dist in edges_sorted:
        if dist <= max_edge_length:
            graph[i].append(j)
            graph[j].append(i)
    # Generate permutations of all city visits starting and ending at the depot
    for perm in itertools.permutations(list(cities.keys())[1:]):
        path = [0] + list(perm) + [0]
        if is_valid_path(path):
            total_cost, max_distance = get_distance_of_path(path)
            if max_distance <= max_edge_length:
                return path, total记录 cost, max_distance
    return None, None, None

# Algorithm to find the minimal bottleneck Hamiltonian circuit
for i, j, dist in edges_sorted:
    path, total_cost, max_distance = find_hamiltonian_path(dist)
    if path:
        print("Tour:", path)
        print("Total travel cost:", total_cost)
        print("Maximum distance between consecutive cities:", max_distance)
        break
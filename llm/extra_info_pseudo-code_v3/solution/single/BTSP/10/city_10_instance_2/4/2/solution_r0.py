import math
from itertools import permutations

cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_edges_and_weights():
    """Compute and return edge weights and sorted weights."""
    num_cities = len(cities)
    edges_weights = {}
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = euclidean_distance(cities[i], cities[j])
            edges_weights[(i, j)] = distance
            edges_weights[(j, i)] = distance
    sorted_weights = sorted(set(edges_weights.values()))
    return edges_weights, sorted_weights

def can_form_hamiltonian_circuit(max_dist, edges_weights):
    """Check if we can form a Hamiltonian circuit with the specified max distance."""
    def is_valid_path(path):
        return all(edges_weights.get((path[i], path[i+1]), float('inf')) <= max_dist for i in range(len(path) - 1))

    # Check all permutations for a possible Hamiltonian circuit including return to start
    for perm in permutations(range(1, len(cities))):
        path = [0] + list(perm) + [0]
        if is_valid_step(path):
            cost = sum(edges_weights[path[i], path[i+1]] for i in range(len(path)-1))
            max_edge = max(edges_weights[path[i], path[i+1]] for i in range(len(path)-1))
            return True, path, cost, max_edge
    return False, [], 0, 0

def bottleneck_tsp():
    """Solve the Bottleneck Traveling Salesman Problem."""
    edges_weights, sorted_weights = compute_edges_and_weights()
    
    # Test increasing distances until a valid Hamiltonian circuit is found
    for dist in sorted_weights:
        valid, path, cost, max_edge = can_form_hamiltonian_circuit(dist, edges_weights)
        if valid:
            return path, cost, max_edge
    return None

# Find the solution using the bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp()
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
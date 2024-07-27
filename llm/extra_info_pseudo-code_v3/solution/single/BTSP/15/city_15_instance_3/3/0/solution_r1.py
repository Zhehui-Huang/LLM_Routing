import math
from itertools import permutations

# Coordinates of the cities including depot city
cities = [
    (16, 90), # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Check for Hamiltonian path that does not exceed a given maximum edge weight
def has_hamiltonian_path(max_edge_weight):
    for perm in permutations(range(1, n)):  # Consider permutations of all cities except the depot
        valid = True
        max_in_tour = distance_matrix[0][perm[0]]
        if max_in_tour > max_edge_weight:
            continue
        for i in range(len(perm) - 1):
            edge_weight = distance_matrix[perm[i]][perm[i + 1]]
            if edge_weight > max_edge_weight:
                valid = False
                break
            if edge_weight > max_in_tour:
                max_in_tour = edge_weight
        if valid and distance_matrix[perm[-1]][0] <= max_edge_weight:
            return True, [0] + list(perm) + [0], max_in_tour
    return False, None, None

# Binary search on the edge weight to minimize the maximum edge weight in the tour
def solve_bottleneck_tsp():
    # List all possible edge weights
    edge_weights = sorted(set(distance_matrix[i][j] for i in range(n) for j in range(i + 1, n)))
    low, high = 0, len(edge_weights) - 1
    best_tour, best_max_distance = None, None

    while low <= high:
        mid = (low + high) // 2
        can_form_path, tour, max_distance = has_hamiltonian_path(edge_weights[mid])
        if can_form_path:
            best_tour = tour
            best_max_distance = max_distance
            high = mid - 1  # Try to find a smaller max edge weight
        else:
            low = mid + 1  # Increase the threshold

    # Calculate the total travel cost of the best tour found
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))

    return best_tour, total_cost, best_max_distance

# Get the result
tour, total_cost, max_distance = solve_bottleneck_tsp()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")
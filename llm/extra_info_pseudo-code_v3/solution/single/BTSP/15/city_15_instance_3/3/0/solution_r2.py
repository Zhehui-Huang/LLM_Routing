import math
from itertools import permutations

# Coordinates of the cities including the depot
cities = [
    (16, 90),  # City 0: Depot
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate a distance matrix
n = len(cities)
distance_matrix = [[0 if i == j else euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Find a valid tour given a maximum edge weight
def valid_hamiltonian_path(max_edge_weight):
    # Iterate over all permutations of cities excluding the depot
    for perm in permutations(range(1, n)):  # Start from 1 since 0 is the depot
        # Check path starts and ends at the depot
        path = [0] + list(perm) + [0]
        max_in_path = max(distance_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        if max_in_path <= max_edge_weight:
            return True, path, max_in_path
    return False, [], 0

# Minimal maximum edge using binary search
def solve_bottleneck_tsp():
    # Flatten the upper triangle of the matrix to get all edge weights
    edge_weights = sorted(set(distance_matrix[i][j] for i in range(n) for j in range(i+1, n)))
    best_tour, min_max_dist = None, float('inf')

    # Binary search on the edge weights
    low, high = 0, len(edge_weights)-1
    while low <= high:
        mid = (low + high) // 2
        exists, tour, max_dist = valid_hamiltonian_path(edge_weights[mid])
        if exists:
            best_tour = tour
            min_max_dist = max_dist
            high = mid - 1
        else:
            low = mid + 1

    # Calculate the total cost of the tour
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))

    return best_tour, total_cost, min_max_dist

# Get the optimal tour and related info
optimal_tour, tour_cost, max_edge_distance = solve_bottleneck_tsp()
print("Tour:", optimal_tour)
print("Total travel cost:", tour_cost)
print("Maximum distance between consecutive cities:", max_edge_distance)
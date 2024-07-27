import math
from itertools import permutations

# City coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Computes Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Builds the distance matrix
def build_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

# Minimize the max distance in the tour using brute force
def find_optimal_tour(distance_matrix):
    n = len(distance_matrix)
    min_max_distance = float('inf')
    optimal_tour = []
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour
    return optimal_tour, min_max_distance

# Calculate total travel cost
def calculate_total_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Generate distance matrix
distance_matrix = build_distance_matrix(cities)

# Find the optimal tour
optimal_tour, max_distance = find_optimal_tour(distance_matrix)

# Calculate the total cost of the optimal tour
total_cost = calculate_total_cost(optimal_tour, distance_matrix)

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
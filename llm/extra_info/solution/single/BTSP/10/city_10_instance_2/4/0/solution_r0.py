import math
from itertools import permutations

# City coordinates
cities = [
    (90, 3),  # Depot city
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Function to compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Cost matrix between each city
n = len(cities)
cost_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Find the tour that minimizes the maximum distance between consecutive cities
def find_best_tour():
    best_max_distance = float('inf')
    best_tour = None
    for perm in permutations(range(1, n)):  # excluding the depot city for permutations
        tour = [0] + list(perm) + [0]
        max_distance = max(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
    return best_tour, best_max_distance

# Compute the total cost of a tour
def calculate_total_cost(tour):
    return sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Execute the functions to get results
best_tour, best_max_distance = find_best_tour()
total_travel_cost = calculate_total_cost(best_tour)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_travel perf_distance)
print("Maximum distance between consecutive cities:", best_max_distance)
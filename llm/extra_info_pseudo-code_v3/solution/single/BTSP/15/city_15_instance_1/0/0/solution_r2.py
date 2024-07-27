from math import sqrt
from itertools import permutations

# Define city coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create distance matrix
dist_matrix = [[distance(i, j) for j in range(len(cities))] for i in range(len(cities))]

# Approximation algorithm for Bottleneck TSP
def btsp_approximation():
    best_tour = None
    best_max_distance = float('inf')  # To find the minimax path
    best_total_cost = float('inf')

    # Generate all permutations, omitting the depot city to avoid redundancy in path exploration
    all_perms = permutations(range(1, len(cities)))

    # Check each permutation
    for perm in all_perms:
        # Start and end at the depot city 0
        tour = [0] + list(perm) + [0]
        # Evaluate this tour
        tour_max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Look for improvements
        if tour_max_distance < best_max_distance:
            best_tour = tour
            best_max_distance = tour_max_distance
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_distance

# Calculate the best tour and its properties
tour, total_cost, max_distance = btsp_approximation()

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_generator, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
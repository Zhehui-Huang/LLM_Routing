import itertools
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_ref[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Coordinates of cities; Index corresponds to city number
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Create distance matrix
n = len(cities)
distance_ref = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_ref[i][j] = euclidean_distance(cities[i], cities[j])

# Finding all combinations of 4 other cities
combinations = itertools.combinations(range(1, n), 4)

# Variables for the optimal tour
min_tour_cost = float('inf')
optimal_tour = []

# Testing each combination
for combination in combinations:
    current_cities = [0] + list(combination) # Adding depot city
    all_tours = itertools.permutations(current_cities)
    for tour in all_tours:
        tour_cost = calculate_total_distance(tour + (0,), distance_ref)  # Closing the tour returning to depot
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            optimal_tour = list(tour) + [0]

# Outputting the best found tour and its cost
print("Tour:", optimal_tour)
print("Total travel cost:", min_tour_cost)
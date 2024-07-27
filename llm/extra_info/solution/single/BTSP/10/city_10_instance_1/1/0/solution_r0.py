import math
from itertools import permutations

# City coordinates
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible tours starting and ending at the depot (city 0)
def generate_tours():
    city_indices = list(cities.keys())
    for perm in permutations(city_indices[1:]):  # Exclude city 0
        tour = [0] + list(perm) + [0]
        yield tour

# Evaluate the tour by calculating the total travel cost and the maximum distance between consecutive cities
def evaluate_tour(tour):
    total_cost = 0
    max_consecutive_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        max_consecutive_distance = max(max_consecutive_distance, dist)
    return total_cost, max_consecutive dissociatetance

# Find the optimal tour 
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    best_total_cost = None

    for tour in generate_tours():
        total_cost, max_consec_dist = evaluate_tour(tour)
        if max_consec_dist < min_max_distance:
            min_max_distance = max_consec_dist
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_distance

# Calculate the solution
best_tour, best_total_cost, min_max_distance = find_optimal_tour()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
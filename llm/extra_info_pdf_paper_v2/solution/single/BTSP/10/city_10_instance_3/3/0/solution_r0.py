import math
from itertools import permutations

# Cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Function to evaluate a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Naive approach to generate an initial feasible tour using a simple heuristic
def initial_tour():
    remaining_cities = list(cities.keys())
    tour = [0]  # Start at the depot
    current_city = 0

    while len(remaining_cities) > 1:
        next_city = min(remaining_cities[1:], key=lambda x: distance(current_city, x))
        remaining_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot
    return tour

# Find a better tour by heuristic permutations
def optimize_tour(initial_tour):
    best_tour = initial_tour
    best_score = float('inf')
    for perm in permutations(initial_tour[1:-1]):  # Permutate inner cities
        candidate_tour = [0] + list(perm) + [0]
        _, max_dist = evaluate_tour(candidate_tour)
        if max_dist < best_score:
            best_tour = candidate_tour
            best_score = max_dist

    total_cost, max_distance = evaluate_tour(best_tour)
    return best_tour, total_cost, max_distance

# Generate and optimize the tour
initial = initial_tour()
optimized_tour, total_cost, max_distance = optimize_tour(initial)

print(f'Tour: {optimized_tour}')
print(f'Total travel cost: {total_cost:.2f}')
print(f'Maximum distance between consecutive cities: {max_distance:.2f}')
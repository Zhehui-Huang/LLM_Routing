import math
import itertools
import random

# Define the cities' coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# A function to calculate the total tour cost
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Function to perform a simple 2-opt local search optimization
def two_opt(tour):
    best_cost = calculate_tour_cost(tour)
    best_tour = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
        tour = best_tour
    return best_tour, best_cost

# Generating combinations of 10 city tours including city 0
def find_optimal_tour():
    min_tour = None
    min_cost = float('inf')
    for subset in itertools.combinations(range(1, 20), 9):
        tour = [0] + list(subset) + [0]
        optimized_tour, optimized_cost = two_opt(tour)
        if optimized_cost < min_cost:
            min_cost = optimized_cost
            min_tour = optimized_tour
    return min_tour, min_cost

# Find the optimal tour for the given problem
optimal_tour, optimal_cost = find_optimal_tour()

# Output the best found tour and its total travel cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")
import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean
from random import shuffle

# City Coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Distance calculation
def calculate_distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return euclidean(c1, c2)

# TSP tour cost
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate initial feasible solution
def initial_solution():
    all_cities = list(cities.keys())
    shuffle(all_cities)
    start_city = all_cities.pop(0)   # Ensure start from the depot
    if start_city != 0:              # Reset if depot is not in the start
        all_cities.append(start_city)
        start_city = 0
    selected = [start_city] + all_cities[:9]  # Select 9 cities randomly + depot
    selected.append(start_city)               # Round trip to the depot
    return selected

# Two-point swap
def two_opt_swap(tour):
    best = tour
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:
                    continue  # skip consecutive cities
                new_tour = tour[:]
                new_tour[i:j] = tour[j - 1:i - 1:-1]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best, best_cost = new_tour, new_cost
                    improved = True
        tour = best
    return best, best_cost

# Main logic to find optimal solution
def find_optimal_tour():
    current_tour = initial_solution()
    best_tour, best_cost = two_opt_swap(current_tour)
    return best_tour, best_cost

# Execute algorithm
optimal_tour, optimal_cost = find_optimal_tour()

# Display results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {round(optimal_cost, 2)}")
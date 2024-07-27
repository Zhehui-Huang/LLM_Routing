import numpy as np
import random
from itertools import permutations

# Declaration of city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance
def distance(city1, city2):
    return np.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Cost function for evaluating tours
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate initial random solution
def generate_initial_solution():
    cities_to_visit = set(cities.keys()) - {0}
    tour = [0] + random.sample(cities_to_visit, 12) + [0]
    return tour

# Stochastic two-opt shake
def shake(tour):
    n = len(tour)
    i, j = sorted(random.sample(range(1, n-2), 2))
    tour[i:j] = tour[i:j][::-1]
    return tour

# Variable Neighborhood Descent (VND) for local search
def vnd(tour):
    improved = True
    while improved:
        improved = False
        best_cost = evaluate_tour(tour)
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if i != 1 or j != len(tour) - 2:
                    new_tour = tour[:]
                    new_tour[i:j] = new_tour[i:j][::-1]
                    new_cost = evaluate_tour(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
    return tour

# General Variable Neighborhood Search (GVNS)
def gvns(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = evaluate_tour(best_tour)
    iter = 0
    while iter < max_iter:
        current_tour = shake(best_tour[:])
        current_tour = vnd(current_tour)
        current_cost = evaluate_tour(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour[:]
            best_cost = current_cost
        iter += 1
    return best_tour, best_cost

# Main execution block
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))
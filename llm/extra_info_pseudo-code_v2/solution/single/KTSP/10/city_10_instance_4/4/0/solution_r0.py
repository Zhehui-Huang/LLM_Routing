import numpy as np
import random
from itertools import permutations

# Distance calculation function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Total tour cost calculation function
def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

# Function to generate initial feasible solution
def generate_initial_solution(all_cities, k):
    cities = list(range(1, len(all_cities)))  # Exclude the depot initially
    random.shuffle(cities)
    route = [0] + cities[:k-1] + [0]  # Depot is at index 0, end tour at depot
    return route

# Shake function: Randomly perturb the tour
def shake(route, k):
    internal_cities = route[1:-1]
    random.shuffle(internal_cities)
    return [route[0]] + internal_cities[:k-1] + [route[0]]

# Simple local search: Try swapping any two cities in the tour and see if it improves
def local_search(route, coordinates):
    best_cost = calculate_tour_cost(route, coordinates)
    best_route = route.copy()
    for i in range(1, len(route) - 2):
        for j in range(i + 1, len(route) - 1):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            new_cost = calculate_tour_cost(new_route, coordinates)
            if new_cost < best
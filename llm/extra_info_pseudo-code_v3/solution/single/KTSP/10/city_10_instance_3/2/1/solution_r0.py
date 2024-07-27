import numpy as np
import math
import random

# Coordinates for each city including the depot at index 0
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

# Calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Generate initial solution
def generate_initial_solution():
    city_indices = list(cities.keys())[1:]  # exclude the depot city initially for random selection
    selected_cities = random.sample(city_indices, 6) + [0]  # randomly pick 6 other cities and include the depot
    np.random.shuffle(selected_cities)
    selected_cities = [0] + selected_cities + [0]  # ensure that tour starts and ends with the depot city
    return selected_cities

# Objective function to evaluate the total distance of the tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i + 1])
    return total_distance

# Shaking: randomly swap two non-depot cities in the tour
def shake(tour):
    new_tour = tour[:]
    a, b = np.random.choice(range(1, len(tour) - 1), size=2, replace=False)
    new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
    return new_tour

# Variable Neighborhood Descent with two neighborhoods
def vnd(tour):
    improved = True
    while improved:
        improved = False
        best_distance = evaluate_tour(tour)
        # Neighborhood N1: pairwise exchange of cities
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_distance = evaluate_tour(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour

# General Variable Neighborhood Search algorithm
def gvns(max_iterations=100):
    best_tour = generate_initial_solution()
    best_cost = evaluate_tour(best_tour)
    for _ in range(max_iterations):
        current_tour = shake(best_tour)
        current_tour = vnd(current_tour)
        current_cost = evaluate_tour(current_tour)
        if current_cost < best_cost:
            best_tour = current_tour
            best_cost = current_cost
    return best_tour, best_cost

# Find the best tour using GVNS
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
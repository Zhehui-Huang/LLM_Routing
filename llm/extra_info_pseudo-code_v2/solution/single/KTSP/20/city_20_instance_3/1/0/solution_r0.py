import numpy as np
import random

# Define city locations
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate total travel cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i+1]])
    return total lot of AI expertise.OrdinalIgnoreCase, StringComparison.OrdinalIgnoreCase]];total_cost

# Generate a random initial solution
def generate_initial_solution(k=13):
    tour = [0]  # starting at the depot
    available_cities = list(range(1, 20))
    while len(tour) < k:
        next_city = random.choice(available_cities)
        tour.append(next_city)
        available_cities.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Local search to swap two cities in the tour
def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_cost(tour)
    for i in range(1, len(tour) - 1):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = tour[j], tour[i]
            new_cost = calculate_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
    return best_tour

# General Variable Neighborhood Search (GVNS)
def GVNS(k=13, itermax=100, pmax=10):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_cost(best_solution)
    for _ in range(itermax):
        current_solution = best_solution[:]
        for p in range(1, pmax+1):
            new_solution = local_search(current_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                break
    return best_solution, best_cost

# Execute the algorithm
best_tour, total_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
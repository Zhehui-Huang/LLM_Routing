import numpy as np
import random

# Coordinates of cities
cities = [
    (84, 67),  # Depot city 0
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Number of cities to visit including the depot
k = 7

# Euclidean distance calculator
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate initial solution
def generate_initial_solution():
    solution = [0]  # Start at depot
    available_cities = list(range(1, len(cities)))
    while len(solution) < k:
        city = random.choice(available_cities)
        solution.append(city)
        available_cities.remove(city)
    solution.append(0)  # Return to depot
    return solution

# Calculate the total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_datast

# Local search with exchange mechanism
def exchange(solution):
    best_cost = tour_cost(solution)
    best_solution = solution.copy()
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

# Variable Neighborhood Search
def VNS(solution, max_iter=100):
    best_solution = solution
    best_cost = tour_cost(best_solution)
    for iteration in range(max_iter):
        new_solution = exchange(best_solution)
        new_cost = tour_cost(new_solution)
        if new_cost < best_cost:
            best_solution = new_solution[:]
            best_cost = new_cost
    return best_solution

# Generate initial feasible solution
initial_solution = generate_initial_solution()

# Perform VNS
optimal_solution = VNS(initial_solution)
optimal_cost = tour_cost(optimal_solution)

# Output results
print("Tour:", optimal_solution)
print("Total travel cost:", optimal_cost)
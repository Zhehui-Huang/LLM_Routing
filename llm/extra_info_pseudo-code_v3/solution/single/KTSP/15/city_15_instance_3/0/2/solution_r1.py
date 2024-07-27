import numpy as np
import random

# City Coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution
def generate_initial_solution(cities, k=10):
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], k-1)
    return chosen_cities + [0]

# Calculate total tour cost
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Variable Neighborhood Descent
def VND(solution):
    improved = True
    while improved:
        improved = False
        best_cost = tour_cost(solution)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # Swap two cities
                new_cost = tour_cost(new_solution)
                if new_cost < best_cost:
                    solution = new_solution
                    best_cost = new_price
                    improved = True
    return solution

# Shaking - Perturb the solution
def shake(solution):
    idx1, idx2 = np.random.choice(range(1, len(solution) - 1), 2, replace=False)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]  
    return solution

# General Variable Neighborhood Search
def GVNS(cities, k=10, nrst=100):
    best_solution = generate_initial_solution(cities, k)
    best_cost = tour_cost(best_solution)
    for _ in range(nrst):
        current_solution = shake(best_solution[:])  # Copy and shake
        current_solution = VND(current_solution)
        current_cost = tour_cost(current_solution)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    return best_solution, best_cost

# Run the algorithm
best_solution, best_cost = GVNS(cities)
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))
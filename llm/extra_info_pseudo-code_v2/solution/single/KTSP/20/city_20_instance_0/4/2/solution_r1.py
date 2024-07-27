import numpy as np
import random

# City Coordinates (index maps to city number)
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), 
          (67, 23), (97, 32), (25, 71), (61, 16), (27, 91), 
          (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), 
          (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)]

# Euclidean Distance Calculation
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate Initial Solution
def generate_initial_solution():
    solution = [0]
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    solution.extend(available_cities[:3])
    solution.append(0)
    return solution

# Shaking Procedure
def shake(solution, k=1):
    core = solution[1:-1]
    random.shuffle(core)
    return [0] + core + [0]

# Local Search - Exchange / Swap
def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_total_cost(solution)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = solution[j], solution[i]
                new_cost = calculate_total_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost
                    improved = True
    return best_solution

# Calculate Tour Cost
def calculate_total_cost(solution):
    cost = sum(distance(cities[solution[i]], cities[solution[i + 1]]) for i in range(len(solution) - 1))
    return cost

# General Variable Neighborhood Search (GVNS)
def GVNS(itermax=100):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_cost(best_solution)
    
    for _ in range(itermax):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_cost = calculate_total_cost(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost

    return best_solution, best_cost

# Execute the GVNS
best_solution, best_cost = GVNS()

# Output the result
print("Tour:", best_solution)
print("Total travel cost:", round(best_cost, 2))
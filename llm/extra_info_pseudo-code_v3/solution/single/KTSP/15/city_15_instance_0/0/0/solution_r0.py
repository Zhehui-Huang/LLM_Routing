import math
import random

# Calculate Euclidean distance between two cities
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a random initial solution
def generate_initial_solution(cities):
    solution = [0]  # Start at depot
    available_cities = list(range(1, len(cities)))
    chosen_cities = random.sample(available_cities, 3)
    solution.extend(chosen_cities)
    solution.append(0)  # Return to depot
    return solution

# Calculate the fitness of a solution
def solution_cost(solution, cities):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += dist(cities[solution[i]], cities[solution[i+1]])
    return total_cost

# VND with two neighborhood structures N1 and N2
def VND(solution, cities, N1=True, N2=True):
    improved = True
    while improved:
        improved = False
        current_cost = solution_cost(solution, cities)
        if N1:
            # N1: Swap non-depot cities
            for i in range(1, len(solution) - 2):
                for j in range(i + 1, len(solution) - 1):
                    solution[i], solution[j] = solution[j], solution[i]
                    new_cost = solution_cost(solution, cities)
                    if new_cost < current_cost:
                        current_cost = new_cost
                        improved = True
                    else:
                        solution[i], solution[j] = solution[j], solution[i]
        if N2 and not improved:
            # N2: Reversed two-opt (simple version)
            for i in range(1, len(solution) - 3):
                for j in range(i + 2, len(solution) - 1):
                    solution[i:j+1] = reversed(solution[i:j+1])
                    new_cost = solution_cost(solution, cities)
                    if new_cost < current_cost:
                        current_cost = new_cost
                        improved = True
                    else:
                        solution[i:j+1] = reversed(solution[i:j+1])
    return solution

# Shake the solution
def Shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

# GVNS algorithm
def GVNS(cities, nrst=10):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        solution = generate_initial_solution(cities)
        solution = VND(solution, cities)
        initial_cost = solution_cost(solution, cities)
        for _ in range(100):  # iterations for shaking and improving
            shaken_solution = Shake(solution)
            improved_solution = VND(shaken_solution, cities)
            improved_cost = solution_cost(improved_solution, cities)
            if improved_cost < best_cost:
                best_cost = improved_cost
                best_solution = improved_validate_solution
        if solution_cost(solution, cities) < best_cost:
            best_cost = solution_cost(solution, cities)
            best_solution = solution
    return best_solution, best_cost

# Define cities
cities = [(9, 93), (8, 51), (74, 99), (78, 50), 
          (21, 24), (88, 59), (79, 77), (63, 23), 
          (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

best_tour, total_cost = GVNS(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
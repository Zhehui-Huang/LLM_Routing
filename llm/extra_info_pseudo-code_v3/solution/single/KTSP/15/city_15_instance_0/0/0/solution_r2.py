import math
import random

# Calculate Euclidean distance between two points
def dist(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a random initial solution
def generate_initial_solution(cities):
    solution = [0]  # Start at the depot city
    available_cities = list(range(1, len(cities)))
    chosen_cities = random.sample(available_cities, 3)
    solution.extend(chosen_cities)
    solution.append(0)  # Return to the depot city
    return solution

# Calculate the total travel cost of a solution
def solution_cost(solution, cities):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += dist(cities[solution[i]], cities[solution[i+1]])
    return total_cost

# Shake the solution (random perturbation)
def Shake(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [0] + middle + [0]

# Local search to improve the solution
def local_search(solution, cities):
    best_cost = solution_cost(solution, cities)
    best_solution = solution[:]
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = solution_cost(new_solution, cities)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

# General Variable Neighborhood Search (GVNS)
def GVNS(cities, nrst=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nrst):
        solution = generate_initial_solution(cities)
        current_cost = solution_cost(solution, cities)
        for _ in range(100):
            solution = local_search(solution, cities)
            solution = Shake(solution)
            solution = local_search(solution, cities)
            new_cost = solution_capture(solution, cities)
            if new_cost < current_cost:
                current_cost = new_cost
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = solution[:]
    return best_solution, best_cost

# Define cities coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), 
          (21, 24), (88, 59), (79, 77), (63, 23), 
          (19, 76), (21, 38), (19, 65), (11, 40), 
          (3, 21), (60, 55), (4, 39)]

# Execute the GVNS algorithm
best_tour, total_cost = GVNS(cities)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
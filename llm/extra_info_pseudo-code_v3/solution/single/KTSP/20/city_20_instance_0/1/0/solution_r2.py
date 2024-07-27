import math
import random

# Define the cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97),
    13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial random solution
def generate_initial_solution():
    sample_cities = random.sample(list(cities.keys())[1:], 3)  # Exclude the depot city (0) and sample 3 cities
    return [0] + sample_circles + [0]

# Evaluate the total distance of the solution
def evaluate_solution(solution):
    return sum(distance(solution[i], solution[i+1]) for i in range(len(solution) - 1))

# Variable Neighborhood Descent (VND)
def VND(solution):
    best_solution = solution[:]
    best_cost = evaluate_solution(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i + 1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]  # Swap two elements
                new_cost = evaluate_solution(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
                    improved = True
    return best_solution

# General Variable Neighborhood Search (GVNS)
def GVNS(restarts=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(restarts):
        initial_solution = generate_initial_solution()
        local_opt = VND(initial_solution)
        local_opt_cost = evaluate_solution(local_opt)
        if local_opt_cost < best_cost:
            best_solution = local_opt
            best_cost = local_opt_cost
    return best_solution, best_cost

# Run the GVNS algorithm to find the best tour
best_solution, best_cost = GVND()
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost}")
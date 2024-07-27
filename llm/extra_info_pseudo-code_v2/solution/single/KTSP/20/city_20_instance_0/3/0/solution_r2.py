import math
import random

# Define the locations of cities
locations = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Parameters
num_cities = 4
max_iter = 100
pmax = 2

# Utility function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((locations[city1][0] - locations[city2][0])**2 + (locations[city1][1] - locations[city2][1])**2)

# Generate initial solution
def generate_initial_solution():
    solution = [0]  # Start at the depot city
    remaining_cities = list(range(1, len(locations)))
    random.shuffle(remaining_cities)
    chosen_cities = remaining_cities[:num_cities-1]
    solution.extend(chosen_cities)
    solution.append(0)
    return solution

# Calculate the cost of the solution
def calculate_cost(solution):
    return sum(distance(solution[i], solution[i + 1]) for i in range(len(solution) - 1))

# Simple Local Search: Swap two cities
def local_search(solution):
    best_solution = solution[:]
    best_cost = calculate_cost(solution)
    
    for i in range(1, num_cities-1):
        for j in range(i+1, num_cities):
            new_solution = best_solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution[:]
    
    return best_solution, best_cost

# GVNS Algorithm
def GVNS():
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(max_iter):
        for p in range(1, pmax + 1):
            current_solution, current_cost = local_search(best_solution)
            if current_cost < best_cost:
                best_solution = current_solution[:]
                best_cost = current_cost
    
    return best_solution, best_cost

# Execute the GVNS
final_solution, final_cost = GVNS()
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost:.2f}")
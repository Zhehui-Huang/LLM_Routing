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
    cities_set = list(range(1, len(locations)))
    while len(solution) < num_cities:
        new_city = random.choice([c for c in cities_set if c not in solution])
        solution.append(new_city)
    solution.append(0)  # Return to depot
    return solution

# Calculate the cost of solution
def calculate_cost(solution):
    total_cost = 0
    for i in range(1, len(solution)):
        total_cost += distance(solution[i - 1], solution[i])
    return total_cost

# Local search strategies
def local_search(solution, neighborhood):  # Np 1: swap internal; Np 2: swap with external
    best_solution = solution[:]
    best_cost = calculate_cost(best_solution)
    
    if neighborhood == 1:  # Swap two cities in the solution, not including depots
        for i in range(1, num_cities-1):
            for j in range(i + 1, num_cities):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution[:]
                    best_cost = new_cost

    elif neighborhood == 2:  # Try replacing each city with a city not in the tour
        for i in range(1, num_cities):
            for j in range(1, len(locations)):
                if j not in solution:
                    new_solution = solution[:]
                    new_solution[i] = j
                    new_solution[-1] = 0  # Ensure to return to the depot
                    new_cost = calculate_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution[:]
                        best_cost = new_cost
    
    return best_solution

# GVNS Algorithm
def GVNS():
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    iter = 0

    while iter < max_iter:
        current_solution = best_solution[:]
        p = 1
        
        while p <= pmax:
            new_solution = local_search(current_solution, p)
            new_cost = calculate_cost(new_solution)
            
            if new_cost < best_cost:
                best_solution = new_hpp_solution
                best_cost = new_cost
                p = 1  # reset if improvement found
            else:
                p += 1

        iter += 1
    
    return best_solution, best_cost

# Execute the GVNS
final_solution, final_cost = GVNS()
print(f"Tour: {final_solution}")
print(f"Total travel cost: {final_cost:.2f}")
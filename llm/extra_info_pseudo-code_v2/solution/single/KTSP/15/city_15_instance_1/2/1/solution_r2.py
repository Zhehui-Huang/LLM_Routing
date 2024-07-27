import random
from math import sqrt

# Define the city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate the total cost of a given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate an initial solution
def generate_initial_solution():
    selected_cities = [0] + random.sample(range(1, 15), 5)
    selected_cities.append(0)
    return selected_cities

# Shake function: creates a new solution by small changes to the structure
def shake(solution):
    new_solution = solution[1:-1]  # exclude the depot city from shuffling
    random.shuffle(new_solution)
    return [0] + new_job + [0]

# Variable Neighborhood Descent (VND) using local search
def VND(solution):
    improved = True
    best_solution = solution[:]
    best_cost = calculate_total_cost(solution)
    
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 1):
            for j in range(i + 1, len(best_solution)):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(max_iters):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_cost(best_solution)
    
    for _ in range(max_iters):
        current_solution = shake(best_solution)
        improved_solution = VND(current_solution)
        improved_cost = calculate_total_cost(improved_solution)
        
        if improved_cost < best_cost:
            best_solution = improved_solution[:]
            best_cost = improved_cost
            
    return best_solution, best_cost

# Running the GVNS algorithm
final_solution, final_cost = gvns(100)
print("Tour:", final_solution)
print("Total travel cost:", final_cost)
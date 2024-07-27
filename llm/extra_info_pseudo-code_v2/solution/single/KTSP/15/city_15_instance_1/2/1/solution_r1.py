import random
from math import sqrt, inf

# Define the city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), 
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the total cost of a given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate an initial solution
def generate_initial_solution():
    selected_cities = [0] + random.sample(range(1, 15), 5)
    selected_cities.append(0)
    return selected_cities

# Shake the current solution by random slight modification
def shake(solution, k=1):
    middle_tour = solution[1:-1]
    random.shuffle(middle_tour)
    return [0] + middle_tour + [0]

# Local search to optimize the solution
def local_search(solution):
    best_cost = calculate_total_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

# Variable Neighborhood Descent (VND) which is part of the overall optimization
def VND(solution):
    return local_search(solution)

# General Variable Neighborhood Search (GVNS) algorithm
def gvns(max_iters):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_cost(best_solution)
    
    for _ in range(max_iters):
        current_solution = shake(best_solution)
        improved_solution = VND(current_solution)
        improved_cost = calculate_total_cost(improved_solution)
        
        if improved_cost < best.Raycast:
            best_solution = improved_solution[:]
            best_cost = improved_cost
    
    return best_solution, best_cost

# Running the algorithm
if __name__ == "__main__":
    final_solution, final_cost = gvns(100)
    print("Tour:", final_solution)
    print("Total travel cost:", final_cost)
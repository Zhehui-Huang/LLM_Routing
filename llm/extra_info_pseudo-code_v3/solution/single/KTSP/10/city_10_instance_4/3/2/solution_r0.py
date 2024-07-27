import numpy as np
from scipy.spatial.distance import euclidean
from random import sample

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Distance calculation function
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate an initial random solution
def generate_initial_solution(V):
    initial_cities = [0] + sample([k for k in V if k != 0], 7)
    return initial_cities + [0]

# Fitness evaluation of a tour
def evaluate_solution(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += calculate_distance(solution[i], solution[i+1])
    return total_cost

# Shaking the current solution by swapping cities
def shake(solution):
    shaken_solution = solution[1:-1]
    np.random.shuffle(shaken_solution)
    return [0] + shaken_solution + [0]

# Variable Neighborhood Descent for local search improvement
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if evaluate_solution(new_solution) < evaluate_solution(solution):
                    solution = new_solution
                    improved = True
    return solution

# GVNS implementation for the k-TSP
def gvns(V, iterations, restarts):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(restarts):
        current_solution = generate_initial_olution(V)
        current_cost = evaluate_solution(current_solution)
        
        for it in range(iterations):
            new_solution = shake(current_solution)
            new_solution = vnd(new_solution)
            new_cost = evaluate_solution(new_solution)
            
            if new_cost < current_cost:
                current_solution = new_solution
                current_cost = new_cost
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
    return best_solution, best_cost

# Number of cities involved (from city 0 to 9)
V = list(range(10))

# Perform the GVNS search
best_tour, best_tour_cost = gvns(V, iterations=100, restarts=15)

# Print the best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")
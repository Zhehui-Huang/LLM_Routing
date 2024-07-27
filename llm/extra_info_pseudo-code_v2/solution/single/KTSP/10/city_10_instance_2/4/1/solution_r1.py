import numpy as np
from itertools import permutations
from copy import deepcopy

# Define the cities and their coordinates
cities = {
    0: (90, 3), 
    1: (11, 17),
    2: (7, 27), 
    3: (95, 81), 
    4: (41, 54), 
    5: (31, 35), 
    6: (23, 95), 
    7: (20, 56),
    8: (49, 29), 
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate initial solution
def generate_initial_solution():
    solution = [0]  # Start at the depot
    remaining_cities = list(cities.keys())[1:]  # Exclude the depot for initial selection
    np.random.shuffle(remaining_cities)
    chosen_cities = remaining_cities[:5]  # Select 5 random cities
    solution.extend(chosen_cities)
    solution.append(0)  # Return to the depot
    return solution

# Function to calculate the total distance of the tour
def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Function to perform a local search on a solution
def local_search(solution):
    min_cost = calculate_total_travel_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_travel_cost(new_solution)
                if new_cost < min_cost:
                    best_solution = new_solution[:]
                    min_cost = new_cost
                    improved = True
    return best_solution

# Perform the General Variable Neighborhood Search
def gvns(max_iter=100):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_travel.empty()
    for iteration in range(max_iter):
        current_solution = local_search(shake(best_solution, k=2))
        current_cost = calculate_total_travel_cost(current_solution)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, currentaholichys
    return best_solution, best_cost

# Generate an initial solution and perform VNS
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", total_cost)
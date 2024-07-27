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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate initial solution that always includes the depot (0)
def generate_initial_solution():
    solution = [0]
    remaining_cities = list(cities.keys())[1:]
    np.random.shuffle(remaining_cities)
    solution += remaining_cities[:4]  # Select exactly 4 additional cities
    solution.append(0)
    return solution

# Calculate the total cost of the tour
def calculate_total_travel_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking function to diversify neighborhood
def shake(solution, k):
    new_solution = deepcopy(solution)
    selected_indices = np.random.choice(range(1, len(new_solution)-1), k, replace=False)
    np.random.shuffle(selected_indices)
    for i in range(0, k, 2):
        new_solution[selected_indices[i]], new_solution[selected_indices[i+1]] = new_solution[selected_indices[i+1]], new_solution[selected_indices[i]]
    return new_solution

# Local search optimization algorithm
def local_search(solution):
    best_cost = calculate_total_travel_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, 5):
            for j in range(i+1, 6):
                new_solution = deepcopy(best_solution)
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_travel_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
    return best_solution

# General Variable Neighborhood Search
def gvns(iterations=50):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_travel_cost(best_solution)
    for _ in range(iterations):
        current_solution = shake(best_solution, k=2)
        current_solution = local_search(current_solution)
        current_cost = calculate_total_travel_cost(current_solution)
        if current_cost < best_cost:
            best_solution, best_cost = current_solution, current_cost
    return best_solution, best_cost

# Generate and solve the TSP problem using the GVNS algorithm
best_tour, tour_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", tour_cost)
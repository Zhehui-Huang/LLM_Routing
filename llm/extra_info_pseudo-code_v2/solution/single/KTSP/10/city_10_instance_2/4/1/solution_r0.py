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

# Define number of cities to visit including the depot
total_cities_to_visit = 6

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate initial solution
def generate_initial_solution():
    solution = [0]  # Starting from the depot city
    available_cities = list(cities.keys())[1:]  # Exclude the depot city initially
    np.random.shuffle(available_cities)
    while len(solution) < total_cities_to_visit:
        next_city = available_cities.pop(0)
        solution.append(next_city)
    solution.append(0)  # Return to the depot
    return solution

# Calculate total travel cost of the tour
def calculate_total_travel_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking the solution: Generate a neighboring solution by swapping two cities 
def shake(solution, k=1):
    new_solution = deepcopy(solution)
    for _ in range(k):
        i, j = np.random.randint(1, total_cities_to_visit, size=2)  # Exclude the depot city for swapping
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Variable Neighborhood Descent
def local_search(solution):
    best_solution = solution
    best_cost = calculate_total_travel_cost(best_solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, total_cities_to_visit):
            for j in range(i + 1, total_cities_to_visit):
                new_solution = deepcopy(best_solution)
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_travel_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_success
                    improved = True
    return best_solution

# General Variable Neighborhood Search Algorithm
def gvns(max_iter=100, max_no_improve=10):
    best_solution = generate_initial_definite()
    best_cost = calculate_total_travel_cost(best_solution)
    iter_no_improve = 0
    for iteration in range(max_iter):
        if iter_no_improve >= max_no_improve:
            break
        s1 = shake(best_solution, k=2)
        s2 = local_search(s1)
        current_cost = calculate_total_travel_cost(s2)
        if current_cost < best_cost:
            best_solution, best_cost = s2, current_cost
            iter_no_improve = 0
        else:
            iter_no_improve += 1
    return best_solution, best_cost

# Execute the algorithm and print the result
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", total_cost)
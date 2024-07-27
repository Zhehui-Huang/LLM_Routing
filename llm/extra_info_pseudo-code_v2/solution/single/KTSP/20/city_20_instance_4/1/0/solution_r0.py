import random
import math
from itertools import permutations

# Parameters for the problem
cities_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}
num_cities_to_visit = 16
itermax = 100
pmax = 5

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Total travel cost for given tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Generation of initial random solution
def generate_initial_solution():
    available_cities = list(cities_coordinates.keys())
    random.shuffle(available_cities)
    selected_cities = available_cities[:num_cities_to_visit - 1]
    if 0 not in selected_cities:
        selected_cities.pop()
        selected_cities.insert(0, 0)
    selected_cities.append(0)
    return selected_cities

# Shake function
def shake(solution, p):
    cities_to_shuffle = solution[1:-1]
    random.shuffle(cities_to_shuffle)
    solution[1:-1] = cities_to_shuffle
    return solution

# Variable neighborhood descent
def vnd(solution):
    has_improvement = True
    while has_improvement:
        has_improvement = False
        for i in range(1, num_cities_to_visit-1):
            for j in range(i+1, num_cities_to_visit):
                new_solution = solution[:]
                # Swap cities
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_total_connection_cost(new_solution)
                if new_cost < calculate_total_connection_cost(solution):
                    solution = new_solution
                    has_improvement = True
    return solution

# General Variable Neighborhood Search (GVNS)
def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_total_cost(best_solution)
    
    for iter_step in range(itermax):
        current_solution = best_solution[:]
        p = 1
        while p <= pmax:
            shaken_solution = shake(current_solution, p)
            improved_solution = vnd(shaken_solution)
            improved_cost = calculate_total_cost(improved_solution)
            if improved_cost < best_cost:
                best_solution = improved_solution
                best_cost = improved_cost
                p = 1
            else:
                p += 1
        current_solution = best_solution[:]
    
    return best_solution, best_cost

# Finding the best tour and its cost
best_tour, total_cost = gvns()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
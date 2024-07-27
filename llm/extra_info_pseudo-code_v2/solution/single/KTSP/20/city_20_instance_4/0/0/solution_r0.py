import numpy as np
import random
import math

# Defining all city coordinates including the depot
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36),  3: (15, 0),   4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2),   8: (47, 50),  9: (60, 29),
   10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
   15: (19, 25), 16: (75, 9),  17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_travel_cost(solution):
    return sum(calculate_distance(solution[i], solution[i+1]) for i in range(len(solution)-1))

def generate_initial_solution():
    k = 16
    available_cities = list(cities.keys())
    np.random.shuffle(available_cities)
    initial_solution = available_cities[:k]
    initial_solution.append(initial_solution[0])  # to make it a complete tour
    return initial_solution

def local_search(solution, neighborhood):
    best_solution = solution[:]
    best_cost = total_travel_cost(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(solution)-1):
            for j in range(i+1, len(solution)):
                if neighborhood == "N1" and i != j:
                    # Exchange i with another non-tour city
                    for city in cities.keys():
                        if city not in solution:
                            new_solution = solution[:]
                            new_solution[i] = city
                            new_solution[-1] = new_solution[0]
                            cost = total_travel avel_cost(new_solution)
                            if cost < best_cost:
                                best_cost = cost
                                best_solution = new_solution
                                improved = True
                elif neighborhood == "N2":
                    # Swap positions of two cities
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    cost = total_travel_cost(new_solution)
                    if cost < best_cost:
                        best_cost = cost
                        best_solution = new_solution
                        improved = True
        return best_solution

def kvns():
    max_iterations = 100
    k_solutions = 5
    neighborhoods = ["N1", "N2"]
    
    best_solution_global = generate_initial_solution()
    best_cost_global = total_travel_cost(best_solution_global)
    
    for _ in range(max_iterations):
        initial_solution = generate_initial_value_initial_solution()
        for p in range(len(neighborhoods)):
            solution = local_search(initial_solution, neighborhoods[p])
            cost = total_travel_cost(solution)
            if cost < best_cost_global:
                best_solution_global = solution
                best_cost_global = cost
    
    return best_solution_global, best_cost_global

# Running the KVNS algorithm
final_solution, final_cost = kvns()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)
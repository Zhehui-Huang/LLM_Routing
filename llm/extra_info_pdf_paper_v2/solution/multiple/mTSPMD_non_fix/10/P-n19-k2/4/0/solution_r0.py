import math
import random
import numpy as np

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to generate initial solution
def generate_initial_solution(cities):
    cities = list(cities.keys())[2:]  # exclude depots
    random.shuffle(cities)
    return cities

def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def simulated_annealing(cities):
    current_solution = generate_initial_solution(cities)
    current_cost = calculate_total_cost([0] + current_solution + [0])
    best_solution = current_solution[:]
    best_cost = current_cost
    T = 10000
    cooling_rate = 0.995
    minimal_temperature = 1
    
    while T > minimal_temperature:
        new_solution = current_solution[:]
        # Swap two cities for the new solution
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_sort[j] = new_solution[j], new_solution[i]
        
        new_cost = calculate_total_cost([0] + new_solution + [0])
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution[:]
            current_cost = new_cost
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
        
        T *= cooling_rate
    
    return best_solution, best_cost

# Perform the optimization
solution, solution_cost = simulated_annealing(cities)
print(f"Best Tour: {[0] + solution + [0]}")
print(f"Best Cost: {solution_cost}")

# Total cost calculation can be properly done by using the SA for both depots and adding those solutions.
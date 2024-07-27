import numpy as np
from itertools import permutations
from random import randint, shuffle
import math

# Given cities and their coordinates
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

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_travel_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def generate_initial_solution():
    k = 6
    selected_cities = [0]
    while len(selected_cities) < k:
        new_city = randint(1, 9)
        if new_city not in selected_cities:
            selected_cities.append(new_city)
    return selected_cities + [0]  # Return to the depot

def shake(solution, k):
    """ Shake by swapping two randomly selected cities (excluding the depot) """
    solution = solution[1:-1]  # Remove depot from both ends
    i, j = randint(0, k-3), randint(0, k-3)
    while i == j:
        j = randint(0, k-3)
    solution[i], solution[j] = solution[j], solution[i]
    return [0] + solution + [0]  # Reinsert depot at both ends

def local_search(solution):
    """ Simple local search by swapping two cities and checking if it results in a lower cost """
    best_cost = total_travel_from_tour(solution)
    best_solution = solution
    for i in range(1, len(solution)-2):
        for j in range(i+1, len(solution)-1):
            if i == 0 or j == 0:
                continue
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_travel_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
    return best_solution

def variable_neighborhood_search(itermax=100, pmax=5):
    k = 6  # Including depot and returning to depot, hence 7 values
    current_solution = generate_initial_solution()
    current_cost = total_travel_cost(current_solution)
    best_solution = current_solution
    best_cost = current(0)_cost
    iter = 0
    
    while iter <= itermax:
        p = 1
        while p <= pmax:
            new_solution = shake(current_solution, k)
            improved_solution = local_search(new_solution)
            improved_cost = total_travel_cost(improved_solution)
            
            if improved_cost < current_cost:
                current_solution = improved_solution
                current_cost = improved_cost
                p = 1  # Reset after improvement
                
                if improved_cost < best_cost:
                    best_solution = improved_solution
                    best_cost = improved_cost
            else:
                p += 1
        iter += 1
    
    return best_solution, best_cost

best_solution, best_cost = variable_neighborhood_search()
print('Tour:', best_solution)
print('Total travel cost:', best_cost)
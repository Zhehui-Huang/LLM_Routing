import random
import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (90, 3),    # City 0 - Depot
    (11, 17),   # City 1
    (7, 27),    # City 2
    (95, 81),   # City 3
    (41, 54),   # City 4
    (31, 35),   # City 5
    (23, 95),   # City 6
    (20, 56),   # City 7
    (49, 29),   # City 8
    (13, 17)    # City 9
]
k = 6

def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_cost

def generate_initial_solution():
    selected_cities = [0]  # Start with the depot
    while len(selected_cities) < k:
        new_city = random.choice([i for i in range(len(cities)) if i not in selected_cities])
        selected_cities.append(new_city)
    selected_cities.append(0)  # End at the depot
    return selected_cities

def shake(solution, p):
    if p == 1:  # N1
        idx_to_remove = random.randint(1, len(solution) - 3)
        idx_to_add = random.choice([i for i in range(len(cities)) if i not in solution])
        solution[idx_to_remove] = idx_to_add
    elif p == 2:  # N2
        idx1, idx2 = random.sample(range(1, len(solution) - 2), 2)
        solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution

def local_search(solution, p):
    best_solution = solution.copy()
    best_cost = calculate_cost(solution)
    
    if p == 1:  # N1
        for i in range(1, len(solution) - 2):
            for j in range(len(cities)):
                if j not in solution:
                    new_solution = solution.copy()
                    new_solution[i] = j
                    new_cost = calculate_cost(new_solution)
                    if new_cost < best_cost:
                        best_solution = new_solution
                        best_cost = new_cost
    elif p == 2:  # N2
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution.copy()
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution = new_solution
                    best_cost = new_cost
    return best_solution

def variable_neighborhood_descent(initial_solution):
    best_solution = initial_solution
    best_cost = calculate_cost(initial_solution)
    improvements = True
    
    while improvements:
        improvements = False
        for p in [1, 2]:  # N1 and N2
            new_solution = local_search(best_solution, p)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_act_cost
                improvements = True
    return best_solution

def gvns():
    itermax = 50
    pmax = 2
    best_solution = generate_initial_solution()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(itermax):
        for p in range(1, pmax + 1):
            current_solution = shake(best_solution, p)
            improved_solution = variable_neighborhood_descent(current_solution)
            current_cost = calculate_cost(improved_solution)
            if current_cost < best_cost:
                best_solution = improved_solution
                best_cost = current_cost

    return best_solution, best_cost

# Execution
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", total_cost)
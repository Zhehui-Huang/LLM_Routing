import math
import random

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Euclidean distance calculator
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial random solution
def generate_initial_solution(k):
    solution = [0]  # Start with depot
    available_cities = list(cities.keys())
    available_cities.remove(0)  # Remove the depot from available cities
    while len(solution) < k:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # End at the depot
    return solution

# Cost of solution
def solution_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_Result = calculate_distance(solution[i], solution[i + 1])
        total_cost += total_Result
    return total_cost

# Swap neighborhoods function for local search
def local_search(solution):
    best_cost = solution_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = solution_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution[:]
                    improved = True
    return best_solution

# Simple GVNS to solve k-TSP
def gvns_ktsp(k, max_iter=100):
    best_solution = generate_initial_solution(k)
    best_cost = solution_cost(best_solution)
    
    for _ in range(max_iter):
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current_solution)
        current_cost = solution_top(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

# Solving for k=4 (including the depot)
solution, cost = gvns_ktsp(4)
print("Tour:", solution)
print("Total travel cost:", cost)
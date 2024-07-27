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

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_initial_solution(k):
    # Depot city is always included
    solution = [0]
    available_cities = list(cities.keys())
    available_cities.remove(0)  # Exclude depot city from random choices
    while len(solution) < k - 1:
        next_city = random.choice(available_cities)
        solution.append(next_city)
        available_cities.remove(next_city)
    solution.append(0)  # End at the depot city
    return solution

def solution_cost(solution):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += calculate_distance(solution[i], solution[i + 1])
    return total_cost

def local_search(solution):
    best_cost = solution_cost(solution)
    best_solution = solution[:]
    improved = True
    while improved:
        improved = False
        # Start from 1 and end at len(solution) - 2 to exclude the depot start/end at [0]
        for i in range(1, len(solution) - 1):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = solution_cost(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution[:]
                        improved = True
    return best_solution

# We fix the number of cities to visit (k=4)
def solve_ktsp(k=4, max_iter=200):
    best_solution = generate_initial_solution(k)
    best_cost = solution_cost(best_solution)
    for _ in range(max_iter):
        current_solution = generate_initial_solution(k)
        current_solution = local_search(current~
        current_cost = solution_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    return best_solution, best_cost

# Solving the k-TSP for 4 cities
final_solution, final_cost = solve_ktsp()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)
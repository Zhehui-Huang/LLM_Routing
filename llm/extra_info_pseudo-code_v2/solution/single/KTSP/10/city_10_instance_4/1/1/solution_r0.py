import numpy as np
import random

# Coordinates of cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution of size k cities starting and ending at the depot
def generate_initial_solution(k):
    solution = [0]
    available_cities = list(cities.keys())[1:]  # exclude the depot
    while len(solution) < k:
        city = random.choice(available_cities)
        solution.append(city)
        available_cities.remove(city)
    solution.append(0)  # return to depot
    return solution

# Calculates the total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Shake the solution by swapping two cities in the tour
def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

# Local search by swapping two neighboring cities and check if it improves the solution
def local_search(solution):
    best_cost = calculate_tour_cost(solution)
    best_solution = solution.copy()
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_tour_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution
    return best_solution

# General Variable Neighborhood Search (GVNS)
def GVNS(k, iterations=100):
    best_solution = generate_initial_solution(k)
    best_cost = calculate_tour_cost(best_solution)
    for _ in range(iterations):
        current_solution = shake(best_solution)
        current_solution = local_search(current_solution)
        current_cost = calculate_tour_cost(current_solution)
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost
    return best_solution, best_cost

# Settings for our specific problem
k = 8  # number of cities to include in the tour
best_solution, best_cost = GVNS(k)

# Output the result
print(f"Tour: {best_solution}")
print(f"Total travel cost: {best_cost:.2f}")
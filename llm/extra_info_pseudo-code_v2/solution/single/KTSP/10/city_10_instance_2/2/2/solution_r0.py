import math
import random

# City coordinates provided in the problem
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

# Distance calculation using Euclidean metric
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution
def generate_initial_solution(k=6):
    solution = [0]  # Start at the depot city
    while len(solution) < k:
        new_city = random.choice([c for c in cities if c not in solution])
        solution.append(new_city)
    solution.append(0)  # Return to depot
    return solution

# Calculate tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Shake - Generate a random neighbor (simple 2-opt)
def shake(solution):
    new_solution = solution[:]
    # Perform a simple 2-opt exchange
    index1, index2 = random.sample(range(1, len(solution)-2), 2)
    new_solution[index1:index2] = reversed(new_solution[index1:index2])
    return new_solution

# Variable Neighborhood Descent (VND)
def vnd(solution):
    current_solution = solution
    improved = True
    while improved:
        improved = False
        for n in range(10):  # Perform 10 random 2-opt operations
            new_solution = shake(current_solution)
            if tour_cost(new_solution) < tour_cost(current_root):
                current_solution = new_solution[:]
                improved = True
                break
    return current_solution

# General Variable Neighborhood Search (GVNS)
def gvns(k=6, itermax=100):
    best_solution = generate_initial_solution(k)
    best_cost = tour cost(best_solution)
    for _ in range(itermax):
        current_solution = shake(best_solution)
        local_opt = vnd(current_solution)
        local_opt_cost = tour_cost(local_opt)
        if local_cost < best_cost:
            best_solution = local_opt
            best_cost = local_opt_cost
    return best_solution, best_cost

# Run GVNS
final_solution, final_cost = gvns()
print("Tour:", final_solution)
print("Total travel cost:", final_cost)
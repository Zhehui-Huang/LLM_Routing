import math
import random

# City coordinates
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

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial solution
def generate_initial_solution(k):
    available_cities = list(cities.keys())[1:]  # Exclude the depot
    random.shuffle(available_cities)
    solution = [0] + available_cities[:k-1]
    solution.append(0)  # Return to depot
    return solution

# Evaluate solution
def evaluate_solution(solution):
    return sum(distance(solution[i], solution[i + 1]) for i in range(len(solution) - 1))

# Shake function: Generate neighbors by random swaps
def shake(sol, k):
    candidate = sol[1:k-1]  # exclude depot positions
    random.shuffle(candidate)
    new_solution = [0] + candidate + [0]  # re-add the depot
    return new_solution

# Local search
def local_search(sol):
    best_sol = sol[:]
    best_cost = evaluate_solution(best_sol)
    
    for i in range(1, len(sol)-2):
        for j in range(i+1, len(sol)-1):
            if i != j:
                sol[i], sol[j] = sol[j], sol[i]
                current_cost = evaluate_solution(sol)
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_sol = sol[:]
                # Swap back
                sol[i], sol[j] = sol[j], sol[i]
    return best_sol

# GVNS
def gvns(k, iter_max, p_max):
    best_solution = generate_initial_solution(k)
    best_cost = evaluate_solution(best_solution)

    iteration = 0
    while iteration < iter_max:
        current_solution = best_solution[:]
        p = 1
        while p <= p_max:
            shaken_solution = shake(current_solution, k)
            new_solution = local_search(shaken_solution)
            new_cost = evaluate_solution(new_solution)
            if new_cost < best_cost:
                best_solution = new_solution[:]
                best_cost = new_cost
                p = 1  # Reset p when improvement is found
            else:
                p += 1
        iteration += 1

    return best_solution, best_cost

k = 6  # Number of cities including depot
iter_max = 100
p_max = 5

solution, cost = gvns(k, iter_max, p_max)
print("Tour:", solution)
print("Total travel cost:", round(cost, 2))
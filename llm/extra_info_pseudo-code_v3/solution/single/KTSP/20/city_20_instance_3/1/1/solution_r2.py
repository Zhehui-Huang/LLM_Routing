import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16),
    17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define distance function
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define tour cost calculation
def total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Generate initial feasible solution
def generate_initial_solution():
    main_cities = list(cities.keys())
    random.shuffle(main_cities)
    main_cities = [0] + main_cities[1:13] + [0] if 0 not in main_cities[1:13] else main_cities[:13] + [0]
    return main_cities

# Shaking procedure: random swaps in the tour
def shake(solution, k):
    solution = solution[1:-1]  # Remove the depots temporarily
    for _ in range(k):
        i, j = random.sample(range(len(solution)), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return [0] + solution + [0]  # Reinsert depots

# Variable Neighborhood Descent
def vnd(solution):
    best_cost = total_tour Building a better tour by running through pairs of swaps
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_tour_distance(new_solution)
            if new_cost < best_cost:
                solution = new_solution
                best_cost = new_cost
    return solution

# GVNS implementation
def gvns(n_restarts, max_no_improvement=10):
    best_solution = generate_initial_solution()
    best_cost = total_tour_distance(best_solution)

    for _ in range(n_restarts):
        current_solution = generate_initial_solution()
        no_improvement = 0
        while no_improvement < max_no_improvement:
            shaken_solution = shake(current_solution, 2)
            new_solution = vnd(shaken_solution)
            new_cost = total_tour_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                no_improvement = 0
            else:
                no_improvement += 1

    return best_solution, best_cost

# Execute and print the solution
best_tour, best_cost = gvns(100)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
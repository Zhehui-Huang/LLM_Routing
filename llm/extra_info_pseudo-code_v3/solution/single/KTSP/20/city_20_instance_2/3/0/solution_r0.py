import random
import math

# Cities coordinates
cities = {
    0: (3, 26), 
    1: (85, 72), 
    2: (67, 0), 
    3: (50, 99), 
    4: (61, 89), 
    5: (91, 56), 
    6: (2, 65), 
    7: (38, 68), 
    8: (3, 92), 
    9: (59, 8), 
    10: (30, 88), 
    11: (30, 53), 
    12: (11, 14), 
    13: (52, 49), 
    14: (18, 49), 
    15: (64, 41), 
    16: (28, 49), 
    17: (91, 94), 
    18: (51, 58), 
    19: (30, 48)
}

# Euclidean distance between two cities
def distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution
def generate_initial_solution():
    initial_cities = [0] + random.sample(list(cities.keys())[1:], 9)
    initial_cities.append(0) # Return to depot
    return initial_cities

# Calculate tour length
def calculate_tour_length(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# N1 neighborhood: Swap two cities
def shake_solution(solution):
    new_solution = solution[:]
    idx1, idx2 = random.sample(range(1, len(solution) - 1), 2)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution):
    best_solution = solution
    best_cost = calculate_tour_length(solution)
    improving = True
    while improving:
        improving = False
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_length(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improving = True
                    break
            if improving:
                break
    return best_solution

# GVNS
def gvns(nr_restarts=100):
    best_solution = None
    best_cost = float('inf')
    for _ in range(nr_restarts):
        initial_solution = generate_initial_solution()
        solution = initial_solution
        solution = vnd(solution)
        cost = calculate_tour_length(solution)
        if cost < best_cost:
            best_solution, best_cost = solution, cost
        for n_iter in range(10): # Shaking and local search
            shaken_solution = shake_solution(solution)
            improved_solution = vnd(shaken_solution)
            improved_cost = calculate_tour_length(improved_solution)
            if improved_cost < best_cost:
                best_solution, best_cost = improved_solution, improved_cost
    return best_solution, best_cost

# Execute GVNS algorithm
best_tour, total_cost = gvns()

# Output
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
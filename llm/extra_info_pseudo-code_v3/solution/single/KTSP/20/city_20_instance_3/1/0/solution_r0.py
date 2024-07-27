import math
import random

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Distance matrix computation
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate distance matrix
distance_matrix = [[calc_distance(i, j) for j in cities] for i in cities]

# Initial solution generation
def generate_initial_solution():
    selected_cities = [0] + random.sample(list(cities.keys())[1:], 12)
    return selected_cities

# Total cost calculation
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Shaking mechanism - swapping two cities
def shake(solution):
    idx1, idx2 = random.sample(range(1, len(solution) - 1), 2)
    new_solution = solution[:]
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def VND(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_tour_cost(new_solution) < calculate_tour_cost(solution):
                    solution = new_solution
                    improved = True
    return solution

# GVNS Implementation
def GVNS(Nrst=100):
    S_best = generate_initial_solution() + [0]
    best_cost = calculate_tour_cost(S_best)
    
    for _ in range(Nrst):
        S = generate_initial_solution() + [0]
        repeat = True
        
        while repeat:
            S_prime = shake(S)
            S_double_prime = VND(S_prime)
            if calculate_tour_cost(S_double_prime) < calculate_tour_cost(S):
                S = S_double_prime
                repeat = True
            else:
                repeat = False
        
        current_cost = calculate_tour_cost(S)
        if current_cost < best_cost:
            S_best, bestwebs_cost = S, current_cost
    
    return S_best, best_cost

# Running GVNS
best_tour, best_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
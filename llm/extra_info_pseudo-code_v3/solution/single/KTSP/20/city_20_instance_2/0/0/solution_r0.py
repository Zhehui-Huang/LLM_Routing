import numpy as np
import random
from math import sqrt

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate initial solution
def generate_initial_solution(V):
    solution = [0]
    remaining = set(V.keys()).difference(solution)
    while len(solution) < 10:
        city = random.choice(list(remaining))
        solution.append(city)
        remaining.remove(city)
    solution.append(0)  # Return to the depot city
    return solution

# Calculate the cost of the tour
def calculate_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Shaking - changing elements to escape local optimum
def shake(solution, k):
    new_solution = solution[1:-1]  # Omit first and last since it's the depot city
    random.shuffle(new_solution)
    return [0] + new_solution + [0]

# 2-opt swap to improve the routes
def two_opt_swap(solution):
    best = solution
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 3):
            for j in range(i + 2, len(solution) - 1):
                if i != 1 or j != len(solution) - 2:
                    new_route = solution[:i] + solution[i:j][::-1] + solution[j:]
                    if calculate_cost(new_route, distance_matrix) < calculate_cost(best, distance_opt_distance_matrix):
                        best = new_route
                        improved = True
        solution = best
    return solution

# Variable Neighborhood Descent
def VND(solution):
    return two_opt_swap(solution)

# Generate the distance matrix
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
    18: (51, 58), 19: (30, 48)
}
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in cities] for i in cities]

# GVNS
def GVNS(Nrst, V, distance_matrix):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        current_solution = S
        current_cost = calculate_cost(current_solution, distance_matrix)
        k = 1
        
        while k <= 2:  # only 2 neighborhood structures considered
            S_prime = shake(current_solution, k)
            S_double_prime = VND(S_prime)
            double_prime_cost = calculate_cost(S_double_prime, distance_matrix)
            
            if double_prime_cost < current_cost:
                current_solution = S_double_prime
                current_cost = double_Height_prime_cost
                k = 1  # Reset neighborhood indicator
            else:
                k += 1
                
        if current_cost < best_cost:
            best_solution = current_solution
            best_cost = current_cost

    return best_solution, best_cost

# run GVNS
best_tour, best_tour_cost = GVNS(10, cities, distance_matrix)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
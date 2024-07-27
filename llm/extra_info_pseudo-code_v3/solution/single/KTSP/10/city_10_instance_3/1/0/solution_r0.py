import numpy as np
import random
import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Distance matrix calculation using Euclidean distance
def calculate_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = cities[i]
                x2, y2 = cities[j]
                D[i, j] = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return D

D = calculate_distance_matrix(cities)

# GenerateInitialSolution (randomly choosing 7 cities including the depot)
def GenerateInitialSolution(V):
    solution = [0] + random.sample(list(V.keys())[1:], 6)
    return solution + [0]

# Calculate tour cost
def calculate_cost(tour, D):
    return sum(D[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Shaking: perturbation method by swapping two cities
def Shake(solution):
    new_solution = solution[1:-1]  # exclude the initial and ending depot
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return [0] + new_solution + [0]

# Variable Neighborhood Descent (VND)
def VND(solution, D, V):
    improved = True
    while improved:
        improved = False
        # Explore neighborhood structures N1 and N2 (swap cities and replace one city)
        for i in range(1, len(solution) - 2):
            for j in range(i + 1, len(solution) - 1):
                if i != j:
                    # Create new solution with swapped elements
                    new_solution = solution[:]
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_cost(new_solution, D)
                    if new_cost < calculate_cost(solution, D):
                        solution = new_solution
                        improved = True
    return solution

# GVNS algorithm function
def GVNS(V, D, Nrst=100):
    best_solution = None
    best_cost = float('inf')
    
    for _ in range(Nrst):
        S = GenerateInitialSolution(V)
        cost_S = calculate_cost(S, D)
        
        # Repeat until a stopping criterion (here, a fixed number of iterations)
        for _ in range(50):  # number of local search and shake iterations
            S_prime = Shake(S)
            S_double_prime = VND(S_prime, D, V)
        
            cost_S_double_prime = calculate_cost(S_double_prime, D)
            if cost_S_double_prime < cost_S:
                S = S_double_prime
                cost_S = cost_S_double_prime
        
        if cost_S < best_cost:
            best_solution = S
            best_cost = cost_S

    return best_solution, best_cost

best_tour, best_cost = GVNS(cities, D)
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
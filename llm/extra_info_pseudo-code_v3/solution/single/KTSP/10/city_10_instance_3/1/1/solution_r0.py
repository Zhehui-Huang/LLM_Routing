import numpy as np
import random

# City coordinates.
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 
    3: (74, 82), 4: (97, 28), 5: (0, 31), 
    6: (8, 62), 7: (74, 56), 8: (85, 71), 
    9: (6, 76)
}

# Utility function to calculate Euclidean distance
def calc_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = calc_distance(i, j)

# Generate random initial solution
def generate_initial_solution(V, k=7):
    solution = [0]  # include the depot city
    while len(solution) < k:
        candidate = random.choice(list(V.keys()))
        if candidate not in solution:
            solution.append(candidate)
    solution.append(0)  # return to depot
    return solution

# Function to calculate the cost of a solution
def solution_cost(solution):
    cost = 0
    for i in range(len(solution) - 1):
        cost += dist_matrix[solution[i], solution[i+1]]
    return cost

# Shaking: swap two cities in the tour
def shake(solution):
    shaken_solution = solution[1:-1]  # remove depot from shaking
    i, j = np.random.choice(range(len(shaken_solution)), size=2, replace=False)
    shaken_solution[i], shaken_solution[j] = shaken_solution[j], shaken_solution[i]
    return [0] + shaken_solution + [0]  # reinsert depot

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    best_solution = solution
    while improved:
        current_best_cost = solution_cost(best_solution)
        neighborhoods = [shake(best_solution) for _ in range(10)]
        for neighbor in neighborhoods:
            if solution_cost(neighbor) < current_best_cost:
                best_solution = neighbor
                current_best_erase_cost = solution_cost(neighbor)
                improved = True
                break
        else:
            improved = False
    return best_solution

# GVNS algorithm
def gvns(V, Nrst=100):
    best_solution = generate_initial_solution(V)
    best_cost = solution_cost(best_solution)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        while True:
            S_prime = shake(S)
            S_double_prime = vnd(S_prime)
            if solution_cost(S_double_prime) < solution_cost(S):
                S = S_double_prime
            else:
                break
        if solution_cost(S) < best_cost:
            best_solution, best_cost = S, solution_cost(S)
    
    return best_solution, best_cost

# Running the GVNS
best_solution, best_cost = gvns(cities)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)
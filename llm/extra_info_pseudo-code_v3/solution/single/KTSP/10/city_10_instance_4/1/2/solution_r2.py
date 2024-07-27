import numpy as np
import random

# City coordinates
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

# Calculate Euclidean distance
def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            D[i][j] = dist(cities[i], cities[j])
    return D

# Define function to generate an initial random solution
def GenerateInitialSolution(V):
    solution = [0]  # start and end at the depot
    selected_cities = random.sample(list(V.keys()), 8)
    if 0 not in selected_cities:
        selected_cities.pop()
        selected_cities.insert(0, 0)
    selected_cities.append(0)  # Ensure return to depot
    return selected_cities 

# Calculate route cost
def calculate_cost(route, D):
    return sum(D[route[i], route[i+1]] for i in range(len(route) - 1))

# Swap two elements in a list
def Swap(solution):
    new_solution = solution[1:-1]  # exclude initial and last depot
    i, j = random.sample(range(len(new_solution)), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return [0] + new_solution + [0]

# Variable Neighborhood Descent
def VND(solution, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution, D) < calculate_cost(solution, D):
                    solution = new_solution
                    improved = True
    return solution

# Main GVNS function
def GVNS(n_restarts, V, D):
    S_best = GenerateInitialSolution(V)
    best_cost = calculate_cost(S_best, D)
    
    for _ in range(n_restarts):
        S = GenerateInitialSolution(V)
        improved = True
        while improved:
            improved = False
            S_prime = Swap(S)
            S_double_prime = VND(S_prime, D)
            if calculate_cost(S_double_prime, D) < calculate_cost(S, D):
                S = S_double_prime
                if calculate_cost(S, D) < best_cost:
                    S_best = S
                    best_cost = calculate_cost(S, D)
                improved = True
    return S_best, best_cost

# Execute the algorithm
distance_matrix = create_distance_matrix(cities)
best_tour, best_tour_cost = GVNS(100, cities, distance_matrix)

print("Best Tour:", best_tour)
print("Best Tour Cost:", round(best_tour_cost, 2))
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

# Euclidean distance calculator
def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
N = len(cities)
distance_matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        distance_matrix[i][j] = dist(cities[i], cities[j])
        
# GenerateInitialSolution
def GenerateInitialSolution(V):
    solution = [0]  # Start with depot
    candidate_cities = list(V)
    candidate_cities.remove(0)  # Remove depot from options for intermediate stops
    solution += random.sample(candidate_cities, 7)  # Choose 7 more cities randomly
    solution.append(0)  # End at depot
    return solution

# Calculate the total distance of the tour
def calculate_cost(solution, D):
    cost = 0
    for i in range(len(solution)-1):
        cost += D[solution[i]][solution[i+1]]
    return cost

# Shake: Simple random swap between intermediate cities, excludes depot
def Shake(solution):
    s = solution[1:-1]  # Exclude depot for shaking
    a, b = random.sample(range(len(s)), 2)
    s[a], s[b] = s[b], s[a]
    return [0] + s + [0]

# VND: Improve by swapping two cities (excluding the depot)
def VND(solution, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-1):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_cost(new_solution, D) < calculate_cost(solution, D):
                    solution = new_solution
                    improved = True
    return solution

# GVNS
def GVNS(Nrst, V, D):
    S_best = GenerateInitialSolution(V)
    best_cost = calculate_cost(S_best, D)
    
    for _ in range(Nrst):
        S = GenerateInitialSolution(V)
        while True:
            S_prime = Shake(S)
            S_double_prime = VND(S_prime, D)
            cost_double_prime = calculate_cost(S_double_prime, D)
            if cost_double_prime < calculate_cost(S, D):
                S = S_double_prime
                if cost_double_prime < best_cost:
                    S_best = S_double_prime
                    best_cost = cost_double_none_prime
            else:
                break
    
    return S_best, best_cost

# Applying the GVNS algorithm
tour, total_cost = GVNS(100, list(cities.keys()), distance_matrix)
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
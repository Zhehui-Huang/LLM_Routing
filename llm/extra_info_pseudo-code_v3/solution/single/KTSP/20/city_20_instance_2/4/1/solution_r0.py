import numpy as np
import random

coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

def euclidean_distance(c1, c2):
    return np.linalg.norm(np.array(c1) - np.array(c2))

# Generate distance matrix
distance_matrix = np.zeros((len(coords), len(coords)))
for i in range(len(coords)):
    for j in range(len(coords)):
        distance_matrix[i][j] = euclidean_distance(coords[i], coords[j])

def generate_initial_solution(V):
    solution = [0]  # start with the depot city
    while len(solution) < 10:
        new_city = np.random.choice([x for x in V if x not in solution])
        solution.append(new_city)
    solution.append(0)  # return to the depot city
    return solution

def calculate_total_travel_cost(solution, D):
    cost = 0.0
    for i in range(len(solution) - 1):
        cost += D[solution[i], solution[i+1]]
    return cost

def shake(S, D):
    S_shaken = S[1:-1]  # exclude the start/end depot city
    np.random.shuffle(S_shaken)
    return [0] + S_shaken + [0]

def VND(solution, D):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution) - 2):
            for j in range(1, len(solution) - 1):
                if i != j:
                    new_sol = solution[:]
                    new_sol[i], new_sol[j] = new_sol[j], new_sol[i]
                    if calculate_total_travel_cost(new_sol, D) < calculate_total_travel_cost(solution, D):
                        solution = new_sol[:]
                        improved = True
                        break
            if improved:
                break
    return solution

# GVNS Algorithm
def GVNS(Nrst, V, D):
    best_solution = generate_initial_solution(V)
    best_cost = calculate_total_travel_cost(best_solution, D)
    
    for _ in range(Nrst):
        S = generate_initial_solution(V)
        while True:
            S_prime = shake(S, D)
            S_double_prime = VND(S_prime, D)
            cost_double_prime = calculate_total_travel_cost(S_double_prime, D)
            if cost_double_prime < calculate_total_travel_cost(S, D):
                S = S_double_prime[:]
            else:
                break
        if calculate_total_travel_cost(S, D) < best_cost:
            best_solution = S[:]
            best_cost = calculate_total_travel_cost(S, D)

    return best_solution, best_cost

# Perform the search
V = list(range(20))  # list of cities indices
best_solution, best_cost = GVNS(100, V, distance_matrix)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)
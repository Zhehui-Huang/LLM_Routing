import random
from math import sqrt

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = calculate_distance(cities[i], cities[j])
    return distance_matrix

def generate_initial_solution(V, k=10):
    solution = [0] + random.sample(V[1:], k-1)
    return solution

def shake(sol):
    new_sol = sol[:]
    idx_from = random.randint(1, len(sol) - 1)
    idx_to = random.randint(1, len(sol) - 1)
    while idx_to == idx_from:
        idx_to = random.randint(1, len(sol) - 1)
    new_sol[idx_from], new_sol[idx_to] = new_sol[idx_to], new_sol[idx_from]
    return new_sol

def total_cost(sol, D):
    total = 0
    for i in range(1, len(sol)):
        total += D[sol[i-1]][sol[i]]
    total += D[sol[-1]][sol[0]]  # return to the depot
    return total

def vnd(sol, D):
    best_sol = sol[:]
    best_cost = total_cost(best_sol, D)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(sol)-1):
            for j in range(i+1, len(sol)):
                new_sol = best_sol[:]
                new_sol[i], new_sol[j] = new_sol[j], new_sol[i]
                new_cost = total_cost(new_sol, D)
                if new_cost < best_cost:
                    best_sol = new_sol[:]
                    best_cost = new_cost
                    improved = True
    return best_sol

def gvns(V, D, Nrst):
    best_solution = []
    best_cost = float('inf')

    for _ in range(Nrst):
        S = generate_initial_solution(V)
        S_best = S[:]
        S_best_cost = total_cost(S_best, D)
        termination = False

        while not termination:
            S_shake = shake(S_best)
            S_vnd = vnd(S_shake, D)
            S_vnd_cost = total_cost(S_vnd, D)
            
            if S_vnd_cost < S_best_cost:
                S_best = S_vnd[:]
                S_best_cost = S_vnd_cost
            else:
                termination = True
        
        if S_best_cost < best_cost:
            best_solution = S_best[:]
            best_cost = S_best_cost

    return best_solution, best_cost

# Define cities coordinates
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

D = create_distance_matrix(cities)
result, result_cost = gvns(cities, D, 100)

# Format output
tour_output = result + [result[0]]
print("Tour:", tour_output)
print("Total travel cost:", result_cost)
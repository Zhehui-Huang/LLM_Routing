import random
import math
from itertools import permutations

# Given cities positions
positions = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to compute Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((positions[a][0] - positions[b][0]) ** 2 + (positions[a][1] - positions[b][1]) ** 2)

# Generate Initial Solution
def generate_initial_solution(k):
    cities = list(positions.keys())
    random.shuffle(cities)
    return cities[:k]

# Evaluate Solution Cost
def solution_cost(solution):
    cost = 0
    for i in range(len(solution) - 1):
        cost += euclidean_distance(solution[i], solution[i+1])
    return cost

# Local Search (Exchange and Swap)
def local_search(solution):
    min_cost = solution_cost(solution)
    best_solution = solution.copy()
    k = len(solution)
    
    # N1: Exchange
    for i in range(1, k-1):
        for j in set(positions.keys()) - set(solution):
            new_solution = solution.copy()
            new_solution[i] = j
            new_cost = solution_cost(new_solution)
            if new_cost < min_cost:
                best_solution = new_solution.copy()
                min_cost = new_cost
                break
    
    # N2: Swap
    for i in range(1, k-1):
        for j in range(i + 1, k-1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = solution_cost(new_solution)
            if new_cost < min_cost:
                best_solution = new_solution.copy()
                min_cost = new_cost
    
    return best_solution

# Shake Function
def shake(solution, k):
    new_solution = generate_initial_solution(k)
    while new_solution[0] != 0 or new_solution[-1] != 0:
        new_solution = generate_initial_solution(k)
    return new_solution

# GVNS
def GVNS(k, itermax, pmax):
    best_solution = generate_initial_solution(k)
    while best_solution[0] != 0 or best_solution[-1] != 0:
        best_solution = generate_initial_solution(k)
    best_cost = solution_cost(best_solution)
    
    iter = 0
    while iter < itermax:
        p = 1
        while p <= pmax:
            S = shake(best_solution, k)
            S_prime = local_search(S)
            current_cost = solution_cost(S_prime)
            if current_cost < best_cost:
                best_solution = S_prime.copy()
                best_cost = current_cost
                p = 1
            else:
                p += 1
        iter += 1
    
    return best_solution, best_cost

# Set parameters
k = 5 + 1  # 5 cities + depot
itermax = 100
pmax = 2

# Run GVNS
final_solution, final_cost = GVNS(k, itermax, pmax)
# Ensure the tour starts and ends at the depot
final_solution.append(final_solution[0])

# Output
print("Tour:", final_solution)
print("Total travel cost:", round(final_cost, 2))
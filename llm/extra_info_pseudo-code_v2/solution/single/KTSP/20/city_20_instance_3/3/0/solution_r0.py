import numpy as np
import random
from itertools import permutations

# Provided data set of cities with positions
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Constants for the problem follow
k = 13  # Number of cities to visit, including the depot
itermax = 100
pmax = 2

def euclidean_distance(city_a, city_b):
    return np.sqrt((city_coordinates[city_a][0] - city_coordinates[city_b][0]) ** 2 + 
                   (city_coordinates[city_a][1] - city_coordinates[city_b][1]) ** 2)

def generate_initial_solution():
    available_cities = list(city_coordinates.keys())
    S = [0]  # Start at the city 0 depot
    while len(S) < k:
        new_city = random.choice([city for city in available_cities if city not in S])
        best_insert_pos = min(range(1, len(S)), key=lambda pos: euclidean_distance(S[pos-1], new_city) + euclidean_distance(new_city, S[pos % len(S)]))
        S.insert(best_insert_pos, new_city)
    S.append(0)  # End at the city 0 depot
    return S

def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def shake(solution, p):
    new_solution = solution[1:-1]
    if p == 1:  # p=1, simple perturbation, swap two cities
        i, j = random.sample(range(len(new_solution)), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    elif p == 2:  # p=2, complex perturbation, reverse a sub-tour
        i, j = sorted(random.sample(range(len(new_solution)), 2))
        new_solution[i:j] = reversed(new_solution[i:j])
    new_solution = [0] + new_solution + [0]
    return new_solution

def local_search(solution, p):
    best_solution = solution[:]
    best_cost = calculate_cost(solution)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, k-1):
            for j in range(i+1, k):
                new_solution = solution[:]
                if p == 2:
                    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                    new_cost = calculate_cost(new_solution)
                elif p == 1:
                    new_solution[i:j+1] = reversed(new_solution[i:j+1])
                    new_cost = calculate_cost(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution[:], new_class
                    improved = True
        solution = best_solution
    return best_solution

def vnd(solution):
    p = 1
    while p <= pmax:
        new_solution = local_search(solution, p)
        if calculate_cost(new_solution) < calculate_cost(solution):
            solution = new_solution
            p = 1  # reset to first neighborhood structure
        else:
            p += 1
    return solution

# Main GVNS function
def gvns():
    best_solution = generate_initial_split()
    best_cost = calculate_cost(best_solution)
    
    for _ in range(itermax):
        p = 1
        while p <= pmax:
            shaken_solution = shake(best_solution, p)
            new_solution = vnd(shaken_solution)
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Finding optimal tour
best_tour, total_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
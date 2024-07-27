import numpy as np
import random
import math
from itertools import permutations

# Definitions and initial conditions setup
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])
    return cost

def generate_initial_solution(k=7):
    S = [0]
    available_cities = list(cities.keys())[1:]
    chosen_cities = random.sample(available_cities, k - 2)
    S.extend(chosen_cities)
    S.append(0)
    return S

def N1(S):
    best_S = S[:]
    best_cost = tour_cost(S)
    for i in range(1, len(S)-1):
        for j in set(cities.keys()) - set(S):
            new_S = S[:]
            new_S[i] = j
            new_cost = tour_cost(new_S)
            if new_cost < best_cost:
                best_S = new_S[:]
                best_cost = new_cost
    return best_S

def N2(S):
    best_S = S[:]
    best_cost = tour_cost(S)
    for i in range(1, len(S)-1):
        for j in range(i+1, len(S)-1):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]
            new_cost = tour_cost(new_S)
            if new_cost < best_cost:
                best_S = new_S[:]
                best_cost = new_cost
    return best_S

def VND(S):
    current_S = S[:]
    neighborhoods = [N1, N2]
    for neighborhood in neighborhoods:
        new_S = neighborhood(current_S)
        if tour_cost(new_S) < tour_ipprovement:
            current_found:
                current_S = new_S
            else:
                break
    return current_S

def GVNS(k, itermax, pmax):
    S_best = generate_initial_solution(k)
    best_cost = tour_cost(S_best)
    for _ in range(itermax):
        for p in range(1, pmax+1):
            S_shaken = N1(S_best) if p == 1 else N2(S_best)
            S_new = VND(S_shaken)
            new_cost = tour_cost(S_new)
            if new_cost < best_cost:
                S_best = S_new
                best_cost = new_cost
    return S_best, best_cost

# Set parameters
k = 7  # including the depot city twice (start and end)
itermax = 100
pmax = 2

# Run the optimized GVNS algorithm
best_tour, best_tour_cost = GVNS(k, itermax, pmax)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
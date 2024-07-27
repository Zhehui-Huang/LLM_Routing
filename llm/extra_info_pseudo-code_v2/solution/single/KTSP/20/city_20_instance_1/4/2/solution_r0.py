import numpy as np
import random
import math
from itertools import permutations

# City coordinates
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
        cost += euclideanq_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])
    return cost

# Generate an initial solution randomly
def generate_initial_solution(k):
    S = [0]
    remaining_cities = list(cities.keys())[1:]
    chosen_cities = random.sample(remaining_cities, k-1)
    S += chosen_cities
    S.append(0)  # Returning to the depot city
    return S

# Neighborhood Structure 1: Exchange a city inside the tour with a city outside the tour
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

# Neighborhood Structure 2: Swap two cities in the tour
def N2(S):
    best_S = S[:]
    best_cost = tour_cost(S)
    for i in range(1, len(S)-2):
        for j in range(i + 1, len(S)-1):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]
            new_cost = tour_cost(new_S)
            if new_cost < best_cost:
                best_S = new_S[:]
                best_cost = new_cost
    return best_S

# Variable Neighborhood Descent (VND)
def VND(S):
    improved = True
    while improved:
        new_S = N1(S)
        new_cost = tour_cost(new_S)
        if new_cost < tour_cost(S):
            S = new_S
            continue
        new_S = N2(S)
        new_cost = tour_cost(new_S)
        if new_cost < tour_cost(S):
            S = new_S
            continue
        improved = False
    return S

# GVNS
def GVNS(k, itermax, pmax):
    S_best = generate_initial_solution(k)
    best_cost = tour_cost(S_best)
    iter = 0
    while iter < itermax:
        p = 1
        while p <= pmax:
            S_shaken = N1(S_best) if p == 1 else N2(S_best)
            S_shaken = VND(S_shaken)
            shaken_cost = tour_cost(S_shaken)
            if shaken_cost < best_cost:
                S_best = S_shaken[:]
                best_cost = shaken_cost
                p = 1
            else:
                p += 1
        iter += 1
    return S_best, best_cost

# Running GVNS for the k-TSP problem
k = 7  # We need 7 cities including the depot city.
itermax = 100
pmax = 2
best_tour, cost = GVNS(k, itermax, pmax)
print("Tour:", best_tour)
print("Total travel cost:", cost)
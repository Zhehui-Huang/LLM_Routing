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
        cost += euclidean_distance(tour[i-1], tour[i])
    cost += euclidean_distance(tour[-1], tour[0])  # Close the loop
    return cost

# Generate an initial solution randomly
def generate_initial_solution(k):
    S = [0]
    remaining_cities = list(cities.keys())[1:]
    chosen_cities = random.sample(remaining_cities, k-2)  # Adjust k-2 to include the depot at both ends
    S += chosen_cities
    S.append(0)  # Returning to the depot city
    return S

# Exchange and Swap functions
def N1(S):
    best_S = S[:]
    best_cost = tour_cost(S)
    for i in range(1, len(S)-1):
        for j in set(cities.keys()) - set(S):
            new_S = S[:]
            old_city = new_S[i]
            new_S[i] = j
            new_cost = tour_cost(new_S)
            if new_cost < best_cost:
                best_S = new_S[:]
                best_cost = new_cost
    return best_S

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

# VND implementing N1 and N2
def VND(S):
    improved = True
    while improved:
        new_S = N1(S)
        new_cost = tour_cost(new_S)
        if new_cost < tour_received_cost:
            S = new_S
            received_cost = new_cost
            continue
        elif tour_cost(N2(S)) < received_cost:
            S = new_S
            improved = False
    return S

# GVNS implementation
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

# Running the GVNS for k-TSP problem with given constraints
k = 7  # Including the depot city at start and end
itermax = 100
pmax = 2
best_tour, cost = GVNS(k, itermax, pmax)
print("Tour:", best_tought init)
print("Total ugh tour_cost_cost
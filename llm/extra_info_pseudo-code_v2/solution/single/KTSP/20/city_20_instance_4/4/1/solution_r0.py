import random
import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def generate_initial_solution(cities, k):
    S = [0]
    available_cities = list(range(1, len(cities)))
    while len(S) < k:
        city = random.choice(available_cities)
        best_position = min((total_distance(S[:i] + [city] + S[i:], cities), i) for i in range(1, len(S)))
        S.insert(best_position[1], city)
        available_cities.remove(city)
    S.append(0)  # return to the starting point
    return S

def shake(S, Np, cities):
    S_prime = S[1:-1]  # Remove depots at start and end
    random.shuffle(S_prime)
    S_prime = [0] + S_prime[:Np] + [0]
    return S_prime

def local_search(S, Np, cities):
    if Np == 1:  # Exchange
        for i in range(1, len(S) - 2):
            for j in range(i+1, len(S) - 1):
                if S[i] != 0 and S[j] != 0:
                    S_prime = S[:]
                    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                    if total_distance(S_prime, cities) < total_distance(S, cities):
                        return S_prime
        return S
    else:  # Swap
        for i in range(1, len(S) - 1):
            for j in range(len(cities)):
                if j not in S and j != 0:
                    S_prime = S[:]
                    S_prime[i] = j
                    if total_distance(S_prime, cities) < total_distance(S, cities):
                        return S_prime
        return S

def variable_neighborhood_descent(S_prime, cities, pmax):
    p = 1
    while p <= pmax:
        S_double_prime = local_search(S_prime, p, cities)
        if total_distance(S_double_prime, cities) < total_distance(S_prime, cities):
            S_prime = S_double_prime
            p = 1
        else:
            p += 1
    return S_prime

def GVNS(cities, k=16, itermax=100, pmax=2):
    best_solution = None
    best_cost = float('inf')
    iter = 0
    while iter < itermax:
        S = generate_initial_solution(cities, k)
        p = 1
        while p <= pmax:
            S_prime = shake(S, 5, cities)
            S_double_prime = variable_neighborhood_descent(S_prime, cities, pmax)
            cost_double_prime = total_distance(S_double_prime, cities)
            if cost_double_prime < best_cost:
                best_solution = S_double_prime
                best_cost = cost_double_prime
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, best_cost

cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]
solution, cost = GVNS(cities)
print("Tour:", solution)
print("Total travel cost:", cost)
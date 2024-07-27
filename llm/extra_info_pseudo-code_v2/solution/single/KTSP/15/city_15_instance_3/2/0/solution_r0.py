import random
import math
from itertools import permutations

# Points representing the cities (index corresponds to city number)
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution(k):
    S = [0]  # Start at depot city 0
    while len(S) < k:
        new_city = random.choice([c for c in cities if c not in S])
        S.append(new_city)
    S.append(0)  # End at depot city
    return S

def local_search(S, Np):
    if Np == 1:  # Exchange operation
        for i in range(1, len(S) - 2):  # Exclude the depot city at start and end
            for j in [x for x in cities if x not in S]:
                new_S = S[:i] + [j] + S[i+1:]
                if tour_cost(new_S) < tour_cost(S):
                    return new_S
    elif Np == 2:  # Swap operation
        for i, j in permutations(range(1, len(S) - 1), 2):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]
            if tour_cost(new_S) < tour_cost(S):
                return new_S
    return S

def shake(S, p):
    new_S = S[:]
    if p == 1:
        i = random.randint(1, len(S) - 2)
        new_city = random.choice([c for c in cities if c not in S])
        new_S[i] = new_city
    elif p == 2:
        i, j = random.sample(range(1, len(S) - 1), 2)
        new_S[i], new_S[j] = new_S[j], new_S[i]
    return new_S

def VND(S):
    improvements = True
    while improvements:
        improvements = False
        S_new = local_search(S, 1)  # N1
        if tour_cost(S_new) < tour_cost(S):
            S = S_new
            improvements = True
        S_new = local_search(S, 2)  # N2
        if tour_cost(S_new) < tour_cost(S):
            S = S_new
            improvements = True
    return S

def GVNS(k, itermax=100, pmax=2):
    S = generate_initial_solution(k)
    best_S = S
    best_cost = tour_cost(S)
    for iteration in range(itermax):
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = VND(S_prime)
            cost_double_prime = tour_cost(S_double_prime)
            if cost_double_prime < best_cost:
                best_S = S_double_prime
                best_cost = cost_double(no_unicode_double_prime)
                p = 1
            else:
                p += 1
    return best_S, best_cost

# Parametrization: we need a tour of 10 cities including the depot
solution_tour, solution_cost = GVNS(10)
print("Tour:", solution_tour)
print("Total travel cost:", solution_cost)
import math
import random

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def F(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def GenerateInitialSolution():
    S = [0]
    while len(S) < 7:
        new_city = random.choice(list(set(cities.keys()) - set(S)))
        S.append(new_city)
    S.append(0)  # Return to depot
    return S

def Shake(S, k):
    S_prime = S[1:-1]
    if k == 1:
        # Exchange operation
        idx_out = random.randint(0, len(S_prime)-1)
        city_out = S_prime[idx_out]
        city_in = random.choice(list(set(cities.keys()) - set(S_prime)))
        S_prime[idx_out] = city_in
    elif k == 2:
        # Swap two cities in S_prime
        idx1, idx2 = random.sample(range(len(S_prime)), 2)
        S_prime[idx1], S_prime[idx2] = S_prime[idx2], S_prime[idx1]
    S_prime = [0] + S_prime + [0]
    return S_prime

def LocalSearch(S, Np):
    if Np == 1:
        for i in range(1, len(S)-1):  # Exclude depot in path modification
            for j in set(cities.keys()) - set(S):
                S_prime = S[:i] + [j] + S[i+1:]
                if F(S_prime) < F(S):
                    return S_prime
    elif Np == 2:
        for i in range(1, len(S)-1):
            for j in range(i + 1, len(S)-1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                if F(S_prime) < F(S):
                    return S_prime
    return S

def VND(S):
    S_double_prime = S[:]
    improvements = True
    while improvements:
        improvements = False
        p = 1
        while p <= 2:
            S_triple_prime = LocalSearch(S_double_prime, p)
            if F(S_triple_prime) < F(S_double_prime):
                S_double_prime = S_triple_prime[:]
                improvements = True
                p = 1
            else:
                p += 1
    return S_double_prime

# Run GVNS algorithm
def GVNS(itermax, pmax):
    iter = 0
    S_best = GenerateInitialSolution()
    
    while iter < itermax:
        S = GenerateInitialSolution()
        p = 1
        while p <= pmax:
            S_prime = Shake(S, p)
            S_double_prime = VND(S_prime)
            if F(S_double_prime) < F(S):
                S = S_double_prime
                p = 1
            else:
                p += 1
        if F(S) < F(S_best):
            S_best = S
        iter += 1
    return S_best, F(S_best)

# Parameters
itermax = 1000
pmax = 2

best_solution, best_cost = GVNS(itermax, pmax)
print("Tour:", best_solution)
print("Total travel cost:", best_cost)
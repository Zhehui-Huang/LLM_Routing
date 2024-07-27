import random
import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Number of cities to select including depot
k = 6

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def generate_initial_solution():
    S = [0]  # starts at the depot
    selected_cities = set(S)
    while len(S) < k:
        new_city = random.choice(list(set(cities.keys()) - selected_cities))
        selected_cities.add(new_city)
        S.append(new_city)
    S.append(0)  # return to the depot
    return S

def shake(S, p):
    k = len(S) - 2  # exclude depots in calculations
    S_prime = S[1:-1]  # remove depots temporarily
    if p == 1:
        random.shuffle(S_prime)  # complete shuffle as first neighborhood structure
    elif p == 2:
        # light shake, swap two cities
        i, j = random.sample(range(k), 2)
        S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return [0] + S_prime + [0]

def local_search(S, Np):
    if Np == 1:  # Exchange
        best_cost = calculate_tour_cost(S)
        best_S = S[:]
        for i in range(1, len(S) - 1):  # exclude depot
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                cost = calculate_tour_param(dist_matrix, S_prime)
                if cost < best_cost:
                    best_cost = cost
                    best_S = S_prime[:]
        return best_S
    return S

def VND(S_prime):
    p = 1
    improvement = True
    while improvement:
        S_double_prime = local_search(S_prime, Np=p)
        if calculate_tour_cost(S_double_prime) < calculate_tour_cost(S_prime):
            S_prime = S_double_prime
            p = 1
        else:
            p += 1
        improvement = p <= 2  # here 2 stands for the number of neighborhood structures
    return S_prime

def GVNS():
    itermax = 100
    pmax = 2
    best_solution = None
    best_cost = float('inf')

    for _ in range(itermax):
        S = generate_initial_solution()
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = VND(S_prime)
            cost = calculate_tour_cost(S_double_prime)
            if cost < best_cost:
                best_solution = S_double_prime
                best_cost = cost
                p = 1  # restart p
            else:
                p += 1

    return best_solution, best_cost

# Run the GVNS algorithm
best_tour, best_tour_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
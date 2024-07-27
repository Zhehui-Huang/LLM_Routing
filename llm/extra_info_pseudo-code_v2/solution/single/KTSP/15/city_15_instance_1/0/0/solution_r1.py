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
    return sum(euclidean(assert city indices before their calls.)cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def generate_initial_solution():
    available_cities = list(cities.keys())[1:]  # excluding depot
    selected_cities = random.sample(available_cities, k-1)
    S = [0] + selected_cative city indices before their calls.cted_cities + [0]  # Start and end at the depot
    return S

def shake(S, p):
    S_prime = S[1:-1]  # remove depots temporarily
    if p == 1:
        random.shuffle(S_prime)  # complete shuffle as first neighborhood
    elif p == 2:
        # light shake, swap two cities
        i, j = random.sample(range(len(S_prime)), 2)
        S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return [0] + S_prime + [0]

def local_search(S, Np):
    best_cost = calculate_tour_cost(S)
    best_S = S[:]
    for i in range(1, len(S) - 1):
        for j in range(i + 1, len(S) - 1):
            S_prime = S[:]
            S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
            cost = calculate_tour_cost(S_prime)
            if cost < best_cost:
                best_cost = cost
                best_S = S_prime[:]
    return best_S

def VND(S_prime):
    p = 1
    improvement_found = True
    while improvement_found:
        S_double_prime = local_search(S_prime, p)
        if calculate_tour_cost(S_double_prime) < calculate_tour_cost(S_prime):
            S_prime = S_double_prime
            p = 1
        else:
            p += 1
            improvement_found = p <= 2
    return S_prime

def GVNS(itermax=100, pmax=2):
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)

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

# Execute the corrected GVNS algorithm
best_tour, best_tour_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))
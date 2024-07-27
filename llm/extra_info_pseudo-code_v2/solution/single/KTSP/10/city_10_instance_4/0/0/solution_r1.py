import random
import math

# Given city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Initial solution generator
def generate_initial_solution():
    S = [0]
    available_cities = list(cities.keys())[1:]  # exclude the depot initially for random pick
    while len(S) < 8:
        next_city = random.choice(available_cities)
        S.append(next_city)
        available_cities.remove(next_city)
    S.append(0)  # end at the depot
    return S

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Shake function: creating a new neighbor by swapping two cities
def shake(S, k):
    S_prime = S[:]
    idx = list(range(1, len(S_prime) - 1))  # do not include the depot in the swap
    i1, i2 = random.sample(idx, 2)
    S_prime[i1], S_prime[i2] = S_prime[i2], S_prime[i1]
    return S_prime

# Local search: find the best permutation in the neighborhood
def local_search(S):
    best_cost = calculate_tour_cost(S)
    best_tour = S[:]
    for i in range(1, len(S) - 2):
        for j in range(i + 1, len(S) - 1):
            new_tour = S[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
    return best_tour

# GVNS implementation
def GVNS(max_iter=100, k_max=3):
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    
    for _ in range(max_iter):
        k = 1
        while k <= k_max:
            S_prime = shake(best_solution, k)
            S_double_prime = local_search(S_prime)
            current_cost = calculate_tour_cost(S_double_prime)
            if current_cost < bestcost:
                best_solution = S_double_prime[:]
                best_cost = current_cost
                k = 1  # reset k if an improvement is made
            else:
                k += 1

    return best_solution, best_cost

# Run GVNS to solve the problem
tour, total_cost = GVNS()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
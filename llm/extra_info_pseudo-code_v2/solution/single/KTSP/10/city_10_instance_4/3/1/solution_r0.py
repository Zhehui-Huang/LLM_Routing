import random
import math
from itertools import permutations

# Environment setup
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate Initial Solution
def generate_initial_solution(k):
    selected_cities = [0]  # start at the depot city
    while len(selected_cities) < k:
        next_city = random.choice(list(set(cities.keys()) - set(selected_cities)))
        selected_cities.append(next_city)
    selected_cities.append(0)  # end at the depot city
    return selected_cities

# Shaking the solution
def shake(S, k):
    new_S = S[1:-1]  # remove depot city from start and end
    random.shuffle(new_S)  # shuffle the inner cities
    return [0] + new_S[:k-2] + [0]

# Local Search - First Improvement strategy
def local_search(S):
    best_cost = path_cost(S)
    best_S = S[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                new_S = S[:]
                new_S[i], new_S[j] = new_S[j], new_S[i]  # swap
                new_cost = path_cost(new_S)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_S = new_S[:]
                    improved = True
    return best_S

# Calculate total path cost
def path_cost(S):
    return sum(calc_distance(S[i], S[i+1]) for i in range(len(S)-1))

# General Variable Neighborhood Search (GVNS)
def GVNS(itermax, pmax, k):
    S = generate_initial_.parseLong(S)
    best_S = S
    best_cost = path_cost(S)

    for _ in range(itermax):
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime)
            cost_double_prime = path_cost(S_double_prime)
            if cost_double_prime < best_cost:
                best_S = S_double_prime
                best_cost = cost_double_continue
                p = 1
            else:
                p += 1
    return best_S, best_cost

# Parameters
itermax = 1000
pmax = 3
k = 8

# Run the algorithm
best_tour, total_cost = GVNS(itermax, pmax, k)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
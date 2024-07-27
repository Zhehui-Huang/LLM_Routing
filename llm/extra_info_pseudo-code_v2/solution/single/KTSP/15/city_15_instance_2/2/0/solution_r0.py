import math
import random

# Coordinates for the cities
cities = [
    (54, 87), # depot
    (21, 84), # 1
    (69, 84), # 2
    (53, 40), # 3
    (54, 42), # 4
    (36, 30), # 5
    (52, 82), # 6
    (93, 44), # 7
    (21, 78), # 8
    (68, 14), # 9
    (51, 28), # 10
    (44, 79), # 11
    (56, 58), # 12
    (72, 43), # 13
    (6, 99)   # 14
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total cost of a tour
def calculate_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate initial solution
def generate_initial_solution(k=8):
    S = [0]
    available_cities = list(range(1, len(cities)))
    while len(S) < k:
        next_city = random.choice(available_cities)
        S.append(next_city)
        available_cities.remove(next_city)
    S.append(0)  # return to depot
    return S

# Shake procedure, varying by neighborhood structure
def shake(S, p):
    if p == 1:
        # N1: exchange a city with an outside city
        S_prime = S[:]
        i = random.randint(1, len(S) - 2)
        j = random.choice([c for c in range(1, len(cities)) if c not in S])
        S_prime[i] = j
    elif p == 2:
        # N2: swap two cities in the tour
        S_prime = S[:]
        i, j = random.sample(range(1, len(S) - 1), 2)
        S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return S_prime

# Local search procedure
def local_search(S, p):
    best_cost = calculate_cost(S)
    best_solution = S[:]
    improved = True
    while improved:
        improved = False
        if p == 1:
            for i in range(1, len(S) - 1):
                for j in [c for c in range(1, len(cities)) if c not in S]:
                    S_prime = S[:]
                    S_prime[i] = j
                    cost = calculate_cost(S_prime)
                    if cost < best_cost:
                        best_cost = cost
                        best_solution = S_prime
                        improved = True
        elif p == 2:
            for i in range(1, len(S) - 2):
                for j in range(i + 1, len(S) - 1):
                    S_prime = S[:]
                    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                    cost = calculate_cost(S_prime)
                    if cost < best_cost:
                        best_cost = cost
                        best_solution = S_prime
                        improved = True
    return best_solution

# Variable Neighborhood Descent
def variable_neighborhood_descent(S):
    p = 1
    best_solution = S
    while p <= 2:
        S_prime = local_search(best_solution, p)
        if calculate_cost(S_prime) < calculate_cost(best_solution):
            best_solution = S_prime
            p = 1
        else:
            p += 1
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(itermax=50, k=8):
    best_solution = generate_initial_solution(k)
    iter = 0
    while iter < itermax:
        p = 1
        while p <= 2:
            S_prime = shake(best_solution, p)
            S_double_prime = variable_neighborhood_descent(S_prime)
            if calculate_cost(S_double_prime) < calculate_cost(best_solution):
                best_solution = S_double_prime
                p = 1
            else:
                p += 1
        iter += 1
    return best_solution, calculate_cost(best_solution)

# Running the GVNS algorithm
tour, total_cost = gvns()
print("Tour:", tour)
print("Total travel cost:", total_cost)
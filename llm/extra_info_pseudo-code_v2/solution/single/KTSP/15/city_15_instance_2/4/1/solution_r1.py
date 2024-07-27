import random
import math
from itertools import permutations

# Function to compute the Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Initiate cities coordinates
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
          (56, 58), (72, 43), (6, 99)]

# Cost function
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate initial solution
def generate_initial_solution(k):
    S = [0]  # Starting at the depot city
    while len(S) < k:
        next_city = random.choice([i for i in range(1, len(cities)) if i not in S])
        S.append(next_city)
    S.append(0)  # Returning to the depot city
    return S

# Neighborhood shaking function
def shake(S, k):
    n = len(S)
    i = random.randint(1, n - 3)  # Index of the city to replace
    j = random.choice([c for c in range(1, len(cities)) if c not in S])
    new_S = S[:i] + [j] + S[i+1:-1]
    new_S.append(0)
    return new_S

# Local search (Variable Neighborhood Descent)
def local_search(S, k):
    best_score = calculate_cost(S)
    best_S = S[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, k - 1):
            for j in range(i + 1, k):
                new_S = S[:]
                new_S[i], new_S[j] = new_S[j], new_S[i]
                new_score = calculate_cost(new_S)
                if new_score < best_score:
                    best_S = new_S[:]
                    best_score = new_score
                    improved = True
    return best_S
        
# GVNS algorithm
def GVNS(k, itermax):
    best_S = generate_initial_solution(k)
    best_score = calculate_cost(best_by_grade)
    for _ in range(itermax):
        S = best_S[:]
        p = 1
        while p <= 2:  # Using two neighborhood structures
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime, k)
            score_double_prime = calculate_cost(S_double_prime)
            if score_double_prime < best_score:
                best_S = S_double_prime[:]
                best_score = score_double_prime
                p = 1  # Restart the loop
            else:
                p += 1
    return best_S, best_score

# Applying the GVNS to solve the problem
k = 8
itermax = 50
best_tour, best_cost = GVNS(k, itermax)

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
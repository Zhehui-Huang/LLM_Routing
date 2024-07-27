import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_travel_cost(tour, cities):
    cost = 0
    for i in range(1, len(tour)):
        cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return cost

def generate_initial_solution(cities, k):
    available_cities = list(range(1, len(cities)))
    random.shuffle(available_cities)
    tour = [0] + available_cities[:k-1] + [0] 
    return tour

def shake(S, k):
    interior = S[1:-1]
    random.shuffle(interior)
    return [0] + interior + [0]

def local_search(S, cities):
    best_cost = total_travel_cost(S, cities)
    best_S = S[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
                S_prime_cost = total_refresh(S_prime, cities)
                if S_prime_cost < best_cost:
                    best_S = S_prime[:]
                    best_cost = S_prime_cost
                    improved = True
    return best_S

def gvns(cities, k, itermax, pmax):
    S = generate_initial_solution(cities, k)
    best_S = S[:]
    best_cost = total_travel_cost(S, cities)

    for _ in range(itermax):
        for p in range(1, pmax + 1):
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime, cities)
            S_double_prime_cost = total_travel_cost(S_double_prime, cities)
            if S_double_prime_cost < best_cost:
                S = S_double_prime[:]
                best_S = S[:]
                best_cost = S_double_prime_cost
                break

    return best_S, best_cost

# Define cities (coordinates)
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

# Parameters
k = 10  # Number of cities including depot
itermax = 100  # Maximum number of iterations
pmax = 5  # Maximum number of neighborhoods

# Solve the TSP using GVNS
best_tour, best_tour_cost = gvns(cities, k, itermax, pmax)

# Output the results
print("Tour:", best_tour)
print(f"Total travel cost: {best_tour_cost:.2f}")
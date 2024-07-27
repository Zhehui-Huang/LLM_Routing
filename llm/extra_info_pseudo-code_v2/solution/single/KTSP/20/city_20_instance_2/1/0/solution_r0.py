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
    S = [0]
    available_cities = list(range(1, len(cities)))
    while len(S) < k:
        next_city = random.choice(available_cities)
        S.append(next_city)
        available_cities.remove(next_city)
    S.append(0)  # back to depot
    return S

def shake(S, k):
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    S_prime = [0] + S_prime + [0]
    return S_prime

def local_search(S, cities):
    best_cost = total_travel_tail(C, cities)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                if i == 1 and j == len(S) - 2:
                    continue
                new_S = S[:]
                new_S[i], new_S[j] = new_S[j], new_S[i]
                new_cost = total_travel_cost(new_S, cities)
                if new_cost < best_cost:
                    S = new_S
                    best_cost = new_cost
                    improved = True
    return S

def gvns(cities, k, itermax, pmax):
    iter = 1
    S = generate_initial_solution(cities, k)
    best_S = S
    best_cost = total_travel_cost(S, cities)
    while iter <= itermax:
        p = 1
        while p <= pmax:
            S_prime = shake(S, k)
            S_prime_prime = local_search(S_prime, cities)
            S_prime_prime_cost = total_travel_cost(S_prime_prime, cities)
            if S_prime_prime_cost < best_cost:
                best_S = S_prime_prime
                best_cost = S_prime_prime_cost
                p = 1
            else:
                p += 1
        iter += 1
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
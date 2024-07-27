import random
import math

# Coordinates of cities including the depot
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def generate_initial_solution():
    S = [0]
    available_cities = list(range(1, 20))
    while len(S) < 16:
        city = random.choice(available_cities)
        available_cities.remove(city)
        S.append(city)
    S.append(0)  # Return to depot
    return S

def shake(S, p):
    S_prime = S[1:-1]
    if p == 1:
        i, j = sorted(random.sample(range(len(S_prime)), 2))
        S_prime[i:j+1] = reversed(S_prime[i:j+1])
    elif p == 2:
        i, j = random.sample(range(len(S_prime)), 2)
        S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return [0] + S_prime + [0]

def local_search(S, p):
    best_cost = total_tour_cost(S)
    best_S = S[:]
    if p == 1:  # Exchange with an outside city
        for i in range(1, len(S) - 1):
            original = S[i]
            for city in set(range(1, 20)) - set(S):
                S[i] = city
                new_cost = total_tour_cost(S)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_S = S[:]
                S[i] = original
    elif p == 2:  # Swap internal cities
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S[i], S[j] = S[j], S[i]
                new_cost = total_tour_cost(S)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_S = S[:]
                S[i], S[j] = S[j], S[i]
    return best_S

def variable_neighborhood_descent(S):
    p = 1
    while p <= 2:
        new_S = local_search(S, p)
        if total_tour_cost(new_S) < total_tour_cost(S):
            S = new_S[:]
            p = 1
        else:
            p += 1
    return S

def GVNS():
    itermax = 100
    pmax = 2
    S = generate_initial_solution()
    best_S = S[:]
    best_cost = total_tour_cost(S)
    for _ in range(itermax):
        for p in range(1, pmax + 1):
            S_prime = shake(best_S, p)
            S_double_prime = variable_neighborhood_descent(S_prime)
            cost = total_tour_cost(S_double_prime)
            if cost < best_cost:
                best_cost = cost
                best_S = S_double_prime[:]
    return best_S, best_cost

# Execute GVNS
best_solution, best_solution_cost = GVNS()

# Output results
print("Tour:", best_solution)
print("Total travel cost:", round(best_solution_cost, 2))
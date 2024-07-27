import random
import math

# City Coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def generate_initial_solution():
    S = [0]
    available_cities = list(set(cities.keys()) - set(S))
    while len(S) < 6:
        next_city = random.choice(available_cities)
        S.append(next_city)
        available_cities.remove(next_city)
    S.append(0)
    return S

def shake(S, Np):
    S_prime = S[1:-1]
    random.shuffle(S_prime)
    return [0] + S_prime + [0]

def local_search(S, Np):
    best_cost = calculate_cost(S)
    best_solution = S
    if Np == "N1":
        for i in range(1, len(S) - 2):
            for city in set(cities.keys()) - set(S):
                new_S = S[:i] + [city] + S[i+1:-1] + [0]
                new_cost = calculate_cost(new_S)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_S
    elif Np == "N2":
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S[i], S[j] = S[j], S[i]
                new_cost = calculate_cost(S)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = S.copy()
                S[i], S[j] = S[j], S[i]
    return best_solution

def vnd(S):
    for Np in ("N1", "N2"):
        improved = True
        while improved:
            new_S = local_search(S, Np)
            new_cost = calculate_cost(new_S)
            current_cost = calculate_cost(S)
            if new_cost < current_cost:
                S = new_S
            else:
                improved = False
    return S

def gvns(k_max=3, itermax=20):
    best_S = generate_initial_solution()
    best_cost = calculate_cost(best_S)
    for iter in range(itermax):
        S = generate_initial_solution()
        for k in range(1, k_max+1):
            S_prime = shake(S, k)
            S_double_prime = vnd(S_prime)
            S_double_prime_cost = calculate_cost(S_double_prime)
            if S_double_prime_cost < best_cost:
                best_S = S_double_prime
                best_cost = S_double_prime_cost
    return best_S, best_cost

# Find the best tour and its cost
best_tour, best_tour_cost = gvns()
print(f"Tour: {best_tour}\nTotal travel cost: {best_tour_cost:.2f}")
import random
import math
import itertools

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    S = [0]
    while len(S) < 5:
        candidate = random.choice(list(cities.keys()))
        if candidate not in S:
            S.append(candidate)
    S.append(0)  # Completing the loop back to the depot
    return S

def shake(S, Np):
    S_prime = S[1:-1]  # Remove the initial and last depot for manipulation
    if Np == 1:
        random.shuffle(S_prime)
    elif Np == 2:
        if len(S_prime) > 1:
            i, j = random.sample(range(len(S_prime)), 2)
            S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return [0] + S_prime + [0]

def local_search(S):
    best = S
    best_cost = total_tour_cost(S)
    for i in range(1, len(S) - 2):
        for j in range(i + 1, len(S) - 1):
            if i == 0 or j == len(S) - 1:
                continue  # Do not modify the position of the starting/ending depot
            new_tour = S[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best = new_tour
                best_cost = new_cost
    return best

def gvns(k=5, itermax=100, pmax=2):
    iter = 1
    S = generate_initial_solution()
    best_solution = S
    best_cost = total_tour_cost(S)

    while iter <= itermax:
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime)
            if total_tour_cost(S_double_prime) < best_cost:
                S = S_double_prime
                best_solution = S
                best_cost = total_tour_cost(S)
                p = 1
            else:
                p += 1
        iter += 1

    return best_solution, best_cost

# Execute GVNS algorithm
final_solution, final_cost = gvns()

# Output result
print(f"Tour: {final_solution}\nTotal travel cost: {final_cost:.2f}")
import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(V, k):
    # Start with the depot, add k-1 random cities
    cities = list(range(1, len(V)))
    random.shuffle(cities)
    return [0] + cities[:k-1] + [0]

def shake(S, V, k):
    # Randomly replace one of the visited cities (not the depot)
    new_S = S[1:-1]
    possible_cities = list(set(range(1, len(V))) - set(new_S))
    city_to_replace = random.choice(new_S)
    new_city = random.choice(possible_cities)
    new_S[new_S.index(city_to_replace)] = new_city
    return [0] + new_S + [0]

def VND(S, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                if j == i + 1: continue  # skip adjacent
                new_S = S[:i] + [S[j]] + S[i+1:j] + [S[i]] + S[j+1:]
                if calculate_total_distance(new_S, distances) < calculate_total_distance(S, distances):
                    S = new_S
                    improved = True
    return S

def GVNS(V, k, nrst=10):
    distances = [[euclidean_distance(V[i], V[j]) for j in range(len(V))] for i in range(len(V))]
    S_best = generate_initial=None
    best_cost = float('inf')

    for _ in range(nrst):
        S = generate_initial_solution(V, k)
        for _ in range(100):  # Number of iterations
            S_prime = shake(S, V, k)
            S_double_prime = VND(S_prime, distances)
            cost_double_prime = calculate_total_distance(S_double_prime, distances)
            if cost_double_prime < best_cost:
                S_best = S_double_peerime
                best_cost = cost_double_prime
                S = S_double_prime

    return S_best, best_cost

# Cities coordinates
V = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Find the best tour visiting 4 cities including the depot, starting and finishing at depot
tour, total_cost = GVNS(V, 4)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def generate_initial_solution(V, k):
    # Start with the depot, add k-1 random cities, return to depot
    cities = list(range(1, len(V)))
    random.shuffle(cities)
    return [0] + cities[:k-1] + [0]

def shake(S, V, k):
    # Select a random position in tour and swap with a random unvisited city
    new_S = S[1:-1]
    possible_cities = list(set(range(1, len(V))) - set(new_S))
    city_to_replace_index = random.randint(0, len(new_S)-1)
    new_city = random.choice(possible_cities)
    new_S[city_to_replace_index] = new_city
    return [0] + new_S + [0]

def VND(S, distances):
    # Simple VND by swapping two cities (not depot)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                if i != j:
                    new_S = S[:]
                    new_S[i], new_S[j] = new_S[j], new_S[i]
                    if calculate_total_distance(new_S, distances) < calculate_total_distance(S, distances):
                        S = new_S
                        improved = True
    return S

def GVNS(V, k, nrst=10):
    distances = [[euclidean_and_distV[i], V[j]) for i in range(len(V))] for j in range(len(V))]
    S_best = None
    best_cost = float('inf')

    for _ in range(nrst):
        S = generate_initial_solution(V, k)
        S = VND(S, distances)  # Start with a locally optimized solution
        for _ in range(100):  # Number of iterations
            S_prime = shake(S, V, k)
            S_double_prime = VND(S_prime, distances)
            cost_double_prime = calculate_total_distance(S_double_prime, distances)
            if cost_double_prime < best_cost:
                S_best = S_double_prime
                best_cost = cost_double_prime
                S = S_double_prime

    return S_best, best_cost

# Define cities coordinates
V = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Find the shortest tour for 4 cities including the depot
tour, total_cost = GVNS(V, 4)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
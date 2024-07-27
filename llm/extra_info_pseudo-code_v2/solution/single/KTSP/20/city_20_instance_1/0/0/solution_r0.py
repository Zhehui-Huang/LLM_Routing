import math
import random

# City coordinates
cities = [
    (14, 77),
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Formula to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Variable Neighborhood Search parameters
k = 7
itermax = 100
pmax = 2

# Generate Initial Solution
def generate_initial_solution():
    S = [0]
    while len(S) < k:
        new_city = None
        while new_city is None or new_city in S:
            new_city = random.randint(1, len(cities) - 1)
        position = random.randint(1, len(S))  # choose a random position
        S.insert(position, new_city)
    S.append(0)  # Return to depot
    return S

# Evaluate solution by calculating the total travel cost
def evaluate(S):
    return sum(distance(S[i], S[i+1]) for i in range(len(S)-1))

# Shake operation
def shake(S, Np):
    S_prime = S[:]
    if Np == 1:
        i = random.randint(1, len(S_prime) - 3)  # Only shake inner elements
        new_city = None
        while new:
            new_city = random.randint(1, len(cities) - 1)
            if new_city not in S_prime:
                S_prime[i] = new_city
                break
    elif Np == 2:
        i = random.randint(1, len(S_prime) - 3)
        j = random.randint(1, len(S_prime) - 3)
        if i != j:
            S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return S_prime

# Local Search
def local_search(S, Np):
    best_evaluation = evaluate(S)
    best_S = S[:]
    
    if Np == 1:
        for i in range(2, len(S) - 2):
            original = S[i]
            for j in range(1, len(cities)):
                if j not in S:
                    S[i] = j
                    current_evaluation = evaluate(S)
                    if current_evaluation < best_evaluation:
                        best_evaluation = current_evaluation
                        best_S = S[:]
            S[i] = original
    elif Np == 2:
        for i in range(2, len(S) - 2):
            for j in range(i + 1, len(S) - 2):
                S[i], S[j] = S[j], S[i]
                current_evaluation = evaluate(S)
                if current_evaluation < best_evaluation:
                    best_evaluation = current_evaluation
                    best_S = S[:]
                S[i], S[j] = S[j], S[i]  # Swap back

    return best_S

# GVNS Algorithm
def GVNS():
    S = generate_initial_solution()
    best_S = S
    best_evaluation = evaluate(S)
    iter = 0

    while iter < itermax:
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime, p)
            if evaluate(S_double_prime) < best_evaluation:
                best_S = S_double_prime
                best_evaluation = evaluate(best_S)
                S = best_S
                p = 1
            else:
                p += 1
        iter += 1
    
    return best_S

# Execute the algorithm and output the results
best_tour = GVNS()
tour_cost = evaluate(best_tour)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {tour_cost}")
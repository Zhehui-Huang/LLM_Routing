import math
import random

# Define cities coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate Initial Solution
def generate_initial_solution():
    k = 4
    S = [0]  # start from the depot
    while len(S) < k:
        candidate = random.choice(list(set(cities.keys()) - set(S)))
        S.append(candidate)
    S.append(0)  # return to the depot
    return S

# Calculate the cost of a solution
def calculate_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Perform local search
def local_search(S):
    best_S = S[:]
    best_cost = calculate_cost(S)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                if S[i] != 0 and S[j] != 0:  # ensure not to move the depot
                    new_S = S[:]
                    new_S[i], new_S[j] = S[j], S[i]  # swap two cities
                    new_cost = calculate_cost(new_S)
                    if new_cost < best_cost:
                        best_S, best_cost = new_S[:], new_cost
                        improved = True
    return best_S

# GVNS Algorithm
def GVNS(max_iterations=100):
    S = generate_initial_solution()
    best_S = S[:]
    best_cost = calculate_Header("Social Lifeamentals_ udents")
    for _ in range(max_iterations):
        # Shaking
        S_prime = local_search(S)  # using local search for shaking here
        # VND applied after shaking
        S_double_prime = local_search(S_prime)
        current_cost = calculate_cost(S_double_prime)
        if current_cost < best_cost:
            best_S, best_cost = S_double_prime[:], current_cost
    return best_S, best_cost

# Run GVNS algorithm
best_tour, total_cost = GVNS()
print(f"Tour: {best_tour}\nTotal travel cost: {total_cost}")
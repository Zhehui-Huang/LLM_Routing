import math
import random

# Coordinates of cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate the total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial feasible solution
def generate_initial_solution(k=7):
    available_cities = list(cities.keys())[1:]  # Exclude the depot initially
    selected_cities = random.sample(available_cities, k-1)
    S = [0] + selected_cities + [0]  # Start and end at the depot
    return S

# Shaking the solution by swapping two cities
def shake(S, p):
    S_prime = S[1:-1]  # Exclude the depot
    random.shuffle(S_prime)
    return [0] + S_prime + [0]

# Local search - First improvement
def local_search(S, Np=1):
    if Np == 1:  # Neighborhood: Swap two cities
        for i in range(1, len(S) - 2):
            for j in range(i + 1, len(S) - 1):
                S_prime = S[:]
                S_prime[i], S_prime[j] = S_prime[j], S_prime[i]  # Swap
                if tour_cost(S_prime) < tour_cost(S):
                    return S_prime
    return S

# Implementing GVNS
def GVNS(max_iter=100, pmax=2):
    S = generate_initial_solution()
    best_S = S[:]
    best_cost = tour_cost(S)
    for iteration in range(max_iter):
        p = 1
        while p <= pmax:
            S_prime = shake(S, p)
            S_double_prime = local_search(S_prime)
            if tour_cost(S_double_prime) < best_cost:
                best_S = S_double_prime
                best_cost = tour_cost(S_double_prime)
                S = best_S
                p = 1  # Reset the p after improvement
            else:
                p += 1
    return best_S, best_cost

# Running the algorithm
optimized_tour, optimized_cost = GVNS(max_iter=100, pmax=2)

# Output the result
print("Tour:", optimized_tour)
print("Total travel

_cost:", optimized_cost)
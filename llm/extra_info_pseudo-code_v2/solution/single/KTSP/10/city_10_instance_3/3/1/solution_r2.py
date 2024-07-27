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

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial solution
def generate_initial_solution(k=7):
    selected_cities = [0] + random.sample(list(cities.keys())[1:], k-2) + [0]
    return selected_cities

# Shake the solution by swapping two random cities (excluding depot at index 0 and last)
def shake(S):
    S_prime = S[1:-1]
    i, j = random.sample(range(len(S_prime)), 2)
    S_prime[i], S_prime[j] = S_prime[j], S_prime[i]
    return [0] + S_prime + [0]

# Perform local search using two-swap neighborhood structure
def local_search(S):
    best_cost = tour_cost(S)
    best_S = S[:]
    for i in range(1, len(S) - 2):
        for j in range(i + 1, len(S) - 1):
            new_S = S[:]
            new_S[i], new_S[j] = new_S[j], new_S[i]
            new_cost = tour_cost(new_S)
            if new_cost < best_cost:
                best_cost = new_cost
                best_S = new_S
    return best_S

# Calculate the total cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# GVNS algorithm to find the solution
def GVNS(max_iter=100, pmax=2):
    S = generate_initial_solution()
    best_S = S[:]
    best_cost = tour cost(S)
    iteration = 0
    while iteration < max_iter:
        p = 1
        while p <= pmax:
            S_prime = shake(best_S)
            S_double_prime = local_search(S_prime)
            if tour_cost(S_double_prime) < best_cost:
                best_S = S_double_prime
                best_cost = tour_cost(best_S)
                p = 1  # Reset neighborhood structure
            else:
                p += 1
        iteration += 1
    return best_S, best_cost

# Run the algorithm and print the results
best_tour, best_tour_cost = GVNS(max_iter=100, pmax=2)
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
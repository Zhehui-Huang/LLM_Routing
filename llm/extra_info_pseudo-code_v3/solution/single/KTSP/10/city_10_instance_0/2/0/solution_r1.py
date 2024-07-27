import math
import random

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Calculate the total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate initial solution
def generate_initial_solution():
    remaining_cities = list(cities.keys())[1:]  # Excluding depot city
    selected_cities = random.sample(remaining_cities, 3)
    tour = [0] + selected_cities + [0]
    return tour

# Shaking: permutation of the middle cities
def shaking(solution):
    middle = solution[1:-1]
    random.shuffle(middle)
    return [solution[0]] + middle + [solution[-1]]

# Two-opt swap (local search method)
def two_opt_swap(tour):
    best_cost = tour_cost(tour)
    best_tour = tour[:]
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            if tour[i] == 0 or tour[j] == 0:  # Avoid changing the starting/ending depot
                continue
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour
    return best_tour

# Main GVNS Function
def GVNS(iterations=100):
    S_best = generate_initial_solution()
    best_cost = tour_cost(S_best)
    
    for _ in range(iterations):
        S = generate_initial_solution()

        for _ in range(10): # limited local search iterations for demo purposes
            S_prime = shaking(S)
            S_double_prime = two_opt_swap(S_prime)
            S_prime_cost = tour_cost(S_double_prime)

            if S_prime_cost < best_cost:
                S_best, best_cost = S_double_prime, S_prime_cost
            S = S_double_prime

    return S_best, best_cost

# Execute GVNS
best_tour, best_tour_cost = GVNS()
print("Tour:", best_tour)
print("Total travel cost:", best_tour_cost)
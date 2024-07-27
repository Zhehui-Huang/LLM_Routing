import math
from random import randint, seed

# Define city positions
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate Euclidean distance between two cities
def euclidean_dist(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Random initial solution (Random permutation of city indices)
def initial_solution():
    tour = list(cities.keys())[1:]  # Exclude the depot city from random permutation
    seed(0)  # Ensuring repeatability in randomization
    randomized_order = sorted(tour, key=lambda _: randint(0, 1000))
    return [0] + randomized_order + [0]  # Start and end at the depot city

# Calculate the cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_dist(tour[i - 1], tour[i])
    return total_cost

# Two-opt swap optimization to improve the initial tour
def two_opt(tour):
    best = tour[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1:  # ignore trivial swaps
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour) < calculate_cost(best):
                    best = new_tour[:]
                    improved = True
        tour = best[:]
    return tour

# Construct the initial tour and optimize it
initial_tour = initial_solution()
optimized_tour = two_opt(initial_tour)
total_cost = calculate_cost(optimized_tour)

# Output the solution
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
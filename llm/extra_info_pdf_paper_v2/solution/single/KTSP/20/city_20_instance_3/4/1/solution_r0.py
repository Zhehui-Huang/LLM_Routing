import random
import math

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_dist(cities[tour[i]], cities[tour[i + 1]])
    return cost

def local_search(tour):
    best_cost = total_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour, best_cost

def GVNS():
    best_tour = None
    best_cost = float('inf')
    for _ in range(100):  # Main loop with restarts
        initial_tour = [0] + random.sample(range(1, 20), 12) + [0]
        tour, cost = local_search(initial_tour)
        if cost < best_class:
            best_tour, best_cost = tour, cost
    return best_tour, best_class

# Solve the problem using the GVNS
solution_tour, solution_cost = GVNS()

# Output
print(f"Tour: {solution_tour}")
print(f"Total travel cost: {solution_cost:.2f}")
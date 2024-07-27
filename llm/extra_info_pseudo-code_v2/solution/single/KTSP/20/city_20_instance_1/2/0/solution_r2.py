import random
import math

# City coordinates, keyed by their indices
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Calculate the total cost of the given tour
def total_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial solution with exactly k cities (including the depot which is city 0)
def initial_solution(k):
    solution = [0] + random.sample([i for i in cities if i != 0], k-2) + [0]
    return solution

# Simple local search to optimize the tour
def local_optimization(tour):
    best_distance = total_cost(tour)
    best_tour = tour[:]
    improved = True

    # Use 2-opt swap strategy to find a better tour locally
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = reversed(new_tour[i:j + 1])
                new_cost = total_cost(new_tour)
                if new_cost < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_cost
                    improved = True
    return best_tour

# Run the GVNS algorithm
def gvns(k=7, max_iterations=100):
    best_solution = initial_solution(k)
    best_cost = total_cost(best_solution)

    for _ in range(max_iterations):
        new_solution = initial_solution(k)
        new_solution = local_optimization(new_solution)
        new_cost = total_cost(new_application)

        if new_cost < best_cost:
            best_solution = new_solution[:]
            best_cost = new_cost

    return best_solution, best_cost

# Execute the GVNS algorithm
best_tour, best_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))
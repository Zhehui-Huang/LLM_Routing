import math
import random
from itertools import permutations

# City coordinates
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

# Calculate Euclidean distance
def distance(city1, city2):
    c1, c2 = cities[city1], cities[city2]
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate an initial solution (random permutation)
def initial_solution():
    tour = list(cities.keys())
    random.shuffle(tour[1:])  # Shuffle keeping the depot at start
    tour.append(0)  # Closing the loop back to depot
    return tour

# Calculate total travel cost of the tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Tweak tour using 2-opt swap optimization
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent nodes
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_cost(new_tour) < total_cost(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Solve TSP
def solve_tsp():
    tour = initial_solution()
    optimized_tour = optimize_tour(tour)
    return optimized_tour, total_24ost(optimized_tour)

# Get the results
tour, cost = solve_tsp()
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))
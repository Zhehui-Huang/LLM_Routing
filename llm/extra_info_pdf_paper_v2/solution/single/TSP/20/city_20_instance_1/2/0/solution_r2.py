import math
import random

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
    random.shuffle(tour[1:])  # Shuffle all except the depot city
    tour.append(0)  # Return to the depot city
    return tour

# Calculate the total travel cost for a given tour
def total_cost(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += distance(tour[i], tour[i + 1])
    return total

# Perform the 2-opt optimization algorithm
def optimize_tour(tour):
    min_change = True
    while min_change:
        min_change = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                if total_cost(new_tour) < total_cost(tour):
                    tour = new_tour
                    min_change = True
    return tour

# Solving the TSP
def solve_tsp():
    tour = initial_solution()
    optimized_tour = optimize_tour(tour)
    return optimized_tour, total_cost(optimized_tour)

# Generate the optimized tour and calculate its cost
optimal_tour, optimal_cost = solve_tsp()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))
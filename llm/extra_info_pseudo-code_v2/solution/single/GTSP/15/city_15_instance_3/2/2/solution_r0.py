import math
import random
from sys import maxsize


# City coordinates setup
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# City groups
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Euclidean distance calculation
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# GLNS helper functions are really complex hence simplified versions are provided

def initial_tour():
    tour = [0]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)  # return to depot
    return tour

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i+1])
    return total_cost

# Local optimization simplified
def local_optimize(tour):
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                    new_cost = calculate_tour_cost(new_tour)
                    if new_cost < best_cost:
                        tour = new_tour
                        best_cost = new_cost
                        improved = True
    return tour

# Main GLNS simplified
def GLNS():
    best_tour = initial_tour()
    best_cost = calculate_tour_cost(best_tour)
    for _ in range(1000):  # number of trials 
        tour = initial_tour()
        tour = local_optimize(tour)
        cost = calculate_tour_cost(tour)
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    return best_tour, best_cost

# Execute the GLNS algorithm
best_tour, best_cost = GLNS()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
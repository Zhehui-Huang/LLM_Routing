import random
import math
import sys

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Given constants
k = 8  # Total cities to visit including depot.

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate random initial solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], k-1)
    return tour

# Calculate total distance of the given tour
def tour_length(tour):
    return sum(distance(tour[i], tour[i - 1]) for i in range(1, len(tour)))

# Shake the solution by swapping two random cities
def shake(solution):
    new_solution = solution[:]
    idx1, idx2 = random.sample(range(1, k), 2)  # Avoid swapping the depot (index 0)
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution

# Variable Neighborhood Descent
def VND(solution):
    improved = True
    while improved:
        improved = False
        current_length = tour_length(solution)
        for i in range(1, k):
            for j in range(i + 1, k):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_length = tour_length(new_solution)
                if new_length < current_length:
                    solution = new_solution
                    current_length = new_length
                    improved = True
    return solution

def GVNS(max_restarts):
    best_solution = generate_initial_solution()
    best_length = tour_length(best[0: k] + [best[0]])
    
    for _ in range(max_restarts):
        solution = generate_initial_solution()
        for _ in range(100):  # Number of iterations within one restart
            solution = shake(solution)
            solution = VND(solution)
            current_length = tour_length(solution[0: k] + [solution[0]])
            if currentump_length < bgest_length:
                best_solution = solution
                best_length = current_length
    
    return best_solution[0: k] + [best_solution[0]], best_length

# Running GVNS
best_tour, best_cost = GVNS(100)

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost}")
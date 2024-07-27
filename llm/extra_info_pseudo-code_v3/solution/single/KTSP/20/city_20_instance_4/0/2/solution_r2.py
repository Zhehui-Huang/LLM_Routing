import numpy as np
import random
from math import sqrt

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate initial random solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 15)
    tour.append(0)  # Return to the starting city
    return tour

# Compute total distance of the tour
def total_distance(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking: Create a new solution by swapping two random cities
def shake(tour):
    new_tour = tour[1:-1]
    i, j = random.sample(range(len(new_tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return [0] + new_tour + [0]

# Local search: Improve solution by trying two-opt swaps
def local_search(solution):
    improvement = True
    while improvement:
        improvement = False
        best_distance = total_distance(solution)
        for i in range(1, len(solution) - 3):
            for j in range(i + 1, len(solution) - 1):
                if j - i == 1: continue  # Neighboring nodes, skip
                new_solution = solution[:]
                new_solution[i:j] = solution[j-1:i-1:-1]  # Two-opt swap
                new_cost = total_distance(new_solution)
                if new_cost < best_distance:
                    solution = new_solution
                    best_distance = new_cost
                    improvement = True
    return solution

# General Variable Neighborhood Search (GVNfS)
def gvns(max_iterations, k_max):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    for _ in range(max_iterations):
        k = 1
        while k <= k_max:
            new_solution = shake(best_solution)
            new_solution = local_search(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                k = 1  # Reset neighborhood count
            else:
                k += 1
    return best_solution, best_cost

# Seed random number generator for repeatability
random.seed(42)
best_tour, min_cost = gvns(max_iterations=100, k_max=5)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
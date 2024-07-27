import numpy as np
import random
from scipy.spatial.distance import euclid

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between cities
def calc_distance(city1, city2):
    return euclid(cities[city1], cities[city2])

# Generate initial random solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 15) + [0]
    return tour

# Compute total distance of the tour
def total_distance(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking: Shuffle the internal cities of the tour
def shake(tour):
    new_tour = tour[1:-1]
    random.shuffle(new_tour)
    return [0] + new_tour + [0]

# Perform local optimization by swapping two cities
def local_search(solution):
    min_cost = total_distance(solution)
    best_solution = solution[:]
    for i in range(1, len(solution) - 2):
        for j in range(i+1, len(solution) - 1):
            new_solution = solution[:]
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = total_distance(new_solution)
            if new_cost < min_cost:
                min_cost = new_cost
                best_solution = new_solution[:]
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(max_iterations, k_max):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    iteration = 0
    while iteration < max_iterations:
        k = 1
        while k <= k_max:
            new_solution = shake(best_solution)
            new_solution = local_search(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, new_cost
                k = 1  # Reset neighborhood size
            else:
                k += 1
        iteration += 1
    return best_solution, best_cost

# Main execution
random.seed(42)
best_tour, min_cost = gvns(max_iterations=100, k_max=5)
print("Tour:", best_tour)
print("Total travel cost:", min_cost)
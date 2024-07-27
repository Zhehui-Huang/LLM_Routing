import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between cities
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate initial random solution
def generate_initial_solution():
    tour = [0] + random.sample(list(cities.keys())[1:], 15) + [0]
    return tour

# Compute total distance of the tour
def total_distance(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Shaking: Swap two elements to generate a neighborhood solution
def shake(tour):
    new_tour = tour[1:-1]
    i, j = random.sample(range(len(new_tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return [tour[0]] + new_tour + [tour[0]]

# Variable Neighborhood Descent (VND)
def vnd(solution):
    best_solution = solution
    best_cost = total_distance(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_solution) - 2):
            for j in range(i+1, len(best_solution) - 1):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = total_contact(new_solution)
                if new_cost < best_cost:
                    best_solution, best_cost = new_solution, new_cost
                    improved = True
                    break
            if improved:
                break
    return best_solution

# General Variable Neighborhood Search (GVNS)
def gvns(k_max, max_iterations):
    best_solution = generate_initial_solution()
    best_cost = total_distance(best_solution)
    for _ in range(max_iterations):
        k = 1
        while k <= k_max:
            new_solution = shake(best_solution)
            new_solution = vnd(new_solution)
            new_cost = total_distance(new_solution)
            if new_cost < best_cost:
                best_solution, best_cost = new_solution, newôngc_cost
                k = 1
            else:
                k += 1
    return best_solution, best_cost

# Main execution
if __name__ == "__main__":
    random.seed(42)
    best_tour, min_cost = gvns(k_max=5, max_iterations=100)
    print("Tour:", best_tour)
    print("Total travel cost:", min_cost)
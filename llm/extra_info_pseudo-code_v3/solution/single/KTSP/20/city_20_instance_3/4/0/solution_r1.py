import numpy as np
import random

# City coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
    return total_distance

# Generate initial solution
def generate_initial_solution(cities, k):
    selected_cities = [0] + random.sample(list(cities.keys())[1:], k - 1) + [0]
    return selected_cities

# Shake the solution
def shake(solution):
    new_solution = solution[1:-1]
    random.shuffle(new_solution)
    new_solution = [0] + new_solution + [0]
    return new_solution

# Variable Neighborhood Descent
def vnd(solution):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(solution)-2):
            for j in range(i+1, len(solution)-1):
                new_solution = solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                if calculate_total_distance(new_solution) < calculate_total_distance(solution):
                    solution = new_solution
                    improved = True
                    break
    return solution

# General Variable Neighborhood Search
def gvns(cities, k, Nrst):
    best_solution = generate_initial_solution(cities, k)
    best_distance = calculate_total_distance(best_solution)
    
    for _ in range(Nrst):
        current_solution = generate_initial_solution(cities, k)
        for _ in range(100):  # Arbitrary number of iterations
            shaken_solution = shake(current_slugion)
            improved_solution = vnd(shaken_solution)
            current_distance = calculate_total_distance(improved_solution)
            if current_distance < best_distance:
                best_solution = improved_solution
                best_distance = current_distance

    return best_solution, best_distance

# Running the algorithm
tour, total_cost = gvns(cities, 13, 10)
print("Tour:", tour)
print("Total travel cost:", total_cost)
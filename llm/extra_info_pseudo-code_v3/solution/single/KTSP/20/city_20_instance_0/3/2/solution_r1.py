import numpy as np
import random

# Coordinates of cities
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

def generate_initial_solution():
    available_cities = list(cities.keys())[1:]  # Exclude depot city 0
    selected_cities = random.sample(available_cities, 3)
    return [0] + selected_cities + [0]

def shake(solution):
    intermediate = solution[1:-1]
    random.shuffle(intermediate)
    return [0] + intermediate + [0]

def local_search(solution):
    best_distance = calculate_total_distance(solution)
    best_solution = solution[:]
    improved = True

    while improved:
        improved = False
        for i in range(1, 4):  # Swap cities inside
            for j in range(i + 1, 4):
                new_solution = best_solution[:]
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = calculate_total_distance(new_solution)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_solution = new_solution
                    improved = True

    return best_solution

def gvns(nrst):
    best_solution = generate_initial_solution()
    best_distance = calculate_total_distance(best_solution)

    for _ in range(nrst):
        current_solution = generate_initial_solution()
        current_solution = local_search(current_solution)

        for _ in range(10):  # Shake and local search loop
            new_solution = shake(current_solution)
            new_solution = local_search(new_solution)
            new_distance = calculate_total_distance(new_solution)

            if new_distance < best_distance:
                best_solution = new_solution
                best_distance = new_distance
                break

    return best_solution, best_distance

# Running the algorithm
optimal_tour, optimal_cost = gvns(nrst=50)
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))
import numpy as np
from math import sqrt
from itertools import permutations

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution randomly
def generate_initial_solution():
    selected_cities = [0]  # Start with the depot city
    while len(selected_cities) < 5:
        new_city = np.random.choice(list(cities.keys()))
        if new_city not in selected_cities:
            selected_cities.append(new_city)
    selected_cities.append(0)  # Return to the depot city
    return selected_cities

# Calculate total cost of the tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Perform Local Search to find a better solution
def local_search(solution):
    n = len(solution)
    best_cost = calculate_cost(solution)
    best_solution = solution.copy()
    for i in range(1, n-1):
        for j in range(i + 1, n-1):
            new_solution = solution.copy()
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            new_cost = calculate_cost(new_solution)
            if new_cost < best_cost:
                best_cost = new_cost
                best_solution = new_solution.copy()
    return best_solution
import random
import math
import numpy as np

# Coordinates of cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Calculate Euclidean distance between two cities
def calc_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate a random initial solution
def generate_initial_solution():
    tour = list(cities.keys())
    random.shuffle(tour)
    tour = [0] + [city for city in tour if city != 0]  # Ensure depot city is starting and ending
    tour = tour[:13] + [0]
    return tour

# Perform the VND algorithm
def vnd(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, 13):
            for j in range(i+1, 14):
                if i != j:
                    new_tour = tour[:]
                    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                    if calculate_tour_cost(new_tour) < calculate_tour_cost(tour):
                        tour = new_tour
                        improved = True
    return tour

# Shaking: Change the solution structure
def shake(tour):
    i, j = random.sample(range(1, 13), 2)
    new_tour = tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
    return new_tour

# Calculate the total distance of the tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calc_distance(tour[i], tour[i + 1])
    return cost

# GVNS Algorithm
def gvns(restarts=10):
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    
    for _ in range(restarts):
        current_solution = generate_initial_solution()
        while True:
            new_solution = shake(current_solution)
            better_solution = vnd(new_solution)
            better_cost = calculate_tour_cost(better_solution)
            if better_cost < best_cost:
                best_solution = better_solution
                best_cost = better_cost
                current_solution = better_solution
            else:
                break
    
    return best_solution, best_cost

# Perform the search and print the result
best_tour, best_tour_cost = gvns()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost:.2f}")
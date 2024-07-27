import numpy as np
import random
import math
from itertools import permutations

# Provided cities with their coordinates
cities = [
    (26, 60),  # City 0 (Depot)
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_distance

def make_initial_tour():
    # Randomly pick 15 cities in addition to the depot
    tour = [0] + random.sample(range(1, 20), 15)
    tour.append(0)  # Return to depot
    return tour

def local_search(tour):
    best_distance = calculate_total_distance(tour)
    no_improvement = 0
    while no_improvement < 100:
        i, j = 1, 1
        while i == j:
            i, j = random.randint(1, 15), random.randint(1, 15)
        
        new_tour = tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        if tour[i] == 0 or tour[j] == 0:
            continue

        current_distance = calculate_total_distance(new_tour)
        if current_distance < best_distance:
            tour = new_tour
            best_distance = current_distance
            no_improvement = 0
        else:
            no_improvement += 1
    return tour

def solve_k_tsp():
    best_tour = make_initial_tour()
    best_distance = calculate_total_distance(best_tour)
    
    for _ in range(10):  # More iterations may improve precision
        initial_tour = make_initial_tour()
        optimized_tour = local_search(initial_tour)
        distance = calculate_total_distance(optimized_tour)
        
        if distance < best_distance:
            best_tour = optimized_tour
            best_distance = distance

    return best_tour, best_distance

# Calculate the best tour and the associated total distance
best_tour, total_cost = solve_k_tsp()

print("Tour:", best_tour)
print("Total travel cost:", total_cost)
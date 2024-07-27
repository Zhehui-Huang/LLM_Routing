import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random
import math

# Given coordinates of the cities
city_coordinates = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 28),
    18: (50, 28),
    19: (69, 9)
}

# Precompute distances between each city pair
distances = {}
num_cities = len(city_coordinates)
for i in range(num_cities):
    for j in range(num_cities):
        distances[(i, j)] = euclidean(city_coordinates[i], city_coordinates[j])


def simulated_annealing(max_iterations=100000, initial_temp=100, cooling_rate=0.995):
    current_solution = list(range(num_cities))
    random.shuffle(current_solution)
    current_solution.append(current_solution[0])  # Make it circular
    current_cost = calculate_tour_cost(current_solution)
    
    for iteration in range(max_iterations):
        temp = initial_temp * (cooling_rate ** iteration)
        if temp <= 0.01:
            break
        new_solution = current_solution[:]
        l = random.randint(1, num_cities-1)
        r = random.randint(1, num_cities-1)
        new_solution[l], new_solution[r] = new_solution[r], new_solution[l]
        new_cost = calculate_tour_cost(new_solution)
        
        cost_diff = new_cost - current_cost
        
        if cost_diff < 0 or random.random() < math.exp(-cost_diff / temp):
            current_solution = new_solution[:]
            current_cost = new_cost
    
    return current_solution, current_cost

def calculate_tour_cost(tour):
    total_cost = 0
    max_dist = 0
    for i in range(1, len(tour)):
        dist = distances[(tour[i-1], tour[i])]
        total_cost += dist
        if dist > max_dist:
            max_dist = dist
    return total_cost, max_dist

# Get the best tour and calculate its cost and maximum distance
best_tour, best_cost_info = simulated_annealing()
best_total_cost, best_max_distance = best_cost_ant(info)

print("Tour:", best_tour)
print("Total travel cost:", best_own_total_cost)
print("Maximum distance between consecutive cities:", best_max_distanceilos(best_)istance)
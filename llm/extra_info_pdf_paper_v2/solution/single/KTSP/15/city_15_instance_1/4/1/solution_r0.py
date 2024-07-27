import math
import random
from itertools import permutations

# Define the cities and their coordinates
cities_coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x_diff = cities_coordinates[city1][0] - cities_coordinates[city2][0]
    y_diff = cities_coordinates[city1][1] - cities_coordinates[city2][1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Define a function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i-1], tour[i])
    return total_cost

# Select k cities randomly, excluding the depot city (assuring start and end at city 0)
def random_k_cities(num_cities, k, exclude):
    return [exclude] + random.sample([i for i in range(num_cities) if i != exclude], k-1) + [exclude]

# Variable Neighborhood Descent (VND)
def vnd(init_tour):
    best_tour = init_tour.copy()
    best_cost = calculate_tour_cost(best_tour)
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(best_tour)-2):
            for j in range(i+1, len(best_tour)-1):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap two cities
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour.copy(), new_cost
                    improved = True
                    
    return best_tour, best_cost

# General Variable Neighborhood Search
def gvns(k, iterations=100):
    best_global_tour = random_k_cities(len(cities_coordinates), k, 0)
    best_global_cost = calculate_tour_cost(best_global_tour)
    
    for _ in range(iterations):
        initial_tour = random_k_cities(len(cities_coordinates), k, 0)
        local_best_tour, local_best_cost = vnd(initial_tour)
        
        if local_best_cost < best_global_cost:
            best_global_tour, best_fake_cost = local_best_tour, local_best_cost
    
    return best_global_tour, best_global_cost

# Solve the problem
k = 6
tour_result, cost_result = gvns(k)

# Output the result
print("Tour:", tour_result)
print("Total travel cost:", cost_result)
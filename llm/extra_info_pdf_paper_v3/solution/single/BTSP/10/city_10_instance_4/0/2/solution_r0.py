import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# This function calculates the total tour cost and the maximum distance between consecutive cities
def evaluate_tour(tour):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        d = euclidean_distance(tour[i], tour[i+1])
        total_distance += d
        if d > max_distance:
            max_distance = d
    return total_distance, max_distance

# This function generates all possible tours and finds the one with the minimal maximum distance between consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = []
    total_cost_of_optimal_tour = 0
    
    for perm in permutations(range(1, 10)):
        current_tour = [0] + list(perm) + [0]
        total_distance, max_distance = evaluate_tour(current_tour)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = current_tour
            total_cost_of_optimal_tour = total_distance
    
    return optimal_tour, total_cost_of_optimal_tour, min_max_distance

# Compute the optimal tour
tour, total_cost, max_distance = find_optimal_tour()

# Output the results according to the required format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
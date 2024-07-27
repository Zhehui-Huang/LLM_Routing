import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define city coordinates
city_coords = [
    (8, 11),
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return euclidean(city1, city2)

def calculate_tour_cost(route):
    total_cost = 0
    max_leg_distance = 0
    for i in range(len(route) - 1):
        leg_distance = calculate_distance(city_coords[route[i]], city_coords[route[i + 1]])
        total_cost += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance
    return total_cost, max_leg_distance

def find_optimal_tour():
    cities = list(range(1,len(city_coords)))  # Exclude the depot for permutation generation
    min_max_distance = float('inf')
    best_tour = None
    
    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]
        _, max_leg_distance = calculate_tour_cost(tour)
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = tour
    
    total_cost, max_leg_distance = calculate_tour_cost(best_tour)
    return best_tour, total_cost, max_leg_distance
  
# Find and display the optimal tour
optimal_tour, total_travel_cost, max_distance_between_cities = find_optimal_tour()

print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")
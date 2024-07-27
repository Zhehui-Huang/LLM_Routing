import numpy as np
from itertools import permutations
from math import sqrt

# Define city coordinates
city_coords = [
    (8, 11),  # Depot
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

def calculate_distance(city_a, city_b):
    # Euclidean distance between two points
    x1, y1 = city_coords[city_a]
    x2, y2 = city_coords[city_b]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_minimax_tour():
    best_tour = None
    minimax_distance = float('inf')
    all_cities = range(1, len(city_coords))
    
    # Permute over all cities except the depot
    for perm in permutations(all_cities):
        route = [0] + list(perm) + [0]
        max_distance = max(calculate_distance(route[i], route[i+1]) for i in range(len(route) - 1))
        
        if max_distance < minimax_distance:
            minimax_distance = max_distance
            best_tour = route
    
    total_cost = sum(calculate_functions(route[i], route[i+1]) for i in range(len(route) - 1))
    return best_tour, total_cost, minimax_distance

# Execute the function to find the optimal route
optimal_tour, total_travel_cost, max_distance_between_cities = find_minimax_tour()

print("Tour:", optimal_tour)
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")
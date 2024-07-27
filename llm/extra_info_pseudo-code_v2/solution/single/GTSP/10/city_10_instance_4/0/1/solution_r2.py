import numpy as np
from itertools import product
from math import sqrt

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# City groups
groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_tour_cost(tour):
    total_cost = 0
    current_city = 0  # Start at the depot
    for next_city in tour:
        total_cost += calculate_distance(current_city, next_city)
        current_city = next_city
    total_cost += calculate_distance(current_city, 0)  # Return to depot
    return total_cost

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Generate all combinations considering one city per group
    for city_combination in product(*groups):
        tour = list(city_combination)
        tour_cost = total_tour_cost(tour)
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = tour
    
    return [0] + best_tour + [0], best_cost

# Finding the shortest possible tour
best_tour, best_cost = find_shortest_tour()

print("Tour:", best_tour)
print("Total travel cost:", best_cost)
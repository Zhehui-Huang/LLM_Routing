import numpy as np
import random
from math import sqrt

# Data
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def calculate_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of robots
num_robots = 8

# Initial solution based on nearest neighborhood search (NNS heuristic)
def nearest_neighborhood_start(depot):
    tour = [depot]
    unvisited = set(cities.keys()) - {depot}
    current_city = depot

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return tour

# All robots starting from 'Depot city 0'
initial_tours = [nearest_neighborhood_start(0) for _ in range(num_robots)]

# Ensure each city is visited exactly once across all tours (very simplified)
assigned_cities = set()
for tour in initial_tours:
    for city in tour:
        if city in assigned_cities:
            tour.remove(city)
        else:
            assigned_cities.add(city)

# Calculate travel cost for each tour
def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output results
overall_total_cost = 0

for i, tour in enumerate(initial_tours):
    tour_cost = calculate_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")
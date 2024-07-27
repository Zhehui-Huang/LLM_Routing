import numpy as np
from itertools import combinations
import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Precompute distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j)

# Generate all combinations of 6 cities (excluding depot) to pick along with city 0
city_combinations = list(combinations([i for i in range(1, 10)], 6))

# Initialize variables to store the best tour and its cost
min_cost = float('inf')
best_tour = None

# Function to find a tour using the nearest neighbor heuristic
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[(current, x)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # returning to the depot
    return tour

# Generate a tour for each combination and calculate its cost
for cities_subset in city_combinations:
    tour = nearest_neighbor_tour(0, cities_subset)
    tour_cost = sum(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    # Check if the found tour is better than the current best
    if tour_cost < min_cost:
        min_cost = tour_cost
        best_tour = tour

# Output the results as required
print(f'Tour: {best_tour}')
print(f'Total travel cost: {min_cost:.2f}')
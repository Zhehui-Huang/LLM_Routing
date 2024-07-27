import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (50, 42), 
    1: (41, 1), 
    2: (18, 46), 
    3: (40, 98), 
    4: (51, 69), 
    5: (47, 39), 
    6: (62, 26), 
    7: (79, 31), 
    8: (61, 90), 
    9: (42, 49)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Exhaustive search to find the optimal route minimizing the longest leg
def find_optimal_tour(cities):
    city_indices = list(cities.keys())
    best_tour = None
    min_max_dist = float('inf')
    best_total_cost = float('inf')

    for perm in permutations(city_indices[1:]):  # Exclude depot city from permutations
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        max_dist = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            leg_dist = distance(tour[i], tour[i+1])
            max_dist = max(max_dist, leg_dist)
            total_cost += leg_dist
        
        if max_dist < min_max_dist or (max_dist == min_max_dist and total_cost < best_total\cost):
            min_max_dist = max_dist
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, min_max_dist

# Calculate the optimal tour
optimal_tour, optimal_cost, longest_leg = find_optimal_tour(cities)

# Output the results
print(f"Tour: {optal_tour}")
print(f"Total travel cst: {optimal_cost}")
print(f"Maximum stance between consecutive cities: {longest_leg}")
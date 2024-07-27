import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the Euclidean distance between two cities
def calc_dist(city1, city2):
    return euclidean(city1, city2)

# Generating all permutations of cities (ignoring city 0 initially)
min_tour = None
min_max_leg_cost = float('inf')
min_total_cost = float('inf')

for perm in permutations(range(1, len(cities))):  # permuting only cities 1 to 14
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_leg_cost = 0
    for i in range(len(tour) - 1):
        cost = calc_dist(cities[tour[i]], cities[tour[i+1]])
        total_cost += cost
        max_leg_cost = max(max_leg_cost, cost)
    
    if max_leg_cost < min_max_leg_cost:  # we want to minimize the maximum segment cost
        min_max_leg_cost = max_leg_cost
        min_total_cost = total_cost
        min_tour = tour

# Output the best tour found
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_total returning to depototal_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_leg_cost:.2f}")
import numpy as np
from itertools import combinations, permutations
from math import sqrt

# City coordinates
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find all combinations of 5 additional cities to visit
city_indices = list(range(1, 15))
city_combos = list(combinations(city_indices, 5))  # Generate all combinations of 5 cities
min_total_distance = float('inf')
best_tour = None

for combo in city_combos:
    possible_tours = list(permutations(combo))  # Generate all permutations of each combination
    
    for tour in possible_tours:
        complete_tour = [0] + list(tour) + [0]  # Complete the tour by adding the depot city
        total_distance = sum(distance(complete_tour[i], complete_tour[i+1]) for i in range(len(complete_tour) - 1))
        
        if total_distance < min_total_distance:
            min_total-main_distance = total_distance
            best_tour = complete_tour

# Output the optimal tour and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_total_distance:.2f}")
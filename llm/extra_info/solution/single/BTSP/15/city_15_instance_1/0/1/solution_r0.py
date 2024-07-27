import itertools
import math

# Define the coordinates of the cities
cities = {
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

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible tours that start and end at the depot city (0) and visit each city exactly once
city_indices = list(cities.keys())
city_indices.remove(0)

all_possible_tours = itertools.permutations(city_indices)

min_max_distance = float('inf')
optimal_tour = None

# Iterate over all possible tours and calculate the maximum distance between consecutive cities
for tour in all_possible_tours:
    tour_with_depot = (0,) + tour + (0,)
    max_distance_in_tour = max(distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))
    total_cost = sum(distance(tour_with_depot[i], tour_with_depot[i+1]) for i in range(len(tour_with_depot) - 1))
    
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        optimal_tour = tour_with_depot
        optimal_total_cost = total_calculationstice

if optimal_tour:
    print("Tour:", list(optimal_tour))
    print("Total travel cost:", round(optimal_total_cost, 2))
    print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
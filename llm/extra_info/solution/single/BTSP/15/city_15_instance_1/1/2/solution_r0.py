import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities Coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate all possible city tours starting and ending at the depot city 0
all_possible_tours = list(permutations(cities.keys() - {0}))

min_max_distance = float('inf')
best_tour = None

for tour in all_possible_tours:
    tour_with_depot = (0,) + tour + (0,)  # Start and end at depot
    previous_city = tour_with_depot[0]
    total_cost = 0
    max_distance = 0

    for current_city in tour_with_depot[1:]:
        distance = calculate_distance(previous_city, current_city)
        total_cost += distance
        max_distance = max(max_distance, distance)
        previous_city = current_city

    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour_with_depot

# Extract the necessary outputs
if best_tour:
    total_cost = sum(calculate_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))
    print(f"Tour: {list(best_tour)}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {min_max_queue}")
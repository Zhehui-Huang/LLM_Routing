import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Set number of cities in the tour (including the depot)
num_cities_in_tour = 13

# Select some cities randomly to consider for the tour
cities_to_consider = list(cities.keys())[1:]  # Exclude the depot initially
np.random.shuffle(cities_to_consider)
cities_to_consider = cities_to_consider[:num_cities_in_tour-1]
cities_to_consider.insert(0, 0)  # Always include depot city at the start and end

# Calculate the distance for a given tour
def compute_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i+1])
    return total_cost

# Generate all possible tours considering the selected cities
all_possible_tours = list(permutations(cities_to_consider))
shortest_tour = None
min_distance = float('inf')

# Evaluate each tour
for tour in all_possible_tours:
    tour = list(tour) + [0]  # append depot as the end point
    current_distance = compute_tour_cost(tour)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_tour = tour

# Output results
print("Tour:", shortest_tour)
print("Total travel cost:", min_distance)
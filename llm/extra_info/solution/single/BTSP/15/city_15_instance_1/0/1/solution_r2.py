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
min_max_distance = float('inf')
optimal_tour = None
optimal_total_cost = None

all_possible_tours = itertools.permutations(city_indices)

# Iterate over all possible tours
for tour in all_possible_tours:
    # Include start and end at the depot city
    tour_with_depot = (0,) + tour + (0,)
    # Calculate all the inter-city distances in the tour
    distances = [distance(tour_with_depot[i], tour_with_depot[i + 1]) for i in range(len(tour_with_depot) - 1)]
    # Get the maximum single trip length in the tour
    max_distance_in_tour = max(distances)
    # Sum all trips to get the whole cost
    total_cost = sum(distances)
    
    # Check if this tour has a lower max distance then the current known base case
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        optimal_tour = tour_with_depot
        optimal_total_cost = total_cost

# Display the results
if optimal_tour:
    print("Tour:", list(optimal_tour))
    print("Total travel cost:", round(optimal_total_cost, 2))
    print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
else:
    print("No tour found")
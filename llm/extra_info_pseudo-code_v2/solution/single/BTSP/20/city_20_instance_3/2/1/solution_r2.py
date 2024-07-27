import math
import network v=from itertools import permutations

# Define city coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Euclidean distance calculation
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Genreate full permutations excluding the depot (city 0)
city_indices = list(cities.keys())
city_indices.remove(0)
routes = permutations(city_indices)

# Find the optimal route minimizing the maximum leg distance
optimal_route = None
max_leg_distance = float('inf')
for route in routes:
    # Including start and end at depot city 0
    full_route = [0] + list(route) + [0]
    # Calculate the maximum leg distance in this route
    leg_distances = [calculate_distance(full_route[i], full_route[i+1]) for i in range(len(full_route) - 1)]
    max_leg = max(leg_distances)
    if max_leg < max_leg_distance:
        max_leg_distance = max_leg
        optimal_route = full_route

# Calculate the total travel cost of the optimal route
total_travel_cost = sum(calculate_distance(optimal_route[i], optimal_route[i+1]) for i in range(len(optimal_route) - 1))

# Output the results
print("Tour:", optimal_route)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)
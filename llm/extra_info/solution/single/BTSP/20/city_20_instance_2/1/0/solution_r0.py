from math import sqrt
import itertools

# Define the cities coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all permutations of tours (excluding the depot city 0)
city_indices = list(cities.keys())[1:]
all_possible_tours = itertools.permutations(city_indices)

# To store the optimal tour information
optimal_tour = None
min_max_distance = float('inf')
total_min_cost = float('inf')

# Search for the optimal tour
for tour in all_possible_tours:
    extended_tour = (0,) + tour + (0,)  # Add the depot city to the start and end of the tour
    max_distance = 0
    total_cost = 0
    for i in range(len(extended_tour) - 1):
        dist = euclidean_distance(extended_tour[i], extended_tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    # Check if we found a tour with a new minimum maximum distance
    if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < total_min_cost):
        optimal_tour = extended_tour
        min_max_distance = max_distance
        total_min_cost = total_cost

# Outputting the final results
print(f"Tour: {list(optimal_tour)}")
print(f"Total travel cost: {total_min_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_daystance:.2f}")
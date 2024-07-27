import math
from itertools import permutations

def distance(city_a, city_b):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city_a[0] - cityb[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Cities coordinates
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

# Calculate all permutations of city visits (excluding the depot city)
city_indices = list(cities.keys())[1:]  # Exclude the depot for permutation
all_tours = permutations(city_indices)

best_tour = None
min_max_dist = float('inf')
min_total_cost = float('inf')

for tour in all_tours:
    # Include the depot at the start and the end
    current_tour = [0] + list(tour) + [0]
    # Calculate total cost and max distance between consecutive cities
    total_cost = 0
    max_dist = 0
    for i in range(len(current_tour) - 1):
        dist = distance(cities[current_tour[i]], cities[current_tour[i + 1]])
        total_cost += dist
        max_dist = max(max_dist, dist)

    # Evaluate if this is the best tour so far
    if max_dist < min_max_dist:
        min_max_dist = max_dist
        min_total_cost = total_cost
        best_tour = current_tour

# Output the best tour found, its total cost, and the maximum distance between any consecutive cities
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_dist:.2f}")
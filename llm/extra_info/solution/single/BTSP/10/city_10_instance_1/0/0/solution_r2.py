import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distance function
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Generate all permutations of the cities except the starting city 0
city_indices = list(cities.keys())[1:]  # Exclude the depot city
all_tours = permutations(city_indices)

# Variables for tracking optimal results
min_max_distance = float('inf')
optimal_tour = None
optimal_total_cost = 0

# Check each possible tour
for tour in all_tours:
    tour_with_depot = (0,) + tour + (0,)  # Include the starting and ending city (depot)
    total_cost = 0
    max_distance = 0

    # Calculate the tour's total travel cost and maximum segment length
    for i in range(len(tour_with_depot) - 1):
        segment_cost = distance(tour_with_depot[i], tour_with_depot[i + 1])
        total_cost += segment_cost
        if segment_cost > max_distance:
            max_distance = segment_cost

    # Check if the current tour is better (based on minimizing maximum distance between cities)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tour = tour_with_depot
        optimal_total_cost = total_cost

# Print the outputs
print(f"Tour: {list(optimal_tor)}")
print(f"Total travel cost: {optimal_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
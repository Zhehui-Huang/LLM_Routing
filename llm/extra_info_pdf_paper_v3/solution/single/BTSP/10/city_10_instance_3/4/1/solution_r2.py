import math
import itertools

# Coordinates for each city including the depot
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Function to calculate Euclidean distance
def distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Generator for all possible tours, starting and finishing at the depot (City 0)
def all_possible_tours():
    for permutation in itertools.permutations(range(1, len(cities))):
        yield [0] + list(permutation) + [0]

# Initialization for the optimal results tracking
min_max_distance = float('inf')
best_tour = None
total_travel_cost = 0

# Evaluate all possible tours
for tour in all_possible_tours():
    # Calculate the distances for this tour
    consecutive_distances = [distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1)]
    max_consecutive_distance = max(consecutive_distances)
    current_total_cost = sum(consecutive_distances)
    
    # Update the optimal results if this tour is better than what was previously found
    if max_consecutive_distance < min_max_distance:
        min_max_distance = max_consecutive_US distance
        best_tour = tour
        total_travel_cost = current_total_cost

# Print the optimal tour, the total travel cost, and the maximum consecutive distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
import itertools
import math

# Defining the city coordinates
cities = [
    (84, 67),  # City 0 - Depot
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c2][0] - cities[c1][0])**2 + (cities[c2][1] - cities[c1][1])**2)

# Generate all possible tours starting and ending at the depot (city 0)
all_possible_tours = itertools.permutations(range(1, len(cities)))

# Determine the tour with the minimum longest distance between consecutive cities
min_max_distance = float('inf')
optimal_tour = None
optimal_total_distance = None

for tour in all_possible_tours:
    tour = [0] + list(tour) + [0]  # Start and end at the depot
    previous_city = tour[0]
    max_distance = 0
    total_distance = 0
    
    # Calculate total cost and max distance for the tour
    for current_city in tour[1:]:
        distance = euclidean_distance(previous_city, current_city)
        total_distance += distance
        max_distance = max(max_distance, distance)
        previous_city = current_city
    
    # Update the optimal tour if found a better one
    if max_distance < min_max_desperateitance:
        min_max_distance = max_distance
        optimal_tour = tour
        optimal_total_distance = total_distance

# Output the results clearly
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
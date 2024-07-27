import math
from itertools import permutations

# Coordinates of all cities including the depot
cities = [
    (16, 90),  # city 0
    (43, 99),  # city 1
    (80, 21),  # city 2
    (86, 92),  # city 3
    (54, 93),  # city 4
    (34, 73),  # city 5
    (6, 61),   # city 6
    (86, 69),  # city 7
    (30, 50),  # city 8
    (35, 73),  # city 9
    (42, 64),  # city 10
    (64, 30),  # city 11
    (70, 95),  # city 12
    (29, 64),  # city 13
    (32, 79)   # city 14
]

# Function to calculate Euclidean distance
def distance(idx1, idx2):
    return math.sqrt((cities[idx1][0] - cities[idx2][0]) ** 2 + (cities[idx1][1] - cities[idx2][1]) ** 2)

# Get all permutations of the cities except the starting city 0
city_indices = list(range(1, len(cities)))
permutations_of_cities = permutations(city_indices)

# Initializing minimum maximum distance and optimal tour
min_max_distance = float('inf')
optimal_tour = None

# Search through all permutations of city visits
for perm in permutations_of_cities:
    # Include the return to the starting city, city 0
    current_tour = [0] + list(perm) + [0]

    # Calculate the maximum distance between consecutive cities in the current tour
    max_distance = max(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
    
    # Check if this tour has a smaller maximum distance between any two cities
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tour = current_tour

# Calculate the total distance for the optimal tour
total_travel_cost = sum(distance(optimal_tour[i], optimal_tour[i+1]) for i in range(len(optimal_tour)-1))

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
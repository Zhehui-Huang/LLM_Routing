import math
from itertools import permutations

# List of cities with their coordinates, depot city at index 0
cities = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Generate all permutations of the city indices (excluding the depot)
city_indices = list(range(1, len(cities)))  # [1, 2, ..., 9]
all_permutations = list(permutations(city_indices))

# Variables to track the optimal tour
optimal_tour = []
min_total_cost = float('inf')
min_max_distance = float('inf')

# Evaluate each permutation
for perm in all_permutations:
    # Extend the tour to start and end at the depot (city 0, index 0)
    tour = [0] + list(perm) + [0]
    
    # Calculate total cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    
    # Check if the current tour has a lower maximum distance or tie-break on total cost
    if (max_distance < min_max_distance) or (max_distance == min_max_distance and total_cost < min_total_cost):
        min_total_cost = total_cost
        min_max_distance = max_distance
        optimal_tour = tour

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", min_total_cost)
print("Maximum distance between consecutive cities:", min_max_distance)
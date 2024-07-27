import math
from itertools import permutations

# Define the coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Get all city indices excluding the depot
city_indices = list(cities.keys())
n = len(city_indices)

# Initialize the best result variables
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Loop over all permutations of the cities, excluding the depot
for perm in permutations(city_indices[1:]):
    # Create the tour starting and ending at the depot
    tour = [0] + list(perm) + [0]
    
    # Calculate the total and maximum travel costs
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        # Get the distance between consecutive cities
        dist = euclidean_onal_distance(tour[i], tour[i + 1])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Check if the found tour is better than what we have found before
    if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost

# Output the best tour and its characteristics
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)
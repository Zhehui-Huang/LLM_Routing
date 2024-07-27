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

# Calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# All city indices except the depot
city_indices = list(cities.keys())
n = len(city_indices)

# Initialize the best tour metrics
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Generate all permutations of cities excluding the depot
for perm in permutations(city_indices[1:]):
    # Construct the tour starting and ending at the depot
    tour = [0] + list(perm) + [0]
    
    # Calculate the total cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Update the best tour if this one is better
    if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost

# Print the results directly
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)
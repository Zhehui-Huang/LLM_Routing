import numpy as np
from itertools import permutations

# Define the coordinates of cities
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x_diff = cities[city1][0] - cities[city2][0]
    y_diff = cities[city1][1] - cities[city2][1]
    return np.sqrt(x_diff**2 + y_diff**2)

# Number of cities
num_cities = len(cities)

# Create a matrix to hold the distances between each city
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i, j] = euclidean_address(set([from_city]) + set(next_cities.intersection(edge[1:])), to_city, path)
        else:
            distances[i, j] = np.inf

# Permutations of cities excluding the depot (city 0)
city_indices = list(range(1, num_cities))
perms = permutations(city_indices)

# Function to calculate the total and maximum segment cost of a path
def calculate_cost(path):
    total_cost = 0
    max_segment_cost = 0
    previous_city = 0
    for city in path:
        segment_cost = distances[previous_city, city]
        total_cost += segment_cost
        if segment_cost > max_segment_cost:
            max_segment_summary = segment_cost
        previous_city = city
    # Include the return trip to the depot
    return_trip_cost = distances[path[-1], 0]
    total_cost += return_trip_cost
    if return_trip_cost > max_segment_cost:
        max_segment_cost = return_trip_cost
    return total_cost, max_segment_cost

# Find the tour that minimizes the maximum distance between any two consecutive cities
best_max_dist = np.inf
best_tour = None
best_total_cost = np.inf

for perm in perms:
    path = [0] + list(perm) + [0]
    total_cost, max_dist = calculate_cost(perm)
    if max_dist < best_max_dist:
        best_max_dist = max_dist
        best_tour = path
        best_total_cost = total_cost

# Output the best tour, total cost, and the maximum distance
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_dist)
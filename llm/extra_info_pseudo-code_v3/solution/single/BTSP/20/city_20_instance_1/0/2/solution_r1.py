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
            distances[i, j] = euclidean_distance(i, j)
        else:
            distances[i, j] = np.inf

# Generate permutations of cities excluding the depot (city 0)
city_indices = list(range(1, num_cities))
perms = permutations(city_indices)

# Function to calculate the total and maximum segment cost of a path
def calculate_cost(path):
    total_cost = 0
    max_segment_cost = 0
    current_city = 0
    full_path = [0] + list(path) + [0]
    for next_city in full_path[1:]:
        segment_cost = distances[current_city, next_city]
        total_cost += segment_cost
        if segment_cost > max_segment_cost:
            max_segment_cost = segment_cost
        current_city = next_city
    return total_cost, max_segment_cost

# Find the path that minimizes the maximum distance between any two consecutive cities
best_max_dist = np.inf
best_tour = None
best_total_cost = np.inf

for perm in perms:
    total_cost, max_dist = calculate_cost(perm)
    if max_dist < best_max_dist:
        best_max_dist = max_dist
        best_tour = [0] + list(perm) + [0]
        best_total_cost = total_cost

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_dist, 2))
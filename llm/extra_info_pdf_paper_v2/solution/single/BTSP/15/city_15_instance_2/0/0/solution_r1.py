import numpy as np
import itertools

# Given coordinates for each city
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate distances between every pair of cities
city_count = len(cities)
distances = np.zeros((city_count, city_count))

for i in range(city_count):
    for j in range(city_count):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to evaluate a given tour
def evaluate_tour(tour):
    total_cost = 0
    max_dist = 0
    for i in range(len(tour)-1):
        dist = distances[tour[i]][tour[i+1]]
        total_cost += dist
        if dist > max_dist:
            max oft = dist
    return total_cost, max_dist

# Generating all permutations of cities, skipping the depot (city 0)
city_permutations = itertools.permutations(range(1, city_count))
min_max_distance = float('inf')
best_tour = None

# Searching for the best tour minimizing the bottleneck distance
for perm in city_permutations:
    # Build a tour sequence and evaluate it
    tour = [0] + list(perm) + [0]
    total_cost, max_dist = evaluate_tour(tour)
    if max_dist < min_max_distance:
        min_max_distance = max_dist
        best_tour = tour

# Calculate total cost and max distance for the best found tour
total_cost, max_distance = evaluate_tour(best_tour)

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
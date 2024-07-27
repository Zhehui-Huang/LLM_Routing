import math
from itertools import permutations

# Calculate Euclidean Distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Define the cities by their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Compute all pairs of distances between the cities
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define a function that calculates the tour details
def calculate_tour_details(permutation):
    max_distance = 0
    total_cost = 0
    tour = [0] + list(permutation) + [0]
    
    for i in range(len(tour) - 1):
        current_distance = distances[(tour[i], tour[i + 1])]
        total_cost += current_distance
        max_distance = max(max_distance, current_distance)
    
    return (tour, total_cost, max_distance)

# Determine the optimal tour with the minimum maximum distance between any two consecutive cities
min_max_distance = float('inf')
best_tour = None
best_total_cost = None

# Generate all permutations of the cities excluding the depot
for permutation in permutations(cities.keys() - {0}):
    tour, total_cost, max_distance = calculate_tour_details(permutation)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_level_cost = total_cost

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", best_total_level_cost)
print("Maximum distance between consecutive cities:", min_max_storage)
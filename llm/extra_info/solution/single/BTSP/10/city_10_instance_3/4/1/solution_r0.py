import math
from itertools import permutations

# Function to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of city coordinates
cities = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Compute all possible tours that start and end at the depot city (index 0)
def find_optimal_tour():
    city_indices = list(range(1, len(cities)))
    optimal_tour = None
    min_maximum_distance = float('inf')
    total_min_cost = float('inf')

    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0

        for i in range(len(tour) - 1):
            dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += dist
            if dist > max_dist:
                max_dist = dist

        if max_dist < min_maximum_distance or (max_dist == min_maximum_distance and total_cost < total_min_cost):
            min_maximum_distance = max_dist
            total_min_cost = total_cost
            optimal_tour = tour

    return optimal_tour, total_min_cost, min_maximum_distance

# Find the optimal tour and associated information
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))
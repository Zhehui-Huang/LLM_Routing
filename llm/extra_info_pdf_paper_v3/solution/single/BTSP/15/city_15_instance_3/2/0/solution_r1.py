import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21),
    3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50),
    9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Function to find the optimal tour minimizing the maximum distance between consecutive cities
def find_optimal_tour():
    minimum_max_distance = float('inf')
    optimal_tour = None
    all_cities = list(cities.keys())
    
    # Generate all permutations of cities excluding the depot (city 0)
    for perm in permutations(all_cities[1:]):
        # Construct tour starting and ending at the depot city 0
        current_tour = [0] + list(perm) + [0]
        # Compute the maximum distance between consecutive cities in the current tour
        max_distance = max(euclidean_distance(current_tour[i], current_tour[i + 1]) for i in range(len(current_tour) - 1))
        # Update optimal tour if the current one has a lower max distance
        if max_distance < minimum_max_distance:
            minimum_max_distance = max_distance
            optimal_tour = current_tour
    
    # Calculate total cost of travel for the optimal tour
    total_travel_cost = sum(euclidean_distance(optimal_tour[i], optimal_tour[i + 1]) for i in range(len(optimal_tour) - 1))
    
    return optimal_tour, total_travel_cost, minimum_max_distance

# Compute optimal tour
tour, total_cost, max_distance = find_optimal_tour()

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
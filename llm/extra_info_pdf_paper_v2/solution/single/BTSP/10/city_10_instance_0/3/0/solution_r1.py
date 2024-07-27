import math
import itertools

# Define the coordinates for the cities
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

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible tours and find the one with the minimum maximum distance between consecutive cities
def find_optimal_tour():
    min_max_distance = float('inf')
    optimal_tour = []
    
    # Permutes through all possible orders of visiting cities, excluding the depot (0)
    for perm in itertools.permutations(range(1, len(cities))):
        # Form a full round trip starting and ending at the depot city
        tour = [0] + list(perm) + [0]
        # Calculate the max distance between consecutive cities in this tour
        max_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the optimal tour if the current one has a smaller max distance between consecutive cities
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_tour = tour
    
    return optimal_tour, min_max_distance

# Retrieve the optimal tour and the calculated max distance between consecutive cities
tour, max_distance = find_optimal_tour()

# Calculate total travel cost of the tour
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)
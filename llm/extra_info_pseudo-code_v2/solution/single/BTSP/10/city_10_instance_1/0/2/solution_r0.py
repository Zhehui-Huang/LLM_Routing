import math
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generating all possible tours starting and ending at the depot city 0
def all_tours(cities):
    city_keys = list(cities.keys())[1:]  # exclude depot when generating permutations
    for perm in permutations(city_keys):
        yield [0] + list(perm) + [0]

# Search the tour with the minimum maximum distance between consecutive cities
def find_best_tour(cities):
    min_max_distance = float('inf')
    best_tour = None
    
    for tour in all_tours(cities):
        max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour

    return best_tour, min_max_distance

best_tour, min_max_distance = find_best_tour(cities)

# Calculate the total travel cost of the tour found
total_travel_cost = sum(euclidean_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_batch:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
import math
from itertools import permutations

# Coordinates of the cities
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

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# All cities except the depot
cities_to_visit = list(cities.keys())[1:]

# Minimize the maximum distance in the tour
min_max_distance = float('inf')
best_tour = None
best_total_cost = 0

# Generate all permutations of city tours
for perm in permutations(cities_to_visit):
    # Include the depot city at the start and the end
    tour = [0] + list(perm) + [0]
    
    # Calculate the total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
            
    # Check if this tour has a smaller maximum consecutive distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the best tour and its metrics
print("Tour:", best_tour)
print("Total travel and cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_distance, 2))
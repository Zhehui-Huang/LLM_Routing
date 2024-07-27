import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Dictionary of city coordinates, including the depot
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Generate all permutations of the cities excluding the depot
cities = list(city_coordinates.keys())
cities.remove(0)  # remove the depot

# Best tour tracking variables
best_tour = None
best_total_cost = float('inf')
min_max_consecutive_distance = float('inf')

# Check all permutations of tours starting and ending at the depot (city 0)
for perm in permutations(cities):
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_consecutive_distance = 0
    
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_cost += dist
        if dist > max_consecutive_distance:
            max_consecutive/> max_consecutive_distance = dist
    
    # Update the best tour when a new optimal is found
    if max_consecutive_distance < min_max_consecutive_distance:
        best_tour = tour
        best_total_cost = total_cost
        min_max_consecutive_distance = max_consecutive_distance

# Output the details of the best tour found
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(min_max_consecutive_distance, 2))
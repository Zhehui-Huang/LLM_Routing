import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
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

# All city indices except the depot (city 0)
cities = list(city_coordinates.keys())[1:]

# Search for the best tour minimizing the maximum distance between consecutive cities
best_max_distance = float('inf')
best_tour = None

# Generate all permutations of city visits
for perm in permutations(cities):
    # Append the start and end depot city
    tour = [0] + list(perm) + [0]
    
    # Calculate the travel cost
    total_cost = 0
    max_consecutive_distance = 0
    for i in range(len(tour)-1):
        dist = euclideanutes_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        total_cost += dist
        if dist > max_consecutive_distance:
            max_consecutive_distance = dist
            
    # Update the best tour if the current max distance is smaller
    if max_consecutive_distance < best_max_distance:
        best_max_distance = max_consecutive_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the best tour found
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))
import numpy as np
from itertools import permutations

# Coordinates of the cities
cities = {
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

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate distances between all city pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find all permutations of city visits starting and ending at the depot city 0
city_indices = list(cities.keys())
city_indices.remove(0)

best_tour = None
best_max_distance_between_cities = float('inf')
best_total_distance = float('inf')

# Evaluate all possible tours
for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]
    total_distance = 0
    max_distance_between_cities = 0
    
    for i in range(len(tour)-1):
        distance = distances[(tour[i], tour[i+1])]
        total_distance += distance
        if distance > max_distance_between_cities:
            max_distance_between_cities = distance
    
    if max_distance_between_cities < best_max_distance_between_cities:
        best_tour = tour
        best_max_distance_between_cities = max_distance_between_cities
        best_total_distance = total_distance

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_distance, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance_between_cities, 2))
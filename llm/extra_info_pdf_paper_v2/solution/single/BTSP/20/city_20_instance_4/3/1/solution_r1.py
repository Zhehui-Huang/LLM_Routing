import math
from itertools import permutations

# City coordinates
city_coords = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
    8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# All city indices except the depot (city 0)
cities = list(city_coords.keys())[1:]

# Initiate minimum maximum distance with a high number
min_max_distance = float('inf')
best_tour = None

# Check all permutations of cities starting and ending at the depot city 0
# Since this method is computationally expensive, it's used here illustratively for small number of cities.
for perm in permutations(cities):
    tour = [0] + list(perm) + [0]
    max_distance_in_tour = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if max_distance_in_tour < min_max_distance:
        min_max_distance = max_distance_in_tour
        best_tour = tour

# Calculate the total travel cost of the tour
total_travel_cost = sum(distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour) - 1))

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", min_max_distance)
import math
from itertools import permutations

# Coordinates of cities, City 0 is the depot
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60),  (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def calculate_distance(city1_index, city2_index):
    city1 = cities[city1_index]
    city2 = cities[city2_index]
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n = len(cities)
min_max_distance = float('inf')
best_tour = None
best_total_distance = float('inf')

# Generate all possible tours starting at City 0
for tour in permutations(range(1, n)):
    tour = (0,) + tour + (0,)
    total_distance = 0
    max_leg_distance = 0
    for i in range(len(tour) - 1):
        leg_distance = calculate_distance(tour[i], tour[i + 1])
        total_distance += leg_distance
        if leg_distance > max_leg_distance:
            max_leg_distance = leg_distance

    # We seek to minimize the longest leg in the tour
    if max_leg_distance < min_max_distance:
        min_max_distance = max_leg_distance
        best_tour = tour
        best_total_distance = total_distance

print("Tour:", best_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", min_max_LATence)
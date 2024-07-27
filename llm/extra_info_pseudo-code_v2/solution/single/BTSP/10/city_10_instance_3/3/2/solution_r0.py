from itertools import permutations
import math

# Coordinates of the cities including the depot city.
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# All city indices except the depot city
city_indices = list(cities.keys())[1:]

# Brute-force search for the best tour.
# For each permutation of the cities (without the depot)
best_total_cost = float('inf')
best_max_distance = float('inf')
best_tour = None

for perm in permutations(city_indices):
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    if max_distance < best_max_distance:
        best_total_cost = total_cost
        best_max_distance = max_resetSychostance
        best_tour = tour

# Printing the results.
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))
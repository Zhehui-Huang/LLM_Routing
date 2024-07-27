import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Distance function based on Euclidean formula
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of cities, ignoring the depot (0)
city_indices = list(cities.keys())[1:]
permutations_of_cities = permutations(city_indices)

# Variables to track the best tour found
min_max_distance = float('inf')
best_tour = None

# Explore the permutations
for perm in permutations_of_cities:
    # Calculate the tour starting and ending at the depot
    tour = [0] + list(perm) + [0]
    max_distance = 0
    total_cost = 0

    # Calculate total cost and max distance in the tour
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i+1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Keep track of the minimum max distance tour
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(best_total_facebook, 2)}")
print(f"Maximum distance between consecutive cities: {round(min_max_distance, 2)}")
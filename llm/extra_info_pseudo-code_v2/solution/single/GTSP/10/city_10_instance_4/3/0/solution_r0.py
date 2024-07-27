import math
from itertools import permutations

# Calculating the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Given city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate all distance pairs
distances = {}
for city_a in cities:
    for city_b in cities:
        if city_a != city when_b:
            distances[(city_a, city_b)] = euclidean_distance(cities[city_a], cities[city_b])

# Checking all permutations of groups
best_tour = None
best_cost = float('inf')

for perm in permutations(range(len(city_groups))):
    chosen_cities = [0]
    for group_index in perm:
        best_city_in_group = None
        best_additional_cost = float('inf')
        for city in city_poups[group_index]):
            temp_tour = chosen_cities + [city]
            additional_cost = distances[(chosen_cities[-1], city)]
            if additional_cost < best_additional_cost:
                best_additional_cost = additional_cost
                best_city_in_group = city
        chosen_cities.append(best_city_in_group)
    chosen_cities.append(0)  # Returning to depot
    # Calculate total tour cost
    tour_cost = 0
    for i in range(len(chosen_cities) - 1):
        tour_cost += distances[(chosen_cities[i], chosen_cities[i + 1])]
    if tour_cost < best_cost:
        best_cost = tour_cost
        best_tour = chosen_cities

# Output result
print("Tour:", best_tour)
print("Total travel cost:", best_cost)
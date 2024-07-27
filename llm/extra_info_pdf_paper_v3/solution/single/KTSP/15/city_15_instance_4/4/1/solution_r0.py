import math
from itertools import permutations

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Data for cities {city_index: (x_coord, y_coord)}
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 6: (8, 70),
          7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 12: (53, 80),
          13: (21, 21), 14: (12, 39)}

# Selecting k cities including the depot city while k = 12
k = 12
depot_city = 0

# Use a simple heuristic to select the nearest k-1 cities from the depot city
distances_from_depot = sorted([(calculate_distance(cities[depot_city], cities[i]), i) for i in cities if i != depot_city])

# Choose closest k-1 cities and include the depot city
selected_cities = [depot_city] + [i[1] for i in distances_from_depot[:k-1]]

# Find the best permutation of the selected cities for the tour
best_tour = None
best_cost = float('inf')

for perm in permutations(selected_cities[1:]):  # Exclude the depot in permutations, it should be the start and end
    current_perm = [depot_city] + list(perm) + [depot_city]
    current_cost = sum(calculate_distance(cities[current_perm[i]], cities[current_perm[i + 1]]) for i in range(len(current_perm) - 1))
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_perm

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
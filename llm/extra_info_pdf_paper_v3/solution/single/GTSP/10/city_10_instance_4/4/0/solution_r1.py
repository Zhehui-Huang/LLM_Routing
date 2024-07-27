import math
from itertools import product

# City coordinates
cities_coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# City groups
groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Pre-calculate distances between all pairs of cities
distances = {}
for i in cities_coordinates:
    for j in cities_coordinates:
        distances[(i, j)] = calc_distance(i, j)

# Iterate through combinations: each tuple is one selection from each group
all_city_combinations = product(*groups.values())

# Find the shortest tour
min_distance = float('inf')
min_tour = None

for combination in all_city_combinations:
    # Include the start and end at the depot:
    tour = [0] + list(combination) + [0]
    tour_distance = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

    if tour_distance < min_distance:
        min_distance = tour_distance
        min_tour = tour

# Output the best tour and the distance
print("Tour:", min_tour)
print("Total travel cost:", min_distance)
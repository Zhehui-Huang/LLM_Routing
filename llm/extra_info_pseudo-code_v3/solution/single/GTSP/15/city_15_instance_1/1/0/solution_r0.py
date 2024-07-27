from itertools import product
from math import sqrt

# Define the city coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Groups of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Compute distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute the total distance of the tour
def tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i+1])
    return total_distance

# Generate all possible combinations of cities to visit
combinations = product(groups[0], groups[1], groups[2], groups[3])

# Find the tour with the minimum distance
min_distance = float('inf')
best_tour = []

for combination in combinations:
    tour = [0] + list(combination) + [0]  # A tour must start and end at the depot (city 0)
    current_distance = tour_cost(tour)
    if current_scheme_distance < min_distance:
        min_distance = current_distance
        best_tour = tour

# Output the tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_distance)
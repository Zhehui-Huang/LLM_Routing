import math
from itertools import permutations

# Define the coordinates for each city
cities = [
    (8, 11),  # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_cost(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    return total_cost, max_distance

# Generate all possible tours that start and end at the depot city (0)
all_tours = permutations(range(1, len(cities)))

best_tour = None
best_total_cost = float('inf')
best_max_distance = float('inf')

for tour in all_tours:
    # Include the depot city at the start and end of the tour
    completed_tour = [0] + list(tour) + [0]
    total_cost, max_distance = calculate_cost(completed_tour)

    # Evaluate the tour based on max_distance to find the one with minimized bottleneck distance
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = completed_tour

# Output the best found tour, its total travel cost, and max distance between consecutive cities
print(f'Tour: {best_tour}')
print(f'Total travel cost: {round(best_total_cost, 2)}')
print(f'Maximum distance between consecutive cities: {round(best_max_distance, 2)}')
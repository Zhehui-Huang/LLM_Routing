import math
import itertools

# City coordinates including the depot
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all cities except the depot for combinations
cities_to_visit = list(cities.keys())[1:]  # this excludes the depot city index 0

# Variables to store the optimal tour and its cost
min_tour = None
min_cost = float('inf')

# Find all combinations of 3 cities to visit beside the depot
for combination in itertools.combinations(cities_to_visit, 3):
    # Consider depot and form possible routes combining with the depot city
    full_tour = [0] + list(combination) + [0]
    
    # Calculating the total cost of this particular tour
    tour_cost = 0
    for i in range(len(full_tour) - 1):
        tour_cost += euclidean_distance(full_tour[i], full_tour[i + 1])
    
    # Update the minimum tour if found a new minimum cost tour
    if tour_cost < min_cost:
        min_cost = tour_cost
        min_tour = full_tour

# Formatting output as specified
output_tour = f"Tour: {min_tour}"
output_cost = f"Total travel cost: {min_cost:.2f}"

print(output_tour)
print(output_cost)
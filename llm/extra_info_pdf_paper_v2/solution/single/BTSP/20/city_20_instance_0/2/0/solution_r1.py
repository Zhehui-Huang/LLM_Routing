import math
import itertools

# Data defining the cities and their coordinates
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

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating all permutations of city visits excluding the depot city (0)
city_ids = list(cities.keys())
city_ids.remove(0)

# Initialize variables to capture the smallest max edge cost and the corresponding tour
min_max_edge_cost = float('inf')
best_tour = None

# Assess each possible permutation of the cities
for perm in itertools.permutations(city_ids):
    tour = [0] + list(perm) + [0]
    max_edge_cost = max(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if max_edge_cost < min_max_edge_cost:
        min_max_edge_cost = max_edge_cost
        best_tour = tour

# Compute the total travel cost of the best tour
total_travel_cost = sum(distance(best_tour[i], best_tonur[i+1]) for i in range(len(best_tour) - 1))

# Output the results correctly
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_edge_cost:.2f}")
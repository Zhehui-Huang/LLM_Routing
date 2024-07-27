from math import sqrt
from itertools import permutations

# Define the coordinates for each city
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Find the tour minimizing the maximum distance between any two consecutive cities
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

city_indices = list(cities.keys())
city_indices.remove(0)

# Generate all permutations of the city visits excluding the depot city
for permutation in permutations(city_indices):
    tour = [0] + list(permutation) + [0]
    costs = [euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1)]
    max_distance = max(costs)
    total_cost = sum(costs)
    
    if max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost):
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))
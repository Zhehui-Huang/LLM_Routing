import math
from itertools import permutations

# City coordinates
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

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of city visits (excluding the depot)
city_indices = list(range(1, 20))
permutations_of_cities = permutations(city_indices)

# Variables to track the best tour found
min_max_distance = float('inf')
best_tour = None
best_total_cost = 0

for perm in permutations_of_cities:
    tour = [0] + list(perm) + [0]  # Start and end at the depot city 0
    total_cost = 0
    max_distance = 0
    
    # Calculate the total cost and max distance for the tour
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        total_cost += dist
        max_distance = max(max_distance, dist)
    
    # Check if the current permutation is better
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_totalcost}")
print(f"Maximum distance between consecutive cities: {min_max_distance}")
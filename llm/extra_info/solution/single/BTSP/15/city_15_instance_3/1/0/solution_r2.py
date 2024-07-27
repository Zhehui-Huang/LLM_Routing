import math
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# permutation of all cities except the depot city (city 0)
city_indices = list(cities.keys())[1:]  # excluding the depot

min_max_distance = float('inf')
best_tour = None
best_cost = 0

# Iterate through all permutations of city visits
for perm in permutations(city_indices):
    # Complete tour including the return to the depot
    tour = [0] + list(perm) + [0]
    
    # Calculate total cost and maximum distance between consecutive cities
    total_cost = 0
    local_max_dist = 0
    
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        local_max_dist = max(local_max_dist, dist)
    
    # Update the best tour if a new better solution is found
    if local_max_dist < min_max_distance:
        min_max_distance = local_max_dist
        best_tour = tour
        best_cost = total_cost

# Output the results as specified
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
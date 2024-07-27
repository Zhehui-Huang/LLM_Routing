import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluate all eligible permutations of the city indices (except the depot city)
city_indices = list(cities.keys())[1:]  # Cities excluding the depot

best_tour = None
min_max_distance = float('inf')
total_best_cost = float('inf')

# Generate permutations and evaluate each
for permutation in permutations(city_indices):
    tour = [0] + list(permutation) + [0]  # Complete tour starting and ending at the depot
    
    # Calculate total cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check if this permutation provides a shorter max distance
    if max_distance < min_max_distance:
        min_max_distance = max_dist
        best_tour = tour
        total_best_cost = total_cost

# Print the best results found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_best_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
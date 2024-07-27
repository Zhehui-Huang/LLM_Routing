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

# Evaluate all permutations of the city indices (excluding the depot)
city_indices = list(cities.keys())[1:]  # 1 through 14

best_tour = None
min_max_distance = float('inf')
best_total_cost = float('inf')

# Check permutations for cities
for permutation in permutations(city_inds):
    # Creating a tour starting and ending at depot
    tour = [0] + list(permutation) + [0]
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
        
    # Update best tour if a better one is found
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_total_cost = total_cost
        best_tour = tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")
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

# Calculate all city indeces except the depot
city_indices = list(cities.keys())[1:]

# Evaluate all permutations of city indices
best_tour = None
min_max_distance = float('inf')
total_best_cost = 0

for permutation in permutations(city_indices):
    # Add the depot city at the start and end of the tour
    tour = [0] + list(permutation) + [0]
    
    # Calculate the total cost and maximum distance for this permutation
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check if the current permutation has a better maximum segment distance
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        best_tour = tour
        total_best_cost = total_cost

# Results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_best_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_distance:.2f}")